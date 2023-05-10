
import math


a = int (input("Digite o valor de a: "))
b = int (input("Digite o valor de b: "))
c = int (input("Digite o valor de c: "))


delta = b**2 - 4 * a * c

print (delta)

if delta < 0:
    print("A raiz não pertence ao conjunto dos reais")

elif delta == 0:
    print ("existe apenas uma raiz real:")
    x = (-b) / (2 * a)
    print (x)

else:
    print("existem duas raízes reais")

    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print ("As raízes são:", x1, x2)

