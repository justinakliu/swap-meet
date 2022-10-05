
class Vendor:
    def __init__(self, inventory=None, condition=0):
        self.inventory = inventory if inventory is not None else []
        self.condition = condition

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category):
        category_list = []
        for item in self.inventory:
            if category == item.category:
                category_list.append(item)
        return category_list

    def swap_items(self, friend_vendor, my_item, their_item):

        if friend_vendor.inventory and self.inventory:
            if my_item in self.inventory and their_item in friend_vendor.inventory:
                friend_vendor.inventory.append(my_item)
                self.inventory.append(their_item)
                self.inventory.remove(my_item)
                friend_vendor.inventory.remove(their_item)
                return True
            return False
        return False

    def swap_first_item(self, friend_vendor):
        if self.inventory and friend_vendor.inventory:
            if self.inventory[0] and friend_vendor.inventory[0]:
                friend_vendor.inventory.append(self.inventory[0])
                self.inventory.append(friend_vendor.inventory[0])
                self.inventory.remove(self.inventory[0])
                friend_vendor.inventory.remove(friend_vendor.inventory[0])
            return True
        return False

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
                self.swap_items(other,me,them)
                return True
        return False
            
    