# --- закупки, оборудование
# заявки на оборудование принимаются когда накапливается 20 или больше частей всего
# или 10 одинаковых частей
# на 7 или больше одинаковых частей идёт скидка 15%
# нужно высчитать сумму деталей и выписать документ с полным перечнем и общей стоимостью на дату

item_1 = {'price': 20, 'brand': 'BELSHINA', 'type_of_detail': 'WHEELL'}
item_2 = {'price': 30, 'brand': 'WEST', 'type_of_detail': 'WHEELL'}
item_3 = {'price': 15, 'brand': 'TOSHIBA', 'type_of_detail': 'CHAIN'}
item_4 = {'price': 15, 'brand': 'TOSHIBA', 'type_of_detail': 'CHAIN'}
item_5 = {'price': 40, 'brand': 'MITUSU', 'type_of_detail': 'CHAIN'}

pur_dict = {5: item_1, 9: item_2, 1: item_3, 6: item_4, 8: item_5}

# заявки на оборудование принимаются когда накапливается 20 или больше частей всего
def gen_report(purchase):
    total_price = 0
    total_count = 0
    for key, items in pur_dict.items():
        total_price += items['price'] * key
        total_count += key
    print(f'Price of purchase: {total_price}; total count of details: {total_count}')


def get_number_of_equals (purchase):
    list_of_counts = []
    for key, items in pur_dict.items():
        list_of_counts.append(key)

    count_of_equals = 0
    for i in range(len(list_of_counts)-1):
        if pur_dict[list_of_counts[i]] == pur_dict[list_of_counts[i+1]]:
            count_of_equals = list_of_counts[i] + list_of_counts[i+1]
    return count_of_equals


def get_number_of_items(purchase):
    sum = 0
    for key in pur_dict.keys():
        sum += key
    return sum


count_of_items = get_number_of_items(pur_dict)
count_of_equals = get_number_of_equals(pur_dict)


if count_of_items >= 20 or count_of_equals == 10:
    gen_report(pur_dict)





















