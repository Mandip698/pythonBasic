class Mobile:
    def __init__(self, company_name):
        print(company_name)

    def brand(self, brand):
        return f'Brand {brand}'

    def model(self, model):
        return f'Model {model}'

    def price(self, price):
        return f'Price {price}'


class Mi(Mobile):
    def __init__(self, company_name, logo):
        # Mobile.__init__(self, company_name)
        super().__init__(company_name)
        print(logo)

    def memory(self, memory):
        return f'Memory {memory}'


obj = Mi('Xiaomi', 'X')
print(obj.brand('Mi'))


# class Laptop:
#     def brand(self, brand):
#         return f'Brand {brand}'
#
#     def model(self, model):
#         return f'Model {model}'
#
#     def price(self, price):
#         return f'Price {price}'
#
#
# class Dell(Laptop):
#     def feature(self, feature):
#         return f'Feature {feature}'
#
#
# class Toshiba(Laptop):
#     def color(self, color):
#         return f'Color {color}'
#
#
# class Mac(Laptop):
#     pass
#
#
# obj = Toshiba()
# obj.model = 'GF63'
# print(obj.model)
