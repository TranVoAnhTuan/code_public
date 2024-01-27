import math
import pandas as pd
class Statistic: #Tạo lớp Statistic để thực hiện các phép tính toán
    # Khai báo các biến dùng để tính toán về giá trị cơ bản ban đầu
    arr = []  #Mẫu dữ liệu thô đầu vào
    table = None #Bảng thống kê
    k = 0   #Số tổ
    h = 0   #Số nhóm
    check = False  ## Biến kiểm tra điều kiện tạo bảng thống kê
    #Hàm def dùng để khởi tạo
    def __init__(self, arr: list = arr, table = table, k: int = k, h: int = h, check: bool = check) -> None:
        self.__arr = arr if arr else []
        self.__table = table
        self.__k = k
        self.__h = h
        self.__check = check

    #Hàm 'disaggregate' dùng để phân tổ cho dữ liệu
    def disaggregate(self):
        array = set(self.__arr)
        n = len(array) #Kích cỡ mẫu
        k = math.ceil((2 * len(self.__arr)) ** (1/3)) #Tính số tổ
        #Kiểm tra điều kiện để xác định xem có cần phân tách thành nhóm hay không
        if n > k and n > 10:
            #Tính khoảng cách nhóm (h) bằng cách chia khoảng giá trị
            #của dữ liệu cho số lượng nhóm (k), với điều chỉnh để đảm 
            #bảo kết quả là một số nguyên bằng hàm 'math.ceil'
            h = math.ceil(((max(self.__arr) - min(self.__arr)) - (k - 1)) / k)
            self.__h = h
        #Ngược lại, nếu không đủ lớn, không cần phân tách và thiết lập __check là True.
        else:
            self.__k = n
            self.__h = 0
            self.__check = True
        return self.__k, self.__h
    
    #Hàm 'createTable' dùng để tạo bảng
    def createTable(self):
        k, h = self.disaggregate() # Lấy ra số tổ và khoảng cách từ phương thức 'disaggregate'
        if self.__check: # Kiểm tra xem có cần phân tách hay không (__check là True)
            res = {} #Tạo một từ điển để lưu trữ tần suất xuất hiện của từng phần tử.
            for element in self.__arr: #Duyệt qua từng phần tử trong mẫu dữ liệu.
                #Kiểm tra xem phần tử đã có trong từ điển hay chưa. Nếu có, tăng tần suất xuất hiện lên 1.
                if element in res: 
                    res[element] += 1
                else:#Nếu phần tử chưa có trong từ điển, thêm phần tử vào và đặt tần suất xuất hiện là 1.
                    res[element] = 1
            representative = list(res.keys()) #Tạo danh sách các phần tử đại diện.
            frequency = list(res.values()) #Tạo danh sách các tần suất xuất hiện tương ứng với từng phần tử.
            cumulative_frequency = [] #Tạo danh sách để lưu trữ tần suất tích lũy.
            for i in range (k):#Duyệt qua mỗi nhóm.
                #Nếu đang xét nhóm đầu tiên, thêm tần suất xuất hiện của nhóm đó vào danh sách tần suất tích lũy.
                if (i+1) == 1:
                    cumulative_frequency.append(frequency[i])
                #Nếu đang xét nhóm khác, thêm tần suất của nhóm đó cộng với tần suất tích lũy của nhóm trước vào danh sách tần suất tích lũy.
                else:
                    cumulative_frequency.append((frequency[i] + cumulative_frequency[i-1]))
            #Tạo Bảng từ các danh sách và lưu vào biến thành viên __table.
            self.__table = pd.DataFrame({'X': representative, 'frequency': frequency, 'cumulative_frequency': cumulative_frequency})
            return self.__table
        else:#Nếu không cần, tạo bảng thống kê dựa trên tần suất xuất hiện của từng phần tử.
            # Calculate the element for each group
            group_element = []
            for i in range(k):
                if (i+1) < k: #Nếu tổ đang xét không phải tổ cuối
                    lower_bound = min(self.__arr) + i * h 
                    upper_bound = lower_bound + h
                    group_element.append(str(lower_bound) + " - " + str(upper_bound))
                else:#Nếu tổ đang xét là tổ cuối thì chặn trên sẽ là phần tử lớn nhất của mẫu dữ liệu
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

            # Tính tần số xuất hiện các phần tử
            frequency = [] #Khởi tạo một danh sách để lưu trữ tần suất của từng nhóm.
            for i in range(k):#Duyệt qua mỗi nhóm.
                #Nếu đang xét nhóm không phải là nhóm cuối cùng, thực hiện các bước sau để tính toán tần suất của nhóm đó.
                if (i+1) < k:
                    lower_bound = min(self.__arr) + i * h #Tính cận dưới tổ đó
                    upper_bound = lower_bound + h #Tính cận trên tổ đó
                    #Tính tần suất của nhóm bằng cách sử dụng hàm filter và len. 
                    #Hàm filter lọc ra các giá trị nằm trong khoảng giá trị của nhóm,
                    #sau đó len đếm số lượng phần tử trong danh sách được lọc. 
                    #Tần suất này sau đó được thêm vào danh sách frequency.
                    frequency.append(len(list(filter(lambda x: lower_bound <= x < upper_bound, self.__arr))))
                else: #Nếu là tổ cuối cùng làm tương tự nhưng cận trên là không có
                    lower_bound = min(self.__arr) + i * h
                    frequency.append(len(list(filter(lambda x: lower_bound <= x, self.__arr))))

            #Tính tần số tích lũy
            cumulative_frequency = [] #Tạo list chứa tần số tích lũy của các tổ
            for i in range (k):
                if (i+1) == 1: #nếu là tố đầu tiên thì tần số tích lũy sẽ là tần số của tổ đó
                    cumulative_frequency.append(frequency[i])
                else: #Các tổ còn lại thì tần số tích lũy sẽ là Tần sô tổ + tần số của tổ trước đó
                    cumulative_frequency.append((frequency[i] + cumulative_frequency[i-1]))

            # Tạo bảng
            self.__table = pd.DataFrame({'group element': group_element, 'representative element': representative_element, 'frequency': frequency, 'cumulative frequency' : cumulative_frequency})          
            return self.__table
    #Tính kỳ vọng
    def expectation(self):
        #Kiểm tra xem dữ liệu đã được phân tách thành nhóm (tính toán theo từng giá trị cụ thể) hay chưa (__check là True).
#         Nếu dữ liệu không phải là dữ liệu được phân tách,
#         tính giá trị kỳ vọng (X) bằng cách lấy tổng của tích của mỗi giá trị và tần suất của nó,
#         sau đó chia cho tổng tất cả các tần suất.
#         Công thức này được sử dụng để tính giá trị kỳ vọng cho dữ liệu không phải là dữ liệu phân nhóm.
        if self.__check:
            X = (1/len(self.__arr)) * sum(self.__table['X'] * self.__table['frequency'])
        else:#Trường hợp dữ liệu đã được phân tách thành nhóm.
#          Tính giá trị kỳ vọng (X) bằng cách lấy tổng của tích của mỗi phần tử đại diện cho nhóm
#          và tần suất của nó, sau đó chia cho tổng tất cả các tần suất. Công thức này được sử dụng
#          để tính giá trị kỳ vọng cho dữ liệu đã được phân tách thành nhóm.
            X = (1/len(self.__arr)) * sum(self.__table['representative element'] * self.__table['frequency'])
        return X
    #Tính phương sai
    def variance(self):
        X = self.expectation() #Nhận giá trị kỳ vọng của phương thức expectation
        if self.__check: #Kiểm tra dữ liệu đã phân tách thành nhóm chưa, nếu chưa thì
             #tính phương sai (var) bằng cách lấy tổng của bình phương của hiệu giữa mỗi
             #giá trị và giá trị kỳ vọng, sau đó chia cho (n - 1), với n là kích thước mẫu. 
            var = sum((self.__table['X'] - X) ** 2)/(len(self.__arr) - 1)
        else:#Dữ liệu đã được phân nhóm
            #Tính phương sai (var) bằng cách lấy tổng của bình phương của hiệu giữa mỗi
            #phần tử đại diện cho nhóm và giá trị kỳ vọng, sau đó chia cho (n - 1) 
            var = sum((self.__table['representative element'] - X) ** 2)/(len(self.__arr) - 1)
        return  var
    #Hàm standardDeviation tính độ lệch chuẩn của dữ liệu dựa trên giá trị phương sai 
    def standardDeviation(self):
        X = self.variance()
        return math.sqrt(X)
    #Hàm mode dùng để tìm yếu vị
    def mode(self):
        Mode = [] #Khởi tạo một danh sách để lưu trữ giá trị yếu vị các tổ.
        frequency_max = self.__table['frequency'].max() #Tìm giá trị tần suất lớn nhất trong bảng thống kê.
        # Tìm chỉ mục của các dòng trong bảng thống kê mà có tần suất bằng với giá trị tần suất lớn nhất.
        max_index = self.__table[self.__table['frequency']==frequency_max].index
        #Kiểm tra nếu tất cả các dòng trong bảng thống kê có tần suất bằng nhau và bằng tần suất lớn nhất,
        #thì trả về chuỗi 'Không có yếu vị', vì không có giá trị nào xuất hiện nhiều nhất.
        if len(max_index) == len(self.__table['frequency']):
            return 'Không có yếu vị'
        else:
            if self.__check: # Kiểm tra xem dữ liệu đã được phân tách thành nhóm hay chưa (__check là True).
                #Nếu không phải dữ liệu phân nhóm, thêm giá trị của cột 'X' (giá trị) tại các chỉ mục có tần suất 
                #lớn nhất vào danh sách yếu vị (Mode).
                for index in max_index:
                    Mode.append(self.__table['X'][index]) 
            else: #Trường hợp dữ liệu đã được phân tách thành nhóm.
                for index in max_index: #Duyệt qua các chỉ mục có tần suất lớn nhất.
                    # Lấy giá trị dưới và trên cùng của nhóm từ cột 'group element'.
                    lower_bound, upper_bound = self.__table['group element'][index].split('-')
                    hMo = float(upper_bound) - float(lower_bound)#ính kích thước nhóm (hMo) từ giá trị dưới và trên cùng của nhóm.
                    nMo = self.__table['frequency'][index]# Lấy tần suất của nhóm.

                    nMoLower = self.__table['frequency'][index-1] if index != 0 else 0 #Lấy tần suất của nhóm liền trước (nếu có) hoặc đặt là 0.
                    # Lấy tần suất của nhóm liền sau (nếu có) hoặc đặt là 0.
                    nMoUpper = self.__table['frequency'][index+1] if index != len(self.__table['frequency']) - 1 else 0
                    #Kiểm tra nếu tổng của tần suất của nhóm hiện tại và nhóm liền trước, cộng với tần suất của nhóm hiện tại và nhóm liền sau, khác 0.
                    if ((nMo - nMoLower) + (nMo - nMoUpper)) != 0:
                        Mode.append(float(lower_bound) + (hMo*((nMo - nMoLower)/((nMo - nMoLower) + (nMo - nMoUpper)))))
                    else:
                        nMoLower = 0
                        nMoUpper = 0
                        Mode.append(float(lower_bound) + (hMo*((nMo - nMoLower)/((nMo - nMoLower) + (nMo - nMoUpper)))))
            return Mode 
    #Tìm trung vị
    def median(self): 
        if self.__check: #Kiểm tra xem dữ liệu đã được phân tách thành nhóm hay chưa 
            if self.__k % 2 == 0:#Nếu số lượng nhóm là số chẵn.
                #Tính giá trị trung vị bằng cách lấy trung bình của hai giá trị ở vị trí k/2 và (k + 2)/2 
                return (self.__table['X'][(self.__k /2)] + self.__table['X'][((self.__k + 2) /2)])/2
            else:#Trường hợp số lượng nhóm là số lẻ.
                #Trả về giá trị trung vị tại vị trí (k + 1)/2
                return self.__table['X'][(self.__k + 1) / 2]
        else: #Trường hợp dữ liệu đã được phân tách thành nhóm thì dùng công thức tính như bình thường
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
        
    #Tìm tứ phân vị
    def quantile(self):

        count = 1#Khởi tạo biến đếm để theo dõi các giá trị phân vị.
        res = []#Khởi tạo danh sách để lưu trữ các giá trị phân vị.
        if self.__check:#Kiểm tra xem dữ liệu đã được phân tách thành nhóm hay chưa, nếu chưa thì
            while(count < 4):#Vòng lặp để tính 3 giá trị phân vị.
                if count != 2:#Nếu không phải là giá trị phân vị thứ hai.
                    #Tính giá trị phân vị bằng cách lấy giá trị ở vị trí count * (k + 1) / 4 
                    res.append(self.__table['X'][math.floor((count * (self.__k + 1)) / 4)])
                else:#Trường hợp giá trị phân vị thứ hai.
                    if self.__k % 2 == 0:#Nếu số lượng nhóm là số chẵn.
                        #Tính giá trị phân vị bằng cách lấy trung bình của hai giá trị ở vị trí k/2 và (k + 2)/2 
                        res.append((self.__table['X'][(self.__k /2)] + self.__table['X'][((self.__k + 2) /2)])/2)
                    else:#Trường hợp số lượng nhóm là số lẻ.
                        #Tính giá trị phân vị bằng cách lấy giá trị ở vị trí (k + 1)/2 
                        res.append(self.__table['X'][(self.__k + 1) / 2])
                count += 1
        else:# Trường hợp dữ liệu đã được phân tách thành nhóm.
            while(count < 4):#Vòng lặp để tính 3 giá trị phân vị.
                xMed = 0#Khởi tạo biến xMed để lưu trữ thông tin về nhóm chứa giá trị phân vị.
                for i in self.__table['cumulative frequency']:#Duyệt qua các giá trị tần suất tích lũy.
                    if i > (count * (len(self.__arr)+1)) / 4:#Nếu giá trị tần suất tích lũy vượt qua giữa của mẫu.
                        #Tìm chỉ mục của nhóm chứa giá trị phân vị.
                        Index = self.__table[self.__table['cumulative frequency'] == i].index[0]
                        xMed = self.__table.loc[Index]#Lưu trữ thông tin về nhóm chứa giá trị phân vị.
                        #Lưu giá trị tần suất tích lũy của nhóm trước đó (nếu có).
                        SMedLower = self.__table['cumulative frequency'][Index - 1] if Index != 0 else 0
                        break#Dừng vòng lặp
                lower_bound, upper_bound = xMed['group element'].split('-')#Tách giá trị dưới và trên cùng của nhóm từ cột 'group element'.
                hMed = int(upper_bound) - int(lower_bound)#Tính kích thước nhóm (hMed) từ giá trị dưới và trên cùng của nhóm.
                nMed = xMed['frequency']#Lấy tần suất của nhóm.
                # Tính giá trị phân vị bằng cách sử dụng công thức cho dữ liệu phân nhóm 
                #và thêm vào danh sách giá trị phân vị (res).
                res.append(float(lower_bound) + (hMed * ((count*len(self.__arr)/4) - SMedLower)/nMed))
                count += 1
        return res
