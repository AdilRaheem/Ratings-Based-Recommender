# Ratings-Based-Recommender API

This is a Product Recommendation System for Walmart products, built with FastAPI.
It uses user-product ratings to generate product recommendations based on user similarity (cosine similarity) and serves precomputed recommendations via an API.

## 🚀 Features

✅ Precomputes personalized product recommendations from review data.
✅ Serves recommendations through a FastAPI backend.
✅ Supports deployment to cloud platforms like Render.
✅ Lightweight and fast response from precomputed .json.
✅ Scalable for integration with front-end websites.

## 📂 Project Structure

├── app.py                          # FastAPI backend
├── generate_recommendations.py     # Script to precompute recommendations
├── precomputed_recommendations.json # Generated recommendations
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
└── dataset/
    └── walmart_reviews.tsv         # (Place your dataset here)

## 📊 Dataset

The system expects a dataset in .tsv format (tab-separated) with columns like:
Uniq Id, Product Id, Product Rating, Product Reviews Count, Product Category, Product Brand, Product Name, Product Image Url, Product Description, Product Tags, Product Contents
Example path:
dataset/product_ratings.tsv

## ⚙️ Installation & Setup

1️⃣ Clone the repository:
git clone https://github.com/AdilRaheem/Ratings-Based-Recommender.git
cd Ratings-Based-Recommender

2️⃣ Install dependencies:
pip install -r requirements.txt

3️⃣ Add your dataset:
Place your .tsv file inside a dataset/ folder.

4️⃣ Precompute recommendations:
python generate_recommendations.py
This generates precomputed_recommendations.json which is served by the API.

## 🌐 Running the API locally

uvicorn app:app --reload --host 0.0.0.0 --port 8000
Visit http://127.0.0.1:8000/docs for the interactive Swagger API documentation.

## 📌 API Endpoints

Method: GET	Endpoint: 	/	Description: Health check (Welcome message).

Method: GET	Endpoint: /recommendations/{user_id}	Description: Get top 5 product recommendations for a user.

## 🛠 Example Usage
curl http://127.0.0.1:8000/recommendations/12345

Response:
[{"Name":"NEXXUS Color Assure Shampoo 13.50 oz (Pack of 4)","Brand":"Nexxus","ImageURL":"https://i5.walmartimages.com/asr/0cf0b1f0-2908-4a45-89f0-672bc179d36e_1.0c5cd0b5f0509fedff860becdea499e1.jpeg","Rating":0.0},{"Name":"3 Pack Dove Go Fresh Pear & Aloe Antiperspirant Deodorant Spray, 150ml each","Brand":"Dove","ImageURL":"https://i5.walmartimages.com/asr/8f3e54ac-b7fe-40a1-93ea-25f707424271_1.42826adfb2e47aa4438237e84303e602.jpeg","Rating":5.0},{"Name":"Dove Revive Antiperspirant Deodorant, 2.6 oz, Twin Pack","Brand":"Dove","ImageURL":"https://i5.walmartimages.com/asr/620ea746-ce42-465c-bca6-4e7ca7ffbc43_1.e11b65acbdb66bacb94b0688b5ec226a.jpeg | https://i5.walmartimages.com/asr/f0582d07-2b0e-4ece-879a-d7d1020ea9f6_1.3a3b8e354202585d70f73ffd5a6ebe28.jpeg | https://i5.walmartimages.com/asr/feebf73f-e933-4b9b-8fc4-b404952b2d0f_1.42cf808047375a025a882303ab8f2c0f.jpeg | https://i5.walmartimages.com/asr/225acb25-1db5-4197-8dc8-f16977d127a4_1.3d0a24dca4b19f250a92e6f5e673fca6.jpeg | https://i5.walmartimages.com/asr/0d0b4ca1-02cc-4e72-9434-c79bba526a13_1.30ca2eec9e59130f0606b65dd148296c.jpeg | https://i5.walmartimages.com/asr/32f838df-275b-403e-9bdb-b55042ce9d22_1.a57c80d77e51f21f4ee3113a0b0b19b1.jpeg | https://i5.walmartimages.com/asr/540cd06e-85f0-4430-93c4-67ac3544184c_1.b2816d1c3a4db5323e3f088200e5be50.jpeg","Rating":4.7},{"Name":"(3 pack) Aveeno Stress Relief Moisturizing Lotion to Calm & Relax, 18 fl. oz","Brand":"Aveeno","ImageURL":"https://i5.walmartimages.com/asr/6c2cbe8b-0d7e-4052-9268-2f6834246292_1.b933cc6e4bf9909fbc0a660519779bf4.jpeg | https://i5.walmartimages.com/asr/5f024034-eed9-485b-af2f-ab1c6bd50dad_1.ce2b091ba5b59da9af09941fddf1a589.jpeg | https://i5.walmartimages.com/asr/a3ccc4d6-98aa-41f9-8cbe-f4961796a68f_1.c1d55d7ddb9def6feb7615d6ef0d4121.jpeg | https://i5.walmartimages.com/asr/13c8dabb-9b88-470a-a736-8822796e4e01_1.7cca4da2eeb176d4ba2d758895df05e2.jpeg | https://i5.walmartimages.com/asr/894418c3-c6f7-4df4-bdfe-98a1029d375c_1.5575747745878ac4430a2e773961a14a.jpeg | https://i5.walmartimages.com/asr/40c3c2a3-d1bf-410f-9078-53fd731f15aa_1.44954a612931975b25ce1566629d01ec.jpeg","Rating":4.7},{"Name":"Dove Fragrance-Free Body Wash for Dry Skin 15.8 oz","Brand":"Dove","ImageURL":"https://i5.walmartimages.com/asr/5859a222-560e-49c1-a0ac-85c33264a730_1.b6e1e311e287c0ba4b1442e2b46a23ec.jpeg | https://i5.walmartimages.com/asr/66bb18ef-7c36-4942-8d42-a6d9cb32a07f_1.5cce9fe5f6d1ff5679237916597bbb98.jpeg | https://i5.walmartimages.com/asr/b90c12f1-9d55-4037-be71-6b1709c41545_1.a0dc77ec7b6e30e7d252374fe675e67a.jpeg | https://i5.walmartimages.com/asr/f378c7ef-af76-4436-8f07-33cfa67bf5e9_1.13ee7c0c672d9f37a41ab2305302e628.jpeg | https://i5.walmartimages.com/asr/d89d8a87-b670-4a72-8e9c-d908dc890d65_1.fc2c824fb56162c3b116e4bf881a2c5b.jpeg | https://i5.walmartimages.com/asr/1536341a-ec1f-4e9b-b4f1-069616fdcdf7_1.2c7fe4445c91818629f8200f6184a96d.jpeg | https://i5.walmartimages.com/asr/fed8c33c-7904-491d-a041-da9fb8f92aca_1.afbdc21fcbf7ff0d3a0255b7372adf8e.jpeg","Rating":4.6}]

## 🌍 Deployment on Render

Push this project to a public GitHub repository.
Sign up at https://render.com.
Create a Web Service:
Runtime: Python 3.x
Build Command: pip install -r requirements.txt
Start Command: uvicorn app:app --host 0.0.0.0 --port 10000
Add your dataset and precomputed .json to the repo before deploying.

## 🧠 Troubleshooting

Problem: precomputed_recommendations.json is empty	Solution: Check dataset quality and rerun the generator.
Problem: API returns empty results	Solution: Verify user IDs and recommendation data.
Problem: Render app resets data	Solution: Use persistent volumes or re-trigger generation.

## 🎯 Future Improvements

✅ Add dynamic recommendation generation endpoint (/generate).
✅ Handle new users and cold-start problems.
✅ Migrate to a persistent database (Postgres, MongoDB).
✅ Frontend integration.
