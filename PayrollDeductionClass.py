class PayrollDeductionTransaction:
    def __init__(self, desc, date, chargeAmt, id):
        self.__desc = desc
        self.__date = date
        self.__chargeAmt = chargeAmt
        self.__id = id

    def getDescription(self):
        return self.__desc
    
    def getDate(self):
        return self.__date
    
    def getChargeAmount(self):
        return self.__chargeAmt
    
    def getID(self):
        return self.__id
