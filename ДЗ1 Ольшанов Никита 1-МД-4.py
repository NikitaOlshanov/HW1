#1
name = 'Никита'
print(name)
#------------------------------------------------------------

#2
age = 18
print("Меня зовут", name, "мне", age, "лет")
#------------------------------------------------------------

#3
names = ("Никита " * 5)
print(names)
#------------------------------------------------------------

#4,5
name2 = input("Как звать тебя, хлопецъ?")
age2 = int(input("Сколько тебе лет, славянин?"))
age3=age2
if age2 in range(1,17):
    print("Ну привет,", name2, ". Че, даже ясельки не окончил еще, раз тебе", age2, "лет?")
else:
    print("Ну привет", name2,". Типа взрослвый уже, да, раз тебе", age2, "лет?")
#------------------------------------------------------------

#6
print(name[2:-1])
print(name[::-1])
print(name[3:])
print(name[:5])
#------------------------------------------------------------

#7
print(len(name))
sum=0
pr=1
while age2>0:
    d=age2%10
    sum=sum+pr
    pr=pr*d
    age2=age2//10
print("Сумма: ", sum)
print("Произведение: ", pr)
#------------------------------------------------------------

#8
print(name.lower())
print(name.upper())
print(name.title())
print(name.swapcase())
#------------------------------------------------------------

#9
if age3>0 and age3<=150:
    print("Ты кста человек")
else:
    print("нормальный возраст укажи, шутник..")
if ' ' in name2:
    print("Не надо выделываться и писать свое имя неправильно.")
else:
    print("Молодец, тебе невероятным чудом удалось написать свое имя правильно.")
#------------------------------------------------------------

#10
primer=int(input("Солько будет 2+2*2?"))
if primer==6:
    print("Красава, это правильный ответ!")
else:
    print("Ну как могло получиться ", primer,"-то? Учи математику, гений...")
# ------------------------------------------------------------