# Computer Bazar
# 1.Dell(20000)
# 2.Toshiba(30000)
# 3.Mac(50000)
# select option : 1 or any
# enter quantity : any
# delivery: 1.Home(1000)  2.Pickup(free)
# packing : 1.Plastic(500) 2.Bag(1000) 3.Gift box(5000) 4.None
# location: 1.ktm 13%tax 2.bkt free 3.ltp free
# total
# total quantity
# taxable amount
# grand total

# ---------My method---------------------------

# print("==========Computer Bazar==========")
# print("1.Dell(20000) 2.Toshiba(30000) 3.Mac(50000)")
# product = int(input("Enter the no. you want to buy from above :"))
# quantity = int(input("Enter quantity of the said item :"))
# print("Delivery")
# print("1.Home(1000) 2.Pickup(Free)")
# deli = int(input("Choose the method of delivery :"))
# print("Packing")
# print("1.Plastic(500) 2.Bag(1000) 3.Gift Box(5000)  4.None")
# pack = int(input("Choose method of packing :"))
# print("Location")
# print("1.Ktm(with 13% tax) 2.Lalitpur(tax free) 3.Bhaktapur(tax free)")
# locate = int(input("Choose location of delivery :"))
# x = {
#     "products": [("Dell", 20000), ("Toshiba", 30000), ("Mac", 50000)],
#     "delivery": [("Home", 1000), ("Pickup", 0)],
#     "packing": [("Plastic", 500), ("Bag", 1000), ("Gift Box", 5000), ("None", 0)],
#     "location": [("Ktm", 13), ("Ltp", 0), ("Bkt", 0)],
# }
# total = x["products"][product - 1][1] * quantity
# print(f"Total amount is : {total}")
# taxable = total * 13 / 100
# if locate == 1:
#     print(f"Taxable amount is : {taxable}")
#
# grandtotal1 = total + x["delivery"][deli - 1][1] + x["packing"][pack - 1][1] + taxable
# grandtotal2 = total + x["delivery"][deli - 1][1] + x["packing"][pack - 1][1]
# if locate == 1:
#     print(f"The GrandTotal is : {grandtotal1}")
# else:
#     print(f"The GrandTotal is : {grandtotal2}")

# ---------------Sir Method---------------------

print("==========Computer Bazar===========")
print("1.Dell(Rs.20000) 2.Toshiba(Rs.30000) 3.Mac(Rs.50000)")

