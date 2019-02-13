print ("mencari bilangan terbesar dari 3 bilangan")

a = int(input("masukan bilangan pertama :"))
b = int(input("masukan bilangan kedua :"))
c = int(input("masukan bilangan ketiga :"))

if a > b and a > c :
        print ("\nBilangan terbesar nya adalah :%s " %a)
elif b > a and b > c :
        print ("\nBilangan terbesar nya adalah :%s " %b)
else :
        print ("\nBilangan terbesar nya adalah :%s " %c)