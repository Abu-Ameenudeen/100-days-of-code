class Tip_calculator:
    def __init__(self, bill_amt, tip):
        self.__bill_amt = bill_amt
        self.__tip = tip
        
    def split_amount(self, people):
        tip_per_person = (self.__tip/100) * self.__bill_amt
        bill_split = (self.__bill_amt/people) + tip_per_person
        return bill_split