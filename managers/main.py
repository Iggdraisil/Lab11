from managers.shoesShopManager import ShoesShopManager
from models import Shoes, Role, SportShoes, Material, ChildShoes, Season, ChildAge


shoesList = [Shoes(42, "Blue", Material.LEATHER, 5000, Season.SUMMER, Role.MEN, "LaCosta"),
             Shoes(46, "Black", Material.CLOUT, 500, Season.SUMMER, Role.WOMEN, "Abibas"),
             ChildShoes(23, "White", Material.LEATHER, 4000, Season.SUMMER,
                        Role.CHILD, "Antoshka", True, True, ChildAge.SCHOLARS),
             ChildShoes(12, "Rainbow", Material.RUBBER, 1000, Season.DEMI_SEASON,
                        Role.CHILD, "Lolikon", False, True, ChildAge.INFANT),
             SportShoes(39, "Purple", Material.FABRIKOID, 3000, Season.DEMI_SEASON,
                        Role.SPORT, "Nike", "Running", True),
             SportShoes(45, "Blue", Material.CLOUT, 100, Season.SUMMER,
                        Role.SPORT, "CoyoPC", "Walking", False)]

manager = ShoesShopManager(shoesList)

manager.print_list()

manager.print_external_list(manager.sort_by_price())

manager.print_external_list(manager.filter_by_role(Role.CHILD))

