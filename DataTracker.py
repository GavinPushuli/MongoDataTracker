import pymongo

dbName = 'datatracker' 

mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")

db = mongoClient.db_name # Create a Mongo Database and name it Data Tracker.

itemCollection = db["product"]
firstItemCollection = db["firstProduct"] # Create a collection for your top 3 products in MongoDB.

itemCollection.delete_many({})
firstItemCollection.delete_many({})

# Add your SPRINT 3 products file to MongoDB you just created.
query = [{ "itemName": "Zambak", "itemType": "LipBalm", "itemsAvailable": 120, "itemPrice": 7.50, "itemDescription": "Most commonly used South African brand", "avrgCost": 5.00 }, { "itemName": "Labello", "itemType": "LipBalm", "itemsAvailable": 37, "itemPrice": 22.50, "itemDescription": "Safe and healthcare quality lip balm", "avrgCost": 16.88 }, { "itemName": "Coke", "itemType": "Cooldrinks", "itemsvailable": 100, "itemPrice": 15.74, "itemDescription": "Coca-Cola, or Coke, is a carbonated soft drink manufactured by The Coca-Cola Company ", "avrgCost": 11.81 }, { "itemName": "Fanta", "itemType": "Cooldrinks", "itemsvailable": 85, "itemPrice": 14.60, "itemDescription": "Fanta is a brand of fruit-flavored carbonated drinks created by Coca-Cola Deutschland under the leadership of German businessman Max Keith.", "avrgCost": 10.95 }, { "itemName": "Cadbury", "itemType": "Chocolates", "itemsAvailable": 45, "itemPrice": 12.00, "itemDescription": 'Cadbury Chocolates', "avrgCost": 9.00 }, { "itemName": "Tex", "itemType": "Chocolates", "itemsAvailable": 13, "itemPrice": 16.00, "itemDescription": 'Tex Chocolates', "avrgCost": 12.00 }, { "itemName": "Pepper Steak", "itemType": "Pies", "itemsAvailable": 10, "itemPrice": 18.99, "itemDescription": 'Pepper Steak Pie', "avrgCost": 14.24 }, { "itemName": "Chicken", "itemType": "Pies", "itemAvailable": 34, "itemPrice": 16.00, "itemDescription": 'Chicken Pie', "avrgCost": 12.00 }, { "itemName": "Pear", "itemType": "Fruit", "itemsAvailable": 92, "itemPrice": 9.00, "itemDescription": 'Pear Fruit', "avrgCost": 6.75 }, { "itemName": "Apple", "itemType": "Fruit", "itemAvailable": 120, "itemPrice": 5.45, "itemDescription": 'Apple Fruit', "itemCost": 4.09 }, { "itemName": "Orange", "itemType": "Fruit", "itemsAvailable": 120, "itemPrice": 7.00, "itemDescription": 'Orange Fruit', "avrgCost": 5.25 }, { "itemName": "Vanilla", "itemType": "Cupcakes", "itemsAvailable": 150, "itemPrice": 12.70, "itemDescription": 'Vanilla Cupcake', "avrgCost": 9.53 }, { "itemName": "Chocolate", "itemType": "Cupcakes", "itemsAvailable": 150, "itemPrice": 14.00, "itemDescription": 'Chocolate Cupcake', "avrgCost": 10.50 }, { "itemName": "Spinach", "itemType": "Veggies", "itemsAvailable": 46, "itemPrice": 10.00, "itemDescription": 'Spinach', "avrgCost": 7.50 }, { "itemName": "Cabbage", "itemType": "Veggies", "itemsAvailable": 50, "itemPrice": 10.00, "itemDescription": 'Cabbage', "avrgCost": 7.50
}]

stmt = itemCollection.insert_many(query) # Implement a descending sort to your data in MongoDB.

itemCollection.find().sort('itemName', -1)

firstItemCollection = db["firstProduct"] 

query2 = query[:3]
stmt2 = firstItemCollection.insert_many(query2) # Create a collection for your top 3 products in MongoDB.

query3 = query[-3:]
stmt3 = firstItemCollection.insert_many(query3) # Insert multiple documents into your collections in question (3) 

result1 = firstItemCollection.delete_many({'itemName': {'$regex': 'Zambak|Labello'}}) # Delete 2 brands from your collection of top 3 products.
print(f'{result1.deleted_count} product(s) deleted.')

query4 = {'itemName':'Cabbage'}
newValues = {"$set": {'itemName': 'Banana', 'itemType': 'Fruit'}}

stmt4 = firstItemCollection.update_one(query4, newValues) # Update 1 product and its brands from your collection you created in question (3).
print(f'{stmt4.modified_count} product(s) updated.')

query5 = itemCollection.find().sort('itemsAvailable').limit(5)
