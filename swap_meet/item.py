class Item:
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
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
