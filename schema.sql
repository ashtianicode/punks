DROP TABLE IF EXISTS images;

CREATE TABLE images (
    id INTEGER PRIMARY KEY,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    image_title TEXT NOT NULL,
    image_attributes TEXT NOT NULL,
    image_similars TEXT NOT NULL,
    image_address TEXT NOT NULL
);
