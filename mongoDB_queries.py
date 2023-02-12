
from pymongo import MongoClient

# Connect to the MongoDB database
client = MongoClient("mongodb://localhost:27017/")
db = client["leclerc_fr"]
collection = db["products"]

# Function to get the total number of products
def get_total_products():
    return collection.count_documents({})

# Function to get the number of products with discount
def get_discounted_products():
    return collection.count_documents({"original_price": {"$ne": "$sale_price"}})

# Function to get the number of unique brands
def get_unique_brands():
    return len(collection.distinct("brand"))

# Function to get the count of products for each brand
def get_products_count_by_brand():
    return collection.aggregate([
        {"$group": {"_id": "$brand", "count": {"$sum": 1}}}
    ])

# Function to get the count of discounted products for each brand
def get_discounted_products_count_by_brand():
    return collection.aggregate([
        {"$match": {"original_price": {"$ne": "$sale_price"}}},
        {"$group": {"_id": "$brand", "count": {"$sum": 1}}}
    ])

# Function to get the count of distinct product URLs for category "vetement-homme"
def get_distinct_product_urls_for_category():
    return len(collection.distinct("product_page_url", {"product_category": "vetement-homme"}))

# Function to get the number of products with EAN
def get_products_with_ean():
    return collection.count_documents({"ean": {"$exists": True}})

# Function to get the number of products with sale price greater than original price
def get_products_with_higher_sale_price():
    return collection.count_documents({"sale_price": {"$gt": "$original_price"}})

# Function to get the number of products with sale price greater than 300
def get_products_with_sale_price_over_300():
    return collection.count_documents({"sale_price": {"$gt": 300}})

# Function to get the number of products with discount percentage greater than 30%
def get_products_with_discount_over_30():
    return collection.count_documents({"discount_percentage": {"$gt": 30}})

# Function to get the number of products with 50% discount
def get_products_with_50_discount():
    return collection.count_documents({"discount_percentage": 50})

# Function to get the brand selling the most number of products in each category
def get_most_selling_brand_by_category():
    return collection.aggregate([
        {"$group": {"_id": {"brand": "$brand", "category": "$product_category"}, "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
    ])
    