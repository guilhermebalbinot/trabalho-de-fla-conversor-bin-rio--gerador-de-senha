import random

resultado = ''
enquanto = 5
# ests inha de comando firifica se enquanto é menor que zero 
# e esecuta o codigo enquanto for verdade
while enquanto > 0:
    num_sorteado = random.randint(0, 9)
    # o inport.randint serve para sortear numerros aleatorios.
    resultado = str(resultado) + str(num_sorteado)
    # transforma  os numerros sorteados en estring, acrecentando 
    #o numerro sorteado ao resultado gerando a sequencia da senha.
    enquanto = enquanto - 1
 #este    

x = str(resultado)
print(resultado)
s = input("digitea senha:")
def verificação(s, x):
    # foi definido uma função para verificar a senha.
    r = []
    s = str(s)
    for i in range(len(s)):
     
        if s[i] in x:
            if s[i] == x[i]:
                r.append(1)
            else:
                r.append(0)
        else:
            r.append(-1)
    return r


#s = input("digitea senha:")
print(verificação(s, x))
    
