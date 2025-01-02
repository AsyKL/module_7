from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'
class Shop:
    __file_name = 'products.txt'
    def  get_products(self):
        file = open(self.__file_name, 'r')
        s = file.read()
        file.close()
        return s
    def add(self, *products):
        list_prod = []
        s = ''
        for i in products:
            line = str(i).split(', ')
            if str(line[0]) in s:
                poz = s.find(line[0]) + len(line[0])
                s = s[poz+2:]
                poz2 = s.find(',')
                weight = float(s[:poz2]) + float(line[1])
                print(f'Продукт {line[0]} уже был в магазине, его общий вес теперь равен {weight}')
            else:
                list_prod.append(str(i))
            s = str(list_prod)
        file = open(self.__file_name, 'w')
        for i in list_prod:
            file.write('\n'+str(i))
        file.close()
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
s1.add(p1, p2, p3)
print(s1.get_products())