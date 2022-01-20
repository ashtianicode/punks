import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cur = self.conn.cursor()
        self.conn.row_factory = dict_factory
        
    
    def create_image(self, new_image):
        self.cur.execute("INSERT INTO images (id, image_title, image_attributes,image_address,image_similars) VALUES (?, ?, ?, ?, ?)", new_image)
        self.conn.commit()


    def get_images(self):
        images = self.conn.execute('SELECT * FROM images').fetchall()
        return images


    def get_image(self,image_id):
        image = self.conn.execute('SELECT * FROM images WHERE id = ?', (image_id,)).fetchone()
        return image
