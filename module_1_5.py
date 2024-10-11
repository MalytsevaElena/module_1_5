immutable_var = (1, 2, 3, 'abc', 'd') # неизменяемый кортеж
print("immutable_var: ",immutable_var)
muttble_list = [1, 2, 3, 'abc', 'd']  # изменяемый список
muttble_list[2]=4                     # изменение 1 списка, замена по индексу
muttble_list.append('new')            # изменение 2 списка, добавление в конце 1 эл.
muttble_list.extend("567")            # изменение 3, добавление c разложением на эл.
muttble_list.remove("abc")            # изменение списка 4, удаление элемента
print("muttble_list: ",muttble_list)