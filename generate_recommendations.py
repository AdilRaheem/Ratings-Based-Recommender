#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def load_data_from_google_sheets(sheet_name):
    """Fetch dataset from Google Sheets."""
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    
    # Load credentials from JSON key file
    creds = ServiceAccountCredentials.from_json_keyfile_name("database-for-recommendation-4245c30a6549.json", scope)
    client = gspread.authorize(creds)

    # Open the Google Sheet
    spreadsheet = client.open(sheet_name)
    worksheet = spreadsheet.sheet1  # Access first sheet

    # Convert to DataFrame
    data = worksheet.get_all_records()
    df = pd.DataFrame(data)
    return df

def main():
    # Load dataset from Google Sheets
    sheet_name = "Ratings-based-Data"  # actual sheet name
    train_data = load_data_from_google_sheets(sheet_name)
    train_data = train_data[:1500]

    # Column renaming
    column_name_mapping = {
        'Uniq Id': 'ID',
        'Product Id': 'ProdID',
        'Product Rating': 'Rating',
        'Product Reviews Count': 'ReviewCount',
        'Product Category': 'Category',
        'Product Brand': 'Brand',
        'Product Name': 'Name',
        'Product Image Url': 'ImageURL',
        'Product Description': 'Description',
        'Product Tags': 'Tags',
        'Product Contents': 'Contents'
    }
    train_data.rename(columns=column_name_mapping, inplace=True)

    # Preprocess data
    train_data.fillna({
        'Rating': 0,
        'ReviewCount': 0,
        'Category': '',
        'Brand': '',
        'Description': ''
    }, inplace=True)

    train_data['ID'] = train_data['ID'].astype(str)
    train_data['ProdID'] = train_data['ProdID'].astype(str)

    # Create user-item matrix
    user_item_matrix = train_data.pivot_table(
        index='ID', 
        columns='ProdID', 
        values='Rating', 
        aggfunc='mean'
    ).fillna(0)

    # Compute user similarity
    user_similarity = cosine_similarity(user_item_matrix)
    user_indices = {user: idx for idx, user in enumerate(user_item_matrix.index)}

    # Precompute recommendations
    precomputed_recommendations = {}

    for user_id, user_index in user_indices.items():
        user_similarities = user_similarity[user_index]
        similar_users_indices = np.argsort(user_similarities)[::-1][1:]  # Exclude self

        recommended_items = []
        for similar_user_idx in similar_users_indices:
            rated_by_similar_user = user_item_matrix.iloc[similar_user_idx]
            not_rated_by_target_user = (rated_by_similar_user > 0) & (user_item_matrix.iloc[user_index] == 0)
            recommended_items.extend(user_item_matrix.columns[not_rated_by_target_user][:10])

        recommendations = train_data[
            train_data['ProdID'].isin(recommended_items)
        ][['Name', 'Brand', 'ImageURL', 'Rating']].drop_duplicates()

        precomputed_recommendations[user_id] = recommendations.head(5).to_dict(orient="records")

    # Save recommendations to JSON
    output_file = "precomputed_recommendations.json"
    with open(output_file, "w", encoding='utf-8') as f:
        json.dump(precomputed_recommendations, f, indent=4)

    print("✅ Precomputed recommendations saved!")

if __name__ == "__main__":
    main()
