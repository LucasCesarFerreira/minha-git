print("*"*6,"Soma","*"*6)
resp='y'
x = int(input("entre com o número\t"))
while resp=='y':
    y=int(input("entre com o proximo número\t"))
    x+=y
    resp=input("deseja entrar com mais um numero na soma? y/n\t")

