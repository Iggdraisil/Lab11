

class ShoesShopManager:
    def __init__(self, list):
        self.list = list

    def sort_by_price(self, sort_type=False):
        return sorted(self.list, key=lambda x1: x1.price, reverse=sort_type)

    def sort_by_size(self, sort_type=False):
        return sorted(self.list, key=lambda x1: x1.size, reverse=sort_type)

    def filter_by_role(self, role):
        return filter(lambda x: x.role == role, self.list)

    def filter_by_size(self, size):
        return filter(lambda x: x.size == size, self.list)

    def print_list(self):
        for elem in self.list:
            print(elem)
        print("\n\n\n end of current list\n")

    @staticmethod
    def print_external_list(list):
        for elem in list:
            print(elem)
        print("\n\n\n end of current list\n")
