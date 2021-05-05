# --- закупки, оборудование
# заявки на оборудование принимаются когда накапливается 20 или больше частей всего
# или 10 одинаковых частей
# на 7 или больше одинаковых частей идёт скидка 15%
# нужно высчитать сумму деталей и выписать документ с полным перечнем и общей стоимостью на дату

class Item:
    def __init__(self, brand, type_of_detail, price):
        self.brand = brand
        self.type_of_detail = type_of_detail
        self.price = price

    def __eq__(self, other):
        if not isinstance(other, Item):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.brand == other.brand and self.type_of_detail == other.type_of_detail and self.price == other.price

    def __str__(self):
        print(f'Brand: {self.brand}, detail: {self.type_of_detail}, price: {self.price} ')


item_1 = Item('TOSHIBA', 'CHAIN', 15)
item_2 = Item('WEST', 'WHEELL', 30)
item_3 = Item('BELSHINA', 'WHEELL', 20)
item_4 = Item('TOSHIBA', 'CHAIN', 15)
item_5 = Item('MITUSU', 'CHAIN', 40)
item_6 = Item('TOSHIBA', 'CHAIN', 15)

pur_dict = {5: item_1, 9: item_2, 1: item_3, 6: item_4, 8: item_5, 2: item_6}


def gen_report():
    list_of_counts = []
    for key, items in pur_dict.items():
        list_of_counts.append(key)

    total = 0
    print("--------------------------------------------------")
    for i in range(len(list_of_counts)):
        count_of_equals = 0

        for j in range(len(list_of_counts)):
            if pur_dict[list_of_counts[i]].__eq__(pur_dict[list_of_counts[j]]) and i != j:
                count_of_equals = list_of_counts[i] + list_of_counts[j]
        if count_of_equals >= 7:
            total = total + pur_dict[list_of_counts[i]].price * list_of_counts[i] * 0.85
        else:
            total = total + pur_dict[list_of_counts[i]].price * list_of_counts[i]
        item = pur_dict[list_of_counts[i]]
        print(f'Brand: {item.brand}, detail: {item.type_of_detail}, price: {item.price}, count: {list_of_counts[i]} ')
    print("--------------------------------------------------")
    print(f'Purchase amount: {total}; total count of details: {sum(list_of_counts)}')


def get_max_of_unique_items():
    unique_items = []
    for key, items in pur_dict.items():
        if pur_dict[key] not in (unique_items):
            unique_items.append(items)

    counts = []
    for unique_item in unique_items:
        count = 0
        for key, items in pur_dict.items():
            if unique_item.__eq__(items):
                count = count+key
        counts.append(count)
    return 10 in counts

def get_number_of_items():
    sum = 0
    for key in pur_dict.keys():
        sum += key
    return sum


count_of_items = get_number_of_items()
number_of_equals_is_10 = get_max_of_unique_items()
print(number_of_equals_is_10)

if count_of_items >= 20 or number_of_equals_is_10:
    gen_report()





