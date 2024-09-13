# Tạo một list ngẫu nhiên
import random
from statistic import Statistic
# arr = []
# for i in range (100):
#     a = random.randint(1,100)
#     arr.append(a)
arr = [28, 23, 30, 24, 19, 21, 39, 22, 22, 31, 37, 33, 20, 30, 35, 21, 30, 27, 28, 29, 27, 21, 25, 28, 26, 29, 29, 22, 32, 27]
# arr = [1,2,2,2,2,2,1,1,1,1,4,4,4,4,4,3,3,3,3,3]

print('Mẫu dữ liệu đã tạo: ')
print(arr)
print(f'Kích cỡ mẫu N = {len(arr)}')
arr.sort()
print('Mẫu sắp xếp:')
print(arr)
data = Statistic(arr)
print(data.createTable())
print(f'kỳ vọng {data.expectation()}')
print(f'phương sai {data.variance()}')
print(f'mode {data.mode()}')
print(f'trung vị {data.median()}')
print(f'tứ phân vị {data.quantile()}')
