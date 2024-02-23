import random
import cursos

cicle = "not"
x = random.randint(100, 500)
lista = []

if cicle == "sim":
    for i in range(x):
        y = random.randint(0,x-1)
        z = random.randint(0,x-1)
        if z!=y:
            lista.append([y,z])


else:
    near = [[]]*x
    for i in range(x):
        y = random.randint(0,x-1)
        z = random.randint(0,x-1)
        if z!=y and [y,z] not in lista and [z,y] not in lista and z not in near[y] and y not in near[z]:
            lista.append([y,z])
            near[y].append(z)
            near[z].append(y)




final = cursos.canFinish(x, lista)

if final == True:
    print("Ok")
else:
    print("Not Ok")


print(lista)