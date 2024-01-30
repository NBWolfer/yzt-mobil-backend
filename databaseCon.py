from pymongo.mongo_client import MongoClient
import dotenv

# Replace the placeholder with your Atlas connection string
uri = dotenv.get_key(dotenv.find_dotenv(), "MONGODB_URI")

# Create a new client and connect to the server
def get_db():
    client = MongoClient(uri)
    db = client['yzt-mobil-app']
    return db