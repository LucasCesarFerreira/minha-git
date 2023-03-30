#print("Teste de criação de matriz")
#A=[]

#for i in range (5):
 #   A.append([0]*5)

#for i in range(5):
 #   for j in range(5):
  #      A[i][j]=input("letra")

#for i in range(5):
#   print(A[i])

lista=["cachorros","doguinhos","sao","fofos"]
estringue=str(lista)
estringue=estringue.replace("[","")
estringue=estringue.replace("]","")
estringue=estringue.replace(",","")
estringue=estringue.replace("'","")
print(estringue)