import sqlite3
from flask import Flask, render_template
from werkzeug.exceptions import abort
from db_tools import DB
from recommender import get_similars, get_recommendations


# Init flaks app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'



# Route
@app.route('/')
def index():
    db = DB()
    images = db.get_images()
    db.conn.close()
    return render_template('index.html', images=images)




@app.route('/<int:image_id>')
def image(image_id):
    db = DB()
    image = db.get_image(image_id)
    if image is None:
        abort(404)

    # Get similar and recommended images    
    similars = get_similars(db,image,4)
    # hybrid_recommendation = get_recommendations(db,image,5)

    db.conn.close()
    return render_template('image.html', image=image, similars=similars)




