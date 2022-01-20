import json


def get_similars(db, image, similar_count):
    image_similars = json.loads(image["image_similars"])
    most_similars_ids = list(image_similars.keys())[:similar_count]
    most_similars = []
    for id in most_similars_ids:
        if id == image["id"]:
            continue
        
        img = db.get_image(id)
        most_similars.append( img )
    return most_similars

    

        

def get_recommendations():
    pass