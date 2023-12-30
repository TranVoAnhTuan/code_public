class DiscountList:
    discountList = []
    def __init__(self, discountList: list = discountList) -> None:
        self.__discountList = discountList
    
    def addToDiscountList(self, discount: object):
        self.__discountList.append(discount)

    def findDiscount(self, date: str):
        totalDiscount = []
        day, month, year = date.split('/')
        day = int(day)
        month = int(month)
        year = int(year)
        for discount in self.__discountList:
            dayStart, monthStart, yearStart = discount.getStartTime().split('/')
            dayStart = int(dayStart)
            monthStart = int(monthStart)
            yearStart = int(yearStart)

            dayEnd, monthEnd, yearEnd = discount.getEndTime().split('/')
            dayEnd = int(dayEnd)
            monthEnd = int(monthEnd)
            yearEnd = int(yearEnd)
            
            if year == yearStart and year == yearEnd:
                if month > monthStart and month == monthEnd:
                    if day <= dayEnd:
                        totalDiscount.append(discount)
                elif month == monthStart and month <= monthEnd:
                    if day >= dayStart:
                        totalDiscount.append(discount)
                elif month > monthStart and month < monthEnd:
                    totalDiscount.append(discount)
            elif year > yearStart and year == yearEnd:
                if month < monthEnd:
                    totalDiscount.append(discount)
                elif month == monthEnd:
                    if day <= dayEnd:
                        totalDiscount.append(discount)
            elif year == yearStart and year < yearEnd:
                if month > monthStart:
                    totalDiscount.append(discount)
                elif month == monthStart:
                    if day >= dayStart:
                        totalDiscount.append(discount)
        return totalDiscount