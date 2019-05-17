import mysql.connector
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import sys

from models.shoes import Shoes

app = Flask(__name__)
app.config.from_pyfile("config.py")
cnx = mysql.connector.connect(user='root', password='barabak',
                              host='127.0.0.1', database='shoes_database',
                              auth_plugin='mysql_native_password')
ma = Marshmallow(app)
db = SQLAlchemy(app)

sys.path.insert(0, 'views')


class ShoesSchema(ma.Schema):
    class Meta:
        fields = ('size', 'color', 'price', 'season', 'role', 'brand', 'material')


shoe_schema = ShoesSchema()
shoes_schema = ShoesSchema(many=True)


@app.route("/shoes", methods=["POST"])
def add_shoe():
    count = Shoes.query.all()
    id = 0
    for i in count:
        id += 1
    size = request.json['size']
    color = request.json['color']
    price = request.json['price']
    season = request.json['season']
    role = request.json['role']
    brand = request.json['brand']
    material = request.json['material']

    new_shoe = Shoes(size, color, material, price, season, role, brand, id)

    db.session.add(new_shoe)
    db.session.commit()

    return jsonify(request.json)


@app.route("/shoes", methods=["GET"])
def get_shoe():
    all_shoes = Shoes.query.all()
    result = shoes_schema.dump(all_shoes)
    return jsonify(result)


@app.route("/shoes/<id>", methods=["GET"])
def shoe_detail(id):
    shoe = Shoes.query.get(id)
    return shoe_schema.jsonify(shoe)


@app.route("/shoes/<id>", methods=["PUT"])
def shoe_update(id):
    shoes = Shoes.query.get(id)

    size = request.json['size']
    color = request.json['color']
    price = request.json['price']
    season = request.json['season']
    role = request.json['role']
    brand = request.json['brand']
    material = request.json['material']

    shoes.size = size
    shoes.color = color
    shoes.price = price
    shoes.season = season
    shoes.role = role
    shoes.brand = brand
    shoes.material = material

    db.session.commit()
    return shoe_schema.jsonify(shoes)


@app.route("/shoes/<id>", methods=["DELETE"])
def shoe_delete(id):
    shoe = Shoes.query.get(id)
    db.session.delete(shoe)
    db.session.commit()

    return shoe_schema.jsonify(shoe)


if __name__ == '__main__':
    app.run()
