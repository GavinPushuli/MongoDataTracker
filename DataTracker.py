import pymongo

db_name = 'datatracker' 

mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")

db = mongo_client.db_name # Create a Mongo Database and name it Data Tracker.

product_collection = db["product"]
top_product_collection = db["top_product"] # Create a collection for your top 3 products in MongoDB.

product_collection.delete_many({})
top_product_collection.delete_many({})

# Add your SPRINT 3 products file to MongoDB you just created.
query = [{ "product_name": "Simba", "product_type": "Chips", "product_available": 120, "product_price": 16.00, "product_description": "Simba Chips is a popular South African brand of potato crisps", "product_avg_cost": 12.00 }, { "product_name": "Lays", "product_type": "Chips", "product_available": 37, "product_price": 22.50, "product_description": "We pack them with the utmost care to create the superb quality chips you have come to expect from Lay's", "product_avg_cost": 16.88 }, { "product_name": "Coke", "product_type": "Cooldrinks", "product_available": 100, "product_price": 15.74, "product_description": "Coca-Cola, or Coke, is a carbonated soft drink manufactured by The Coca-Cola Company ", "product_avg_cost": 11.81 }, { "product_name": "Fanta", "product_type": "Cooldrinks", "product_available": 85, "product_price": 14.60, "product_description": "Fanta is a brand of fruit-flavored carbonated drinks created by Coca-Cola Deutschland under the leadership of German businessman Max Keith.", "product_avg_cost": 10.95 }, { "product_name": "Cadbury", "product_type": "Chocolates", "product_available": 45, "product_price": 12.00, "product_description": 'Cadbury Chocolates', "product_avg_cost": 9.00 }, { "product_name": "Tex", "product_type": "Chocolates", "product_available": 13, "product_price": 16.00, "product_description": 'Tex Chocolates', "product_avg_cost": 12.00 }, { "product_name": "Pepper Steak", "product_type": "Pies", "product_available": 10, "product_price": 18.99, "product_description": 'Pepper Steak Pie', "product_avg_cost": 14.24 }, { "product_name": "Chicken", "product_type": "Pies", "product_available": 34, "product_price": 16.00, "product_description": 'Chicken Pie', "product_avg_cost": 12.00 }, { "product_name": "Pear", "product_type": "Fruit", "product_available": 92, "product_price": 9.00, "product_description": 'Pear Fruit', "product_avg_cost": 6.75 }, { "product_name": "Apple", "product_type": "Fruit", "product_available": 120, "product_price": 5.45, "product_description": 'Apple Fruit', "product_avg_cost": 4.09 }, { "product_name": "Orange", "product_type": "Fruit", "product_available": 120, "product_price": 7.00, "product_description": 'Orange Fruit', "product_avg_cost": 5.25 }, { "product_name": "Vanilla", "product_type": "Cupcakes", "product_available": 150, "product_price": 12.70, "product_description": 'Vanilla Cupcake', "product_avg_cost": 9.53 }, { "product_name": "Chocolate", "product_type": "Cupcakes", "product_available": 150, "product_price": 14.00, "product_description": 'Chocolate Cupcake', "product_avg_cost": 10.50 }, { "product_name": "Spinach", "product_type": "Veggies", "product_available": 46, "product_price": 10.00, "product_description": 'Spinach', "product_avg_cost": 7.50 }, { "product_name": "Cabbage", "product_type": "Veggies", "product_available": 50, "product_price": 10.00, "product_description": 'Cabbage', "product_avg_cost": 7.50
}]

stmt = product_collection.insert_many(query) # Implement a descending sort to your data in MongoDB.

product_collection.find().sort('product_name', -1)

top_product_collection = db["top_product"] 

query2 = query[:3]
stmt2 = top_product_collection.insert_many(query2) # Create a collection for your top 3 products in MongoDB.

query3 = query[-3:]
stmt3 = top_product_collection.insert_many(query3) # Insert multiple documents into your collections in question (3) 

result1 = top_product_collection.delete_many({'product_name': {'$regex': 'Simba|Lays'}}) # Delete 2 brands from your collection of top 3 products.
print(f'{result1.deleted_count} product(s) deleted.')

query4 = {'product_name':'Cabbage'}
newValues = {"$set": {'product_name': 'Banana', 'product_type': 'Fruit'}}

stmt4 = top_product_collection.update_one(query4, newValues) # Update 1 product and its brands from your collection you created in question (3).
print(f'{stmt4.modified_count} product(s) updated.')

query5 = product_collection.find().sort('product_available').limit(5)
