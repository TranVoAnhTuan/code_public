import math
import pandas as pd
class Statistic:
    arr = []
    table = None
    k = 0
    h = 0
    check = False
    def __init__(self, arr: list = arr, table = table, k: int = k, h: int = h, check: bool = check) -> None:
        self.__arr = arr if arr else []
        self.__table = table
        self.__k = k
        self.__h = h
        self.__check = check

    def disaggregate(self):
        array = set(self.__arr)
        n = len(array)
        k = math.ceil((2 * len(self.__arr)) ** (1/3)) #group number
        if n > k and n > 10:
            h = math.ceil(((max(self.__arr) - min(self.__arr)) - (k - 1)) / k) #group distance
            self.__k = k
            self.__h = h
        else:
            self.__k = n
            self.__h = 0
            self.__check = True
        return self.__k, self.__h
    
    def createTable(self):
        k, h = self.disaggregate()
        if self.__check: 
            res = {}
            for element in self.__arr:
                if element in res:
                    res[element] += 1
                else:
                    res[element] = 1
            representative = list(res.keys())
            frequency = list(res.values())
            cumulative_frequency = []
            for i in range (k):
                if (i+1) == 1:
                    cumulative_frequency.append(frequency[i])
                else:
                    cumulative_frequency.append((frequency[i] + cumulative_frequency[i-1]))
            self.__table = pd.DataFrame({'X': representative, 'frequency': frequency, 'cumulative_frequency': cumulative_frequency})
            return self.__table
        else:
            # Calculate the element for each group
            group_element = []
            for i in range(k):
                if (i+1) < k:
                    lower_bound = min(self.__arr) + i * h
                    upper_bound = lower_bound + h
                    group_element.append(str(lower_bound) + " - " + str(upper_bound))
                else:
                    lower_bound = min(self.__arr) + i * h
                    upper_bound = max(self.__arr)
                    group_element.append(str(lower_bound) + " - " + str(upper_bound))
            
            # Calculate the representive element for each group
            representative_element = []
            for i in range(k):
                if (i+1) < k:
                    lower_bound = min(self.__arr) + i * h
                    upper_bound = lower_bound + h
                    representative_element.append((upper_bound + lower_bound) / 2)
                else:
                    lower_bound = min(self.__arr) + i * h
                    upper_bound = max(self.__arr)
                    representative_element.append((upper_bound + lower_bound) / 2)

            # Calculate the frequency for each group
            frequency = []
            for i in range(k):
                if (i+1) < k:
                    lower_bound = min(self.__arr) + i * h
                    upper_bound = lower_bound + h
                    frequency.append(len(list(filter(lambda x: lower_bound <= x < upper_bound, self.__arr))))
                else:
                    lower_bound = min(self.__arr) + i * h
                    frequency.append(len(list(filter(lambda x: lower_bound <= x, self.__arr))))

            # Calculate the cumulative frequency
            cumulative_frequency = []
            for i in range (k):
                if (i+1) == 1:
                    cumulative_frequency.append(frequency[i])
                else:
                    cumulative_frequency.append((frequency[i] + cumulative_frequency[i-1]))

            # Create Dataframe
            self.__table = pd.DataFrame({'group element': group_element, 'representative element': representative_element, 'frequency': frequency, 'cumulative frequency' : cumulative_frequency})          
            return self.__table
    
    def expectation(self):
        if self.__check:
            X = (1/len(self.__arr)) * sum(self.__table['X'] * self.__table['frequency'])
        else:
            X = (1/len(self.__arr)) * sum(self.__table['representative element'] * self.__table['frequency'])
        return X
    
    def variance(self):
        X = self.expectation()
        if self.__check:
            var = sum((self.__table['X'] - X) ** 2)/(len(self.__arr) - 1)
        else:
            var = sum((self.__table['representative element'] - X) ** 2)/(len(self.__arr) - 1)
        return  var
    
    def standardDeviation(self):
        X = self.variance()
        return math.sqrt(X)

    def mode(self):
        Mode = []
        frequency_max = self.__table['frequency'].max()
        max_index = self.__table[self.__table['frequency']==frequency_max].index
        if len(max_index) == len(self.__table['frequency']):
            return 'Không có yếu vị'
        else:
            if self.__check:
                for index in max_index:
                    Mode.append(self.__table['X'][index])
            else:
                for index in max_index:
                    lower_bound, upper_bound = self.__table['group element'][index].split('-')
                    hMo = float(upper_bound) - float(lower_bound)
                    nMo = self.__table['frequency'][index]

                    nMoLower = self.__table['frequency'][index-1] if index != 0 else 0
                    nMoUpper = self.__table['frequency'][index+1] if index != len(self.__table['frequency']) - 1 else 0
                    if ((nMo - nMoLower) + (nMo - nMoUpper)) != 0:
                        Mode.append(float(lower_bound) + (hMo*((nMo - nMoLower)/((nMo - nMoLower) + (nMo - nMoUpper)))))
                    else:
                        nMoLower = 0
                        nMoUpper = 0
                        Mode.append(float(lower_bound) + (hMo*((nMo - nMoLower)/((nMo - nMoLower) + (nMo - nMoUpper)))))
            return Mode 

    def median(self):
        if self.__check:
            
        else:
            xMed = 0
            for i in self.__table['cumulative frequency']:
                if i > (len(self.__arr)+1)/2:
                    Index = self.__table[self.__table['cumulative frequency'] == i].index[0]
                    xMed = self.__table.loc[Index]
                    SMedLower = self.__table['cumulative frequency'][Index - 1]
                    break
            lower_bound, upper_bound = xMed['group element'].split('-')
            hMed = int(upper_bound) - int(lower_bound)
            nMed = xMed['frequency']
            return float(lower_bound) + (hMed * ((len(self.__arr)/2) - SMedLower)/nMed)
        
    def quantile(self):
        n = len(self.__arr)
        count = 1
        res = []
        while(count < 4):
            xMed = 0
            for i in self.__table['cumulative frequency']:
                if i > (count * (n+1)) / 4:
                    Index = self.__table[self.__table['cumulative frequency'] == i].index[0]
                    xMed = self.__table.loc[Index]
                    SMedLower = self.__table['cumulative frequency'][Index - 1] if Index != 0 else 0
                    break
            lower_bound, upper_bound = xMed['group element'].split('-')
            hMed = int(upper_bound) - int(lower_bound)
            nMed = xMed['frequency']
            res.append(float(lower_bound) + (hMed * ((count*n/4) - SMedLower)/nMed))
            count += 1
        return res

    
    
            

        