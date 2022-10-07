

class Item:
    def __init__(self, category="", condition=0.0, age=0):
        if not isinstance(category,str) or not isinstance(condition,(float,int)) or not isinstance(age,(float,int)):
            raise TypeError("Invalid parameters. Please check category is string, condition is float and age is float")
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        
        self.condition=round(self.condition)
        
        condition_dict = {
            0: "poor",
            1: "mhaa",
            2: "hmmm",
            3: "okay",
            4: "YeahAaaa.",
            5: "GIMME!!!"
        }
        return condition_dict[self.condition]

    # alternate implementation:
    #
    # def condition_description(self):
    #     if self.condition > 5:
    #         return "wow"
    #     elif self.condition > 4:
    #         return "ooo"
    #     elif self.condition > 3:
    #         return "okay"
    #     elif self.condition > 2:
    #         return "eh"
    #     else:
    #         return "meh"
