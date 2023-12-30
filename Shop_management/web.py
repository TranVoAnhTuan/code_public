from bill import Bill
from brand import Brand
from category import Category
from customer import Customer
from discount_list import DiscountList
from discount import Discount
from product import Product
from shop import Shop
from user import User

#create Category
cate1 = Category()
cate1.setID('111')
cate1.setName('smartphone')

cate2 = Category()
cate2.setID('222')
cate2.setName('PC')

cate3 = Category()
cate3.setID('333')
cate3.setName('laptop')

#create Brand
brand1 = Brand()
brand1.setID('101')
brand1.setName('Apple')
brand1.setCountry('US')

brand2 = Brand()
brand2.setID('102')
brand2.setName('Samsung')
brand2.setCountry('Korean')

brand3 = Brand()
brand3.setID('103')
brand3.setName('Lenovo')
brand3.setCountry('China')

#create product
product11 = Product()
product11.setID('011')
product11.setName('Iphone 15 Plus')
product11.setProductCategory(cate1)
product11.setBrand(brand1)
product11.setQuantity(1000)
product11.setListPrice(1099.0)

product21 = Product()
product21.setID('021')
product21.setName('Iphone 15 Plus')
product21.setProductCategory(cate1)
product21.setBrand(brand1)
product21.setQuantity(500)
product21.setListPrice(1099.0)

product31 = Product()
product31.setID('031')
product31.setName('Iphone 15 Plus')
product31.setProductCategory(cate1)
product31.setBrand(brand1)
product31.setQuantity(500)
product31.setListPrice(1099.0)

product41 = Product()
product41.setID('041')
product41.setName('Iphone 15 Plus')
product41.setProductCategory(cate1)
product41.setBrand(brand1)
product41.setQuantity(1000)
product41.setListPrice(1099.0)

product12 = Product()
product12.setID('012')
product12.setName('Macbook Pro')
product12.setProductCategory(cate3)
product12.setBrand(brand1)
product12.setQuantity(1000)
product12.setListPrice(1200.0)

product22 = Product()
product22.setID('022')
product22.setName('Macbook Pro')
product22.setProductCategory(cate3)
product22.setBrand(brand1)
product22.setQuantity(200)
product22.setListPrice(1200.0)

product32 = Product()
product32.setID('032')
product32.setName('Macbook Pro')
product32.setProductCategory(cate3)
product32.setBrand(brand1)
product32.setQuantity(1000)
product32.setListPrice(1200.0)

product42 = Product()
product42.setID('042')
product42.setName('Macbook Pro')
product42.setProductCategory(cate3)
product42.setBrand(brand1)
product42.setQuantity(1000)
product42.setListPrice(1200.0)

product13 = Product()
product13.setID('013')
product13.setName('Thinkpad')
product13.setProductCategory(cate3)
product13.setBrand(brand3)
product13.setQuantity(200)
product13.setListPrice(1200.0)

product23 = Product()
product23.setID('023')
product23.setName('Thinkpad')
product23.setProductCategory(cate3)
product23.setBrand(brand3)
product23.setQuantity(100)
product23.setListPrice(1200.0)

product43 = Product()
product43.setID('043')
product43.setName('Thinkpad')
product43.setProductCategory(cate3)
product43.setBrand(brand3)
product43.setQuantity(50)
product43.setListPrice(1200.0)

product14 = Product()
product14.setID('014')
product14.setName('S22 Ultra')
product14.setProductCategory(cate1)
product14.setBrand(brand2)
product14.setQuantity(200)
product14.setListPrice(999.0)

product24 = Product()
product24.setID('024')
product24.setName('S22 Ultra')
product24.setProductCategory(cate1)
product24.setBrand(brand2)
product24.setQuantity(50)
product24.setListPrice(999.0)

product44 = Product()
product44.setID('044')
product44.setName('S22 Ultra')
product44.setProductCategory(cate1)
product44.setBrand(brand2)
product44.setQuantity(250)
product44.setListPrice(999.0)

product15 = Product()
product15.setID('015')
product15.setName('iMac')
product15.setProductCategory(cate2)
product15.setBrand(brand1)
product15.setQuantity(10)
product15.setListPrice(2000.0)

product25 = Product()
product25.setID('025')
product25.setName('iMac')
product25.setProductCategory(cate2)
product25.setBrand(brand1)
product25.setQuantity(15)
product25.setListPrice(2000.0)

product35 = Product()
product35.setID('035')
product35.setName('iMac')
product35.setProductCategory(cate2)
product35.setBrand(brand1)
product35.setQuantity(1000)
product35.setListPrice(2000.0)

product45 = Product()
product45.setID('045')
product45.setName('iMac')
product45.setProductCategory(cate2)
product45.setBrand(brand1)
product45.setQuantity(20)
product45.setListPrice(2000.0)

# create Customer
customer1 = Customer()
customer1.setID('1')
customer1.setName('Tuan')

customer2 = Customer()
customer2.setID('2')
customer2.setName('Bao')

customer3 = Customer()
customer3.setID('3')
customer3.setName('Thang')

customer4 = Customer()
customer4.setID('4')
customer4.setName('Hieu')

customer5 = Customer()
customer5.setID('5')
customer5.setName('Phuc')

#create user
user11 = User()
user11.setID('u11')
user11.setName('Loi')

user12 = User()
user12.setID('u12')
user12.setName('Nghia')

user21 = User()
user21.setID('u21')
user21.setName('Nhan')

user22 = User()
user22.setID('u22')
user22.setName('Trang')

user31 = User()
user31.setID('u31')
user31.setName('Kiet')

user32 = User()
user32.setID('u32')
user32.setName('Khoa')

user33 = User()
user33.setID('u33')
user33.setName('Dung')

user34 = User()
user34.setID('u34')
user34.setName('Bao')

user41 = User()
user41.setID('u41')
user41.setName('Chi')

user42 = User()
user42.setID('u42')
user42.setName('Yen')

#create shop
shop1 = Shop()
shop1.setID('s1')
shop1.setName('Hoang Ha')
shop1.addToProduct(product11)
shop1.addToProduct(product12)
shop1.addToProduct(product13)
shop1.addToProduct(product14)
shop1.addToProduct(product15)
shop1.addToUser(user11)
shop1.addToUser(user12)

shop2 = Shop()
shop2.setID('s2')
shop2.setName('Cellphone')
shop2.addToProduct(product21)
shop2.addToProduct(product22)
shop2.addToProduct(product23)
shop2.addToProduct(product24)
shop2.addToProduct(product25)
shop2.addToUser(user21)
shop2.addToUser(user22)

shop3 = Shop()
shop3.setID('s3')
shop3.setName('Apple Store')
shop3.addToProduct(product31)
shop3.addToProduct(product32)
shop3.addToProduct(product35)
shop3.addToUser(user31)
shop3.addToUser(user32)
shop3.addToUser(user33)
shop3.addToUser(user34)

shop4 = Shop()
shop4.setID('s4')
shop4.setName('The gioi di dong')
shop4.addToProduct(product41)
shop4.addToProduct(product42)
shop4.addToProduct(product43)
shop4.addToProduct(product44)
shop4.addToProduct(product45)
shop4.addToUser(user41)
shop4.addToUser(user42)

#Create discount
discount1 = Discount()
discount1.setAll(True)
discount1.setDeal(0.05)
discount1.setTime('30/10/2023','11/11/2023')

discount2 = Discount()
discount2.setBrand(brand1)
discount2.setDeal(0.04)
discount2.setTime('15/09/2023','03/01/2024')

discount3 = Discount()
discount3.setCategory(cate1)
discount3.setDeal(0.045)
discount3.setTime('10/10/2023','02/12/2023')

discount4 = Discount()
discount4.setBrand(brand2)
discount4.setDeal(0.1)
discount4.setTime('20/10/2023','20/11/2023')

discount5 = Discount()
discount5.setCategory(cate3)
discount5.setDeal(0.15)
discount5.setTime('05/09/2023', '20/11/2023')

discount6 = Discount()
discount6.setProductID('023')
discount6.setDeal(0.2)
discount6.setTime('01/10/2023', '23/02/2024')

#create discount list
discountList = DiscountList()
discountList.addToDiscountList(discount1)
discountList.addToDiscountList(discount2)
discountList.addToDiscountList(discount3)
discountList.addToDiscountList(discount4)
discountList.addToDiscountList(discount5)
discountList.addToDiscountList(discount6)

#create bill
bill1 = Bill()
bill1.setCustomer(customer1)
bill1.addToProduct(product11, 4)
bill1.addToProduct(product12, 3)
bill1.setDiscountList(discountList)
bill1.setDate('20/11/2023')
print(bill1.orderTotal())

# user update current price
user11.updateProductCurrentPrice('011', 850)
# print(user11.getInformation())

#display 
shop1.getProductCategoryList('smartphone')
shop1.getProductCurrentPrice(1200.0)

#Total Inventory Cost
print(f"Total Inventory Cost: {shop1.getTotalInventoryCost()}")





