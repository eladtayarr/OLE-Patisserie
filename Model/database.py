import pymongo
from pymongo import MongoClient
import uuid
from bson import ObjectId, json_util

SECRET_KEY = '0rsppWZt0kr5v1zclzlMFi3PEmGVgUT0HKaQZ68oiiLBERCRufUYRFy3b9UFanm2'
MONGO_URI = "mongodb+srv://elad:elad@cluster0.ecf8sfr.mongodb.net/myNewDatabase?retryWrites=true&w=majority"

class Database:
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client.myNewDatabase
        self.orders_collection = self.db.OpenOrders
        self.menu_collection = self.db.Menu
        self.opinion_collection = self.db.Opinion

    #######################################
    #          NEW   ORDER                #
    #######################################

    def add_order(self, cart, customer_name):
        order_id = str(uuid.uuid4())
        total_price = sum(item['price'] for item in cart)
        order = {
            "order_id": order_id,
            "customer_name": customer_name,
            "cart": cart,
            "total_price": total_price,
            "status": "open"
        }
        self.orders_collection.insert_one(order)
        return order_id

    def convert_order_to_json(self, order):
        return {
            "_id": str(order["_id"]),
            "order_id": order.get("order_id", ""),
            "total_price": order.get("total_price", 0),
            "status": order.get("status", "")
        }
    
    def get_open_orders(self):
        orders = list(self.orders_collection.find({"status": "open"}))
        return [self.convert_order_to_json(order) for order in orders]

    def close_order(self, order_id):
        self.orders_collection.update_one({"order_id": order_id}, {"$set": {"status": "closed"}})

    #######################################
    #             OPINION                 #
    #######################################

    def add_opinion(self, name, email, subject, message, rating):
        opinion = {
            "name": name,
            "email": email,
            "subject": subject,
            "message": message,
            "rating": rating
        }
        result = self.opinion_collection.insert_one(opinion)
        return result.inserted_id is not None

    def convert_review_to_json(self, review):
        return {
            "name": review.get("name", ""),
            "email": review.get("email", ""),
            "subject": review.get("subject", ""),
            "message": review.get("message", ""),
            "rating": review.get("rating", 0)
        }

    def get_reviews(self):
        reviews = list(self.opinion_collection.find())
        return [self.convert_review_to_json(review) for review in reviews]

    #######################################
    #             MENU                    #
    #######################################

    def add_dish(self, name, description, price, image_path):
        dish = {
            "name": name,
            "description": description,
            "price": price,
            "image": image_path
        }
        self.menu_collection.insert_one(dish)

    def convert_dish_to_json(self, dish):
        return {
            "name": dish.get("name", ""),
            "description": dish.get("description", ""),
            "price": dish.get("price", ""),
            "image": dish.get("image", "")
        }
    
    def get_menu(self):
        menu = list(self.menu_collection.find())
        return [self.convert_dish_to_json(dish) for dish in menu]
