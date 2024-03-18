#print(10+5)
#print(10-8)
#print("G'rubetda garib shodmon bo'lmas emish \nEl anga shafiqu mehribon bo'lmas emish") #\n keyingi qatorga tushuradi
#print(2**8)
#print("beshning kvadrati", 5**2 , "ga teng") # ** kvadrat
#ism = 'Yusuf'
#yosh = 24
#print(ism)
#print(yosh)
#ism = "Ali"
#print("Mening ismim " + ism)
#familiya = "Rajabov"
#ism_familiya = f"{ism} {familiya}"
#print(ism.lower())
# meva = "      olma     "
# print("Men " + meva + "ni yaxshi ko'raman!")
# print("Men " + meva.lstrip()+ "ni yaxshi ko'raman!") # chap tomondagi boshliqni olib tashlaydi
# print("Men " + meva.rstrip()+ "ni yaxshi ko'raman!") # ong tomondagi boshliqni olib tashlaydi
# print("Men " + meva.strip()+ "ni yaxshi ko'raman!") # chap va ong tomondagi boshliqni olib tashlaydi
# ism= input("Ismingiz nima? ") # foydalanuvchidan  sorash
# print("Assalomu aleykum, "+ ism)
#ism= input("Ismingiz nima? \n>>>")
#print("Assalomu aleykum, "+ ism.title())
#Sonlar!!!
#x,y,z=10.5,25,-98
#c=x*y
#print(c)
#ism = "Jobir"
#yosh = 36
#yosh = str(yosh) #yoshini string tipiga otkazish
#xabar= ism + " " +str( yosh) + " yoshda"
#print(xabar)
#t_yil= int(input("Tug'ilgan yilingizni kiriting\n>>"))
#yosh=2023 - t_yil
#print("Siz",yosh,"yoshda ekansiz!")
# mevalar = ['olma','anjir','shaftoli','arik']
# narxlar = [12000,14500,34500,33300,12100]
# narxlar[3]= narxlar[3]+700 #narxni yangilash
# print(narxlar)
#sonlar = ['bir','ikki',3,4]
#ismlar = []
#print(narxlar[0]+ narxlar[4])
#mevalar[3]='anor'
# print(mevalar[1].title())
# mevalar.append('banan') #ro'yxat oxiriga qoshadi
# mevalar.insert(1,'malina') # indexda korsatilgan joyga qoshadi.
# print(mevalar)
# cars=[]
# cars.append('malibu')
# cars.append('lasetti')
# cars.append('tico')
# cars.append('damas')
# del cars[2]
# cars.insert(0,'naxia 3') #o indexsga qoyadi
# cars.remove('damas') #royxatdan olib tashlaydi , agar 2 ta bolsa 1 sini olib tashlaydi
# print(cars)
# hayvonlar=['it','mushuk','ot','sigir','buqa','mushuk']
# hayvonlar.remove('mushuk') #
# print(hayvonlar)
#bozorlik=['yog\'','piyoz','un','banan','go\'sht']
# maxsulot=bozorlik.pop(2) #korsatilgan indexdagini royxatdan sugurib oladi
#print(bozorlik[0:2]) #korsatilgan oraliqni sugurib olish oxirgi yozilgan index kirmaydi
# print("Men bozordan " + maxsulot + " oldim")
# print("Olmagan maxsulotlarim ", bozorlik)
#cars=['audi','mersides','bmw','chevrolet','byd','honda','nissan']
# cars.reverse() #royxatni tekkari joylashtirish alifbo emas!!!
# print(cars)
# cars.sort() # royxatni alifbo boyicha joylashtirish, katta harflar kichik harflardan oldin joylashadi
# cars.sort(reverse=True) # teskari tartibda joylashtirish
# print(cars)
# print(sorted(cars)) # tartiblangan royxatni chiqarish asl royxat ozgarmaydi
# print(sorted(cars,reverse=True)) # teskari tartibda
# sonlar = [1,58,4,36,-8,56,-58,56]
# uzunlik = len(sonlar)
# print(len(sonlar)) #uzunligini aniqlash
# sonlar.sort()
#print(sonlar)
# print(sorted(sonlar))
# print(sorted(sonlar,reverse=True))
# harflar=[]
# harflar=list(range(0,11)) #malum oraliqdagi sonlarni chiqaradi bu yerda 0 dan 10 gacha 11 olmaydi!!
# print(harflar)
# toq_sonlar=list(range(1, 20, 2)) # oxiridagisi sakrashi, juft bolsa 3 yoki royxatni 2 dan boshla!!!
# print(toq_sonlar)
# max_qiymat= max(toq_sonlar) # max qiymatni listdan chiqarish
# min_qiymat= min(toq_sonlar) # min qiymatni listdan chiqarish
# summa= sum(toq_sonlar) # toq sonlarning yigindisi
# print(summa)
# my_cars=cars[:] # royxatdan nusxa olish
# print(my_cars)
# toys=('bus','car','bear','snake','dino','lizard') # ozgarmas royxat [] qavs orniga () ishlatiladi!!
# print(toys[1:4])
# toys = list(toys) # tuplle ni odiiy listga aylantirish
# toys.append('teddy')
# toys=tuple(toys) #oddiy listni tupple aylantirish
# print(toys)
# print (type(toys)) # tipini aniqlash
#SIKL SIKL SIKL SIKL SIKL
# mehmonlar = ['ali','vali','hasan','husan','olim']
# for mehmon in mehmonlar: #SIKL mehmon deb yozilishi shart emas
#   print('Salom',mehmon)
#   print(f'hurmatli {mehmon} biz sizni 21 mart navroz bayramida kutamiz') # fstream funksiyasi
# sonlar = list(range(1,11)) # 1 dan 10 gacha bolgan sonlar royxatining kvadratini hisoblaydi
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")
# sonlar = list(range(11))
# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son**2) # sonlarning kvadratidan iborat royxat yaratadi
# print(sonlar_kvadrati)
# dostlar = [] #bosh royxat
# print('5 ta eng yaqin dostingiz kim? ')
# for n in range(1,6): # n bu yerda 0 dan 4 gacha qiymat oladi
#      dostlar.append(input(f'{n} - yaqin dostingizni ismini kiriting:' )) # append yordamida dostlarga ism qoshamiz. input kiritish funksiyasi.
# print(dostlar)
# TARMOQLANISH
# avtolar = [ 'bmw','volvo','nissan','audi','gm','honda']
# for avto in avtolar:
#     # print(avto.title())
#     if avto == 'bmw': $shart operatori qoyildi
#         print(avto.upper()) # agara shart bajarilsa uni hamma harfini katta qilindi
#     else:
#          print(avto.title()) # shart bararilmasa faqat 1 harf katta boldi
# ism='Ali'
# ism.lower()== 'ali'  # bu joyda ismlarni hammasini kichik harfga ozgartirib solishtirdik.
# ism= input('ismingizni kiriting\n >>>')
# if ism.lower() != 'ali' : #kiritilgan ismni kichkina qilib ali bilan solishtirdik
#     print(f'Uzr,{ism.title()} biz Alini kutyapmiz!')  #ism.title qilib uning yozgan ismini chiqardik
# else: # agar ali bolsa
#     print('Salom Ali') # u bilan salomlashdik
# yosh = int (input('Yoshingiz nechada?\n >>>'))
# if yosh>=18:
#     print('Xush kelibsiz')
# else:
#     print("kirish mumkin emas!")
# login = input("Yangi login kiriting: ")
# if len(login)<=5 :
#     print("login 5 harfdan kam bolmasin")
# yil= int(input("Tugilgan yilingizni kiriting:\n ")) # foydalanuvchidan yili soraldi
# if 2023-yil<18: # yoshini aniqlab 18 dan kattami yoqmi tekshirildi.
#     print(f'Yoshingiz {2023-yil} da ekan.')
#     print('Kirish mumkin emas')
# else: print('Xush kelibsiz')

# x,y=26,34
# print('x>y') if x>y else print('x<y')
   #######                             ###############################
# A, B = map(int, input().split()) # bitta qatorda kiritish.
# x = pow(2,(2**A),B) # B qoldiqli boslish.
# print(x)
# sonlar=[]
# a = int(input('Nechagacha bo\'lgan tub sonlar kerak: '))
# Fibonacci series using recursion
# n= int(input())
# a=(((n+3)*n-9*(n%2))*n+72)//144
# print(a)
# a=int(input())
#   if(a%2==0)
#       print(a/2)
#    else:
#      print('-1')
# def fibonacci(n):
#     # Taking 1st two fibonacci numbers as 0 and 1
#     f = [0, 1]
#
#     for i in range(2, n + 1):
#         f.append(f[i - 1] + f[i - 2])
#     return f[n]
# a=int(input())
# j=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229]
# print(fibonacci(a)+j[a-1])
# x= int(input())
# f=pow(x,5)+8*pow(x,4)-5*pow(x,3)+3*pow(x,2)+x-12
# print(f)
###################                    ###########################################
# kun=input("Bugun qaysi kun? ")
# harorat=float(input("Havo qanday?"))
# if (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat>=30:
#     print("Chomilishga ketdik")
# elif (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat<30:
#  print("Uyda dam olamiz")
### BOOLEAN ### BOOLEAN ### BOOLEAN ### BOOLEAN ### BOOLEAN ### BOOLEAN ### BOOLEAN ### BOOLEAN
# narx=15000
# non=True
# choy=1
# salat=False
# kampot=True
# assorti=0
# if non:
#     print("Mijoz non oldi")
#     narx=narx+5000
# if choy:
#     print("Mijoz choy oldi")
#     narx=narx+5000
# if salat:
#     print("Mijoz salat oldi")
#     narx=narx+5000
# if kampot:
#     print("Mijoz kampot oldi")
#     narx=narx+5000
# if assorti:
#     print("Mijoz assorti oldi")
#     narx=narx+5000
# print(f"Mijozning narxi {narx} som boldi ")
######### IN OPERATORI
# menyu = ['osh','somsa','manti','kabob','baliq']
# # print('manti' in menyu)  # in royxat ichida bor yoki yoqligini tekshiradi
# ovqat = input("Yeyishga nima hoxlaysiz?>>> ")
# if ovqat.lower() in menyu :
#  print("Zakaz olindi")
# else:
#  print("Kechirasiz boshqasini tanlang")
 ##print('tuxum' not in menyu) # menyuda tuxum yoqmi deb sorab True qiymat qabul qildim.
# menyu = ['osh','somsa','manti','kabob','baliq']
# buyurtmalar = ['osh','shashlik', 'kabob']
# if buyurtmalar: # royxatda taom bor yoki yoqligini tekshiradi
#  for taom in buyurtmalar:
#   if taom in menyu:
#    print(f"menyuda {taom} bor")
#   else:
#    print(f"Kechirasiz {taom} menyuda yoq")
# else: #agar royxat bosh bolsa
#     print("Savatchangiz bosh")
# sonlar= [1,2,4,6,8,3,5]
# print(sum(sonlar[3:]))
# son=list(range(0,10))
# print(son)




