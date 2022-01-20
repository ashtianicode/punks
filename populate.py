from db_tools import DB
import json
import pandas as pd

# Init a db connection
db = DB()

# Fresh start with db
with open('schema.sql') as f:
    db.conn.executescript(f.read())


# Populate all images
punks = pd.read_json("data/punks.json")

for _,punk in punks.iterrows():
    id = str(punk['id'])
    image_address = f"punks/{punk['id']}.png"
    image_title = f"CryptoPunk #{punk['id']}"
    image_attributes = json.dumps(punk['accessories'])
    image_similars = json.dumps(punk['similars'])
    image_data = (id, image_title, image_attributes, image_address,image_similars)
    
    # create new image
    db.create_image(image_data)

