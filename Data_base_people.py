from random import randint
#n = int(input('Напишите сколько будет субъектов/Write down how many subjects there will be - '))
#for i in range(n):
s = []
d = input("Фамилия/Surname - " )
j = input("Имя/Name - " )
k = input("Отчество/Middle name - " )
s.insert(0, d)
s.insert(1, j)
s.insert(2, k)
J = randint(1, 9999)
BB = 'Id пользователя/user =', J
s.insert(4, J)
result = s
with open('Data_base_' + d + '.txt', 'w') as F:
    F.write(str(result))
    F.write("\n")
    F.write(str(BB))
    F.close()
