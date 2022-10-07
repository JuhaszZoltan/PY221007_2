# szöveges (string) 'karakterlánc'
a:str = 'szöveg'

print('kutya' + 'ház') # OP: 'kutyaház'
print(3 * 'cica ') # OP: 'cica cica cica '

# egész (integer) 'decimális egész szám'
b:int = 1986
# lebegőpontos (floating point number) ""decimális valós szám""
c:float = 3.1415

print(20 * 3)
print(20 + 3)
print(30 - 3)
print(10 / 3) # 'sima' osztás OP: 3.3333...
print(10 // 3) # 'div' azaz 'egész osztáy' OP: 3
print(10 % 3) # 'mod' azaz 'maradékképzés' OP: 1

print(2 ** 10) # hatványozás OP: 1024
print(16 ** .5) # n sqrt(x) == x^(1/n)

# float és int 'típuskompatibilis' egymással operátorok tekintetében
print(10 // 1.5)

# logikai (Boolean) 
d:bool = True # False

print(True and False) # logikai és OP: False
print(True or False) # logikai vagy  OP: True
print(not True) # logikai tagadás OP: False

# 'összehasonlító operátorok'
print(10 < 3) # OP: False
print(10 > 3)
print(10 <= 3)
print(10 >= 3)

print(10 == 3)
print(10 != 3)

#              T
#         F          T
print(10 <= 3 or 10 != 3) # OP: True

# 'tartalmazza' halmazművelet
# érték in <kollekció> -> logikai
print(12 in [5, 8, 31, 45, 12, 5, 5, 11]) # OP: True