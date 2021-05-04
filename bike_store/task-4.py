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

pur_dict = {5: item_1, 9: item_2, 1: item_3, 6: item_4, 8: item_5}

def gen_report():
    total_price = 0
    total_count = 0
    print("--------------------------------------------------")
    for key, items in pur_dict.items():
        total_price += items.price * key
        total_count += key
        print(f'Brand: {items.brand}, detail: {items.type_of_detail}, price: {items.price}, count: {key} ')
    print("--------------------------------------------------")
    print(f'Purchase amount: {total_price}; total count of details: {total_count}')


def get_number_of_equals ():
    list_of_counts = []
    for key, items in pur_dict.items():
        list_of_counts.append(key)

    count_of_equals = 0
    for i in range(len(list_of_counts)-1):
        for j in range(len(list_of_counts)-1):
            if pur_dict[list_of_counts[i]].__eq__(pur_dict[list_of_counts[j]]) and i != j:
                count_of_equals = list_of_counts[i] + list_of_counts[j]
    return count_of_equals


def get_number_of_items():
    sum = 0
    for key in pur_dict.keys():
        sum += key
    return sum


count_of_items = get_number_of_items()
count_of_equals = get_number_of_equals()


if count_of_items >= 20 or count_of_equals == 10:
    gen_report()