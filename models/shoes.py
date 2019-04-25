class Shoes:

    def __init__(self, size, color, material, price, season, role, brand):
        self.size = size
        self.color = color
        self.material = material
        self.price = price
        self.season = season
        self.role = role
        self.brand = brand

    def __str__(self) -> str:
        return "\n\nCurrent Shoe:\n size: " + str(self.size) + "\n color: " \
               + self.color + "\n material: " + str(self.material) + "\n price: " \
               + str(self.price) + "\n season: " + str(self.season) + "\n role:" + str(self.role) \
               + "\n brand: " + self.brand
