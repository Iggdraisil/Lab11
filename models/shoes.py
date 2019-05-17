from managers.appf import db


class Shoes(db.Model):
    __tablename__ = 'shoes'
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(20))
    color = db.Column(db.String(20))
    price = db.Column(db.String(20))
    season = db.Column(db.String(20))
    role = db.Column(db.String(20))
    brand = db.Column(db.String(20))
    material = db.Column(db.String(20))

    def __init__(self, size=40, color="Blue", material=3, price=1000, season=1, role=1, brand="Abibbas", id =0):
        self.size = size
        self.color = color
        self.material = material
        self.price = price
        self.season = season
        self.role = role
        self.brand = brand
        self.id = id

    def __str__(self) -> str:
        return "\n\nCurrent Shoe:\n size: " + str(self.size) + "\n color: " \
               + self.color + "\n material: " + str(self.material) + "\n price: " \
               + str(self.price) + "\n season: " + str(self.season) + "\n role:" + str(self.role) \
               + "\n brand: " + self.brand
