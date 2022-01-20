import pandas as pd
import json

punks = pd.read_json("https://raw.githubusercontent.com/raymondfeng/punks.attributes/master/punks.json")
punks = punks.iloc[:1000]


def dict_to_key_value_pairs(img):
  return [f"{k}:{v}" for (k,v) in img["accessories"].items() ]


def find_similars(selected_image):
      # Get keys for selected image
      selected_attributes = set(selected_image["accessories_joined"])

      # Search over all other images, with similar attributes
      similars = []
      for _,img in punks.iterrows():
            img_attributes =  set(img["accessories_joined"])
            similarity = selected_attributes.intersection(img_attributes)
            if len(similarity) > 0:
              similars.append({"id":img["id"], "similarity_count":len(similarity) })     
      
      # Sort descending by similarity count
      similars = sorted(similars, key=lambda item: item["similarity_count"],reverse=True)
      similars = {s["id"]:s["similarity_count"] for s in similars }
      
      return similars



# Turn {key:value, ...} into [ "key:value", ...]
punks["accessories_joined"] = punks.apply(lambda selected_image: dict_to_key_value_pairs(selected_image), axis=1) 

# Find similars and write ids to similars columns
images = punks.copy()
images["similars"] = images.apply(lambda selected_image: find_similars(selected_image), axis=1)

# Dump the punks with similars
images.to_json("data/punks.json")