

## CryptoPunk Recommendation Engine
I'm building a recommendation engine for cryptopunks. 
Right now it is simply finding similar punks based on intersection of their attributes.
But ultimately we want to have a hybrid recommendation engine using years of bidding data, and the attributes combined. 


## Work to be done on recommendation 
- Use bidding data for cryptopunks to train a hybrid LightFM recommnedation model (works great with cold starts)
- Build a fast way of generating a similarity matrix for attributes. and then try TF-IDF.
- Read HEX color codes from the image, and use KNN to find punks with similar color combinations.

## Turn this into a research platform for studying auction research
Use bidding history for modeling auction revenue maximization, which would spit out profit-maximizing reserve price range for seller, and bid price range for bidder. 
Check these out:
https://srdas.github.io/MLBook/Auctions.html#introduction-5
https://cheeptalk.files.wordpress.com/2009/11/profit-maximizing-auctions.pdf
https://www.cs.ubc.ca/~cs532l/gt2/slides/11-6.pdf
https://theory.stanford.edu/~tim/f13/l/l5.pdf
https://www.cs.toronto.edu/~nisarg/teaching/304f17/slides/CSC304-L11.pdf


## How to run
```
pip3 install -r requirements.txt
python3 populate.py
export FLASK_APP=app
flask run

```

![Punks](docs/punks.png)
![Similars](docs/similars.png)

