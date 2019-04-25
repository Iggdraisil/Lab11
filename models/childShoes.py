from models.shoes import Shoes


class ChildShoes(Shoes):

    def __init__(self, size, color, material, price, season, role, brand,
                 anatomic_last, supinator, child_age):
        super().__init__(size, color, material, price, season, role, brand)
        self.anatomic_last = anatomic_last
        self.supinator = supinator
        self.child_age = child_age

    def __str__(self) -> str:
        return super().__str__() + "\n anatomic last: " + str(self.anatomic_last) \
               + "\n supinator: " + str(self.supinator) + "\n child age: " + str(self.child_age)
