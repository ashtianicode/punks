from db_tools import DB
from recommender import get_similars
import unittest


class TestBackend(unittest.TestCase):

    def test_db_tools(self):
        db = DB()
        images = db.get_images()
        self.assertTrue(len(images) > 0 ,"There are no images in db")	

        image = db.get_image(0)
        self.assertIsNotNone(image ,"Image 0 is none")	

        db.conn.close()

        
    def test_all_images_attributes(self):
        db = DB()
        images = db.get_images()
        for image in images:
            self.assertTrue(len(image["image_title"]) > 0,"Image 0 title is empty")
            self.assertTrue( ".png" in image["image_address"] ,"Images should be png")


    def test_get_similars(self):
        db = DB()
        image = db.get_image(0)
        similars = get_similars(db,image,4)
        self.assertIsInstance(similars ,list,"get_similars() should return list")	


if __name__ == '__main__':
    unittest.main()