class Item:
    def __init__(self, category=None, condition=0):
        self.category = category if category is not None else ''
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
