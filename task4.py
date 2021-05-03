# --- закупки, оборудование
# заявки на оборудование принимаются когда накапливается 20 или больше частей всего
# или 10 одинаковых частей
# на 7 или больше одинаковых частей идёт скидка 15%
# нужно высчитать сумму деталей и выписать документ с полным перечнем и общей стоимостью на дату

item_1 = {'price': 150, 'brand': 'BELSHINA', 'type_of_detail': 'WHEELL'}
item_2 = {'price': 150, 'brand': 'BEL', 'type_of_detail': 'WHEELL'}
item_3 = {'price': 150, 'brand': 'TOSHIBA1', 'type_of_detail': 'CHAIN'}
item_4 = {'price': 150, 'brand': 'TOSHIBA2', 'type_of_detail': 'CHAIN'}
item_5 = {'price': 150, 'brand': 'TOSHIBA3', 'type_of_detail': 'CHAIN'}


# заявки на оборудование принимаются когда накапливается 20 или больше частей всего
pur_dict = {5: item_1, 9: item_2, 21: item_3, 6:item_4}
sum = 0
for key in pur_dict.keys():
    sum += key
# print("SUM", sum)

if sum >= 20:
    total_price = 0
    for key, items in pur_dict.items():
        total_price += items['price']
    # print(total_price)

# или 10 одинаковых частей
list = []
for key, items in pur_dict.items():
    list.append(key)
print(list)
count_of_equals = 0
for i in range(len(list)):
    print(i+1)
    print(pur_dict[list[i]])
    print(pur_dict[list[i+1]])

    if pur_dict[list[i]] == pur_dict[list[i+1]]:
        count_of_equals += 1

print(count_of_equals)




