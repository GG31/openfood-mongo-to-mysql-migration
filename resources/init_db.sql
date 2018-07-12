USE openfood;

CREATE TABLE product(id INT auto_increment, name VARCHAR(100), nutriment_per_qty varchar(100), language VARCHAR(100), barcode VARCHAR(20), PRIMARY KEY (id));

CREATE TABLE category(id INT auto_increment, tag VARCHAR(100), name VARCHAR(100), PRIMARY KEY (id));
CREATE TABLE product_category(
product_id INT,
category_id INT,
FOREIGN KEY (product_id) REFERENCES product(id),
FOREIGN KEY (category_id) REFERENCES category(id)
);

CREATE TABLE brand(id INT auto_increment, tag VARCHAR(100), name VARCHAR(100), PRIMARY KEY (id));
CREATE TABLE product_brand(
product_id INT, brand_id INT,
FOREIGN KEY (product_id) REFERENCES product(id),
FOREIGN KEY (brand_id) REFERENCES brand(id)
);

CREATE TABLE ingredient(id INT auto_increment, tag VARCHAR(100), name VARCHAR(100), PRIMARY KEY (id));
CREATE TABLE product_ingredient(
product_id INT, ingredient_id INT,
FOREIGN KEY (product_id) REFERENCES product(id),
FOREIGN KEY (ingredient_id) REFERENCES ingredient(id)
);

CREATE TABLE nutriment(id INT auto_increment, tag VARCHAR(100), quantity VARCHAR(100), PRIMARY KEY (id));
CREATE TABLE product_nutriment(
product_id INT, nutriment_id INT,
FOREIGN KEY (product_id) REFERENCES product(id),
FOREIGN KEY (nutriment_id) REFERENCES nutriment(id)
);

CREATE TABLE keyword(id INT auto_increment, name VARCHAR(100), PRIMARY KEY (id));
CREATE TABLE product_keyword(
product_id INT, keyword_id INT,
FOREIGN KEY (product_id) REFERENCES product(id),
FOREIGN KEY (keyword_id) REFERENCES keyword(id)
);

CREATE TABLE additive(id INT auto_increment, tag VARCHAR(100), PRIMARY KEY (id));
CREATE TABLE product_additive(
product_id INT, additive_id INT,
FOREIGN KEY (product_id) REFERENCES product(id),
FOREIGN KEY (additive_id) REFERENCES additive(id)
);

CREATE TABLE product_trace(
product_id INT, ingredient_id INT,
FOREIGN KEY (product_id) REFERENCES product(id),
FOREIGN KEY (ingredient_id) REFERENCES ingredient(id)
);

CREATE TABLE country(id INT auto_increment, tag VARCHAR(100), name VARCHAR(100), PRIMARY KEY (id));
CREATE TABLE product_country_selling(
product_id INT, country_id INT,
FOREIGN KEY (product_id) REFERENCES product(id),
FOREIGN KEY (country_id) REFERENCES country(id)
);
CREATE TABLE product_country_origin(
product_id INT, country_id INT,
FOREIGN KEY (product_id) REFERENCES product(id),
FOREIGN KEY (country_id) REFERENCES country(id)
);