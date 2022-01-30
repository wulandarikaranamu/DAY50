print("\n"+"program mengubah meter ke centimeter dan kilometer"+"\n"+50*"=")

def centimeter():
    bilangan = int(input("masukkan bilangan (m):"))
    centimeter = bilangan*100
    print("cm",centimeter)
def kilometer():
    bilangan = int(input("masukkan bilangan (m) :"))
    kilometer = bilangan/1000
    print("km",kilometer)
def menu():
    print("pilih menu dibawah ini")
    print("[1]meter ke centimeter")
    print("[2]meter ke kilometer")
    choose = int(input("pilih menu :"))
    if choose == 1:
        centimeter()
    elif choose == 2:
        kilometer()
    else:
        print("menu yang anda masukkan tidak ada")

menu()
