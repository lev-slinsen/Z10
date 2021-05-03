# --- байки, запчасти
# запчасти: рама, руль, цепь, педали, скорости
# каждой части должно быть минимум по 3 бренда с разными ценами (примерно 60-120 за целый байк)
# если деталь одного бренда заканчивается, её надо до-заказать.



import random

class Parts():
    def __init__(self, a, b, c, d, f):
        self.frame = a
        self.handlebar = b
        self.chain = c
        self.pedals = d
        self.shifters = f

class_1 = Parts(30, 7, 5, 12, 18)
k = class_1.__dict__

class Brand ():
    def __init__(self , a, b, c):
        self.brand_1 = a
        self.brand_2 = b
        self.brand_3 = c
      
class_2 = Brand(1, 1.3, 0.8)
k_1 = class_2.__dict__

print ('brand_1', 'brand_2', 'brand_3')
a=input()
k_2=k_1[a]
print(k_2)
prise={}
for i, j in k.items():
    prise[i]=j*k_2
print (prise)

for i, j in prise.items():
    print (i, j)
total=0
for i in prise.values():
    total+=i
print('Итого:', total)




    #def __init__ (self, b, p):
        #self.brend = b
        #self.prise_brend = p
#class Detail():
    #def __init__ (self, detail, price):
        #self.detail=detail
        #self.price_detail=price_detail

#brend=['standard', 'base', 'lux']
#prise=[1.2, 2, 3]
#dict_1=Brend(brend, prise).__dict__

#print(dict_1)
#print("")

#class_2 = class_1.__dict__
#brand_1 = {}
#brand_2 = {}
#for i, j in class_2.items():
    #brand_1[i]=j*1.2
    
#print(brand_1)




#class  Brands():
    #def __init__(self, a, b):
       # self.self.detail = a
        #self.price_detail = b
        #return (a,b)

#brand = Brands(a, b)
#price = [(1.2), (1,4), (1,6)]
#dict_1 = Brands(brand, price).__dict__
#print (dict_1)