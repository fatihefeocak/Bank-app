# bank

hesapa = {
    'ad' : 'Fatih',
    'hesapno' : '12345',
    'bakiye' : 3000,
    'ekhesap' : 2000,
}

def paracek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if(hesap['bakiye']>=miktar):
        print("Paranızı alabilirsiniz.")
        hesap['bakiye'] -= miktar
    else:
        toplam = hesap['bakiye'] + hesap['ekhesap']
        if (toplam >= miktar):
            ekparakullanimi = input("Ek para kullanmak ister misiniz : (e/h)")
            if ekparakullanimi == 'e':
                ekhesapmiktarkullanimi = miktar-hesap['bakiye']
                hesap['bakiye']=0
                hesap['ekhesap']-=ekhesapmiktarkullanimi
                print("Paranizi alabilirsiniz.")
            else:
                print(f"{hesap['hesapno']} nolu hesabınızda bakiyeniz {hesap['bakiye']}'dir.")
        else:
            print("Bakiye yetersiz.")
c=int(input("Ne kadar para çekmek istersiniz:"))

def bakiyesorgula(hesap):
    print(f"{hesap['hesapno']} nolu hesapta {hesap['bakiye']} tl vardır. Ekte ise {hesap['ekhesap']} tl vardır.")

paracek(hesapa,c)
bakiyesorgula(hesapa)
print("************")