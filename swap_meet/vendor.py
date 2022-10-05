
class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        # (O(n))
        if item in self.inventory:
            # O(n)
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        items_in_category = []

        for item in self.inventory:
            if item.category == category:
                items_in_category.append(item)

        return items_in_category

    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            self.remove(my_item)
            vendor.add(my_item)
            vendor.remove(their_item)
            self.add(their_item)
            return True
        else:
            return False

    def swap_first_item(self, vendor):
        if not self.inventory or not vendor.inventory:
            return False
        self.inventory[0], vendor.inventory[0] = vendor.inventory[0], self.inventory[0]
        return True

    def get_best_by_category(self, category):
        category_list = self.get_by_category(category)
        if category_list:
            category_list.sort(key=lambda item: item.condition, reverse=True)
            return category_list[0]
        return None
    def swap_best_by_category(self, other, my_priority, their_priority):
        me = self.get_best_by_category(their_priority)
        them = other.get_best_by_category(my_priority)
        if me and them:
            self.swap_items(other, me, them)
            return True
        return False
