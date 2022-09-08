# quiz determinar si un numero es capicua

print("-----------------------------------------------------")
print("--- determinar si un numero de 5 cifras es capicua---")
print("-----------------------------------------------------")

# inpunt

n= int(input("ingrese un numero de 5 cifras: "))
#procesing 
if n>9999:
    if print("si es un numero de 5 cifras"):
        m=n%1
        N2=(n%10)%1
        N301=n%100
        N3=(N301%10)%1
        N401=n%1000
        N402=(N401%100)%10
        N4=(N402)%1
        N501=(n%10000)%1000
        N502=(N501%100)%10
        N5=N502%1
        if m == N5:
            if N2 == N5:
                print("si es un numero capicua")
        else:
            print("no es un numero capicua")
    else:
        print("no es un numero capicua")
else:
    print("no es un numero de 5 cifras")

