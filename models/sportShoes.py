from models.shoes import Shoes


class SportShoes(Shoes):
    def __init__(self, size, color, material, price, season, role, brand, sport_type, spec_enhancements):
        super().__init__(size, color, material, price, season, role, brand)
        self.sport_type = sport_type
        self.spec_enhancements = spec_enhancements

    def __str__(self) -> str:
        return super().__str__() + "\n sport type: " + self.sport_type \
               + "\n special enhancements: " + str(self.spec_enhancements)
