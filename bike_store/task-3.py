# --- байки, запчасти
# запчасти: рама, руль, цепь, педали, скорости
# каждой части должно быть минимум по 3 бренда с разными ценами (примерно 60-120 за целый байк)
# если деталь одного бренда заканчивается, её надо до-заказать.
'''
бренды: объекты
части: объекты
заказать надо: объекты
'''


class Parts():
    def __init__(self, a, b, c, d, f):
        self.frame = a
        self.handlebar = b
        self.chain = c
        self.pedals = d
        self.shifters = f


class_1 = Parts(30, 7, 5, 12, 18)
k = class_1.__dict__


class Brand():
    def __init__(self, a, b, c):
        self.brand_1 = a
        self.brand_2 = b
        self.brand_3 = c


# доделать логику создания товара, который имеет атрибуты детали и бренда,
# высчитать стоимость детали, вывести её на экран (вывести несколько на экран)


class_2 = Brand(1, 1.3, 0.8)
k_1 = class_2.__dict__

print('brand_1', 'brand_2', 'brand_3')
a = input()
k_2 = k_1[a]
print(k_2)
prise = {}
for i, j in k.items():
    prise[i] = j * k_2
print(prise)

for i, j in prise.items():
    print(i, j)
total = 0
for i in prise.values():
    total += i
print('Итого:', total)
