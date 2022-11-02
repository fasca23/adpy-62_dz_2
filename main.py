import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ

# правим регулярным выражением все номера    
pattern = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
            r'([-]*)(\d{3})(\s*)([-]*)(\d{2})(\s*)([-]*)' \
            r'(\d{2})(\s*)(\(*)(доб)*([-]*)(\s*)(\d+)*(\)*)'
sub = r'+7(\4)\8-\11-\14\15\17\18\19\20'
list_result = []
for i in contacts_list:
    i_as_string = ','.join(i)
    formatted_i = re.sub(pattern, sub, i_as_string)
    i_as_list = formatted_i.split(',')
    list_result.append(i_as_list)

# разбиваем ФИО по колонкам регулярным выражением, перенося запятые если их нет
pattern2 = r'^(\w+)(\s*)([,]?)(\w+)' \
            r'(\s*)([,]?)(\w*)([,]?)([,]?)([,]?)'
sub2 = r'\1\3\10\4\6\9\7\8'
list_result2 = []
for j in list_result:
    j_as_string = ','.join(j)
    formatted_card = re.sub(pattern2, sub2, j_as_string)
    j_as_list = formatted_card.split(',')
    list_result2.append(j_as_list)
    
# сравниваем одинаковые строчки (по Ф и И) друг с другом по наличию или отсутствию значений и перезаписываем эти значения при отсутствии + чистим от повторов
for i in list_result2:
    for j in list_result2:
        if i[0] == j[0] and i[1] == j[1] and i != j:
            if i[2] == "":
                i[2] = j[2]
            if i[3] == "":
                i[3] = j[3]
            if i[4] == "":
                i[4] = j[4]
            if i[5] == "":
                i[5] = j[5]
            if i[6] == "":
                i[6] = j[6]
list_result3 = []
for i in list_result2:
    if i not in list_result3:
        list_result3.append(i)

# # TODO 2: сохраните получившиеся данные в другой файл
# # код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
  datawriter.writerows(list_result3)