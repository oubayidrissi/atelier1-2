#oubay el idrissi
#atelier 1:

#ex1:
#fonction pour calculer le factoriel
def fact(x):      
    if x==1:
        return 1
    else:
        return x*fact(x-1)
s=0
n= int (input("entrer un nombre:"))
for i in range(1,n+1):       
    s=s+fact(i)//i
#pour afficher tous les element précédente de la somme               
    print("la somme des séries est:",s)       

#ex2:

# fonction pour convertir le nombre décimal en nombre binaire
def binaire(x):
    if x>1:
#pour afficher le reste de la division sur 2
        binaire(x//2)  
    print(x%2,end=" ") 

n=int(input("entrer votre nombre:"))
binaire(n)

#ex3:

#un programme peut calculer la somme des nombres de 1 à n
def somme(x):
    if x==1:    
        return 1 
    else:
        return x+somme(x-1) 

n= int(input("entrer votre nombre:"))
print("la somme est:",somme(n))

#ex4:

#la série Fibonacci
def fibonacci(x):
#si x=1 ou x=0
    if x<=1:        
        return x
    else:
        return fibonacci(x-1)+fibonacci(x-2)
n= int(input("entrer votre nombre:"))
#pour entrer un nombre positif
if n<=0:                            
    print("entrer un nombre positive:")
else:
    for i in range(n):
    #pour afficher tous les termes de serie fibonacci
        print(fibonacci(i))   

#ex5:

def chiff(x):
    if x//10 ==0:
        return 1
    else:
        return 1 + chiff(x//10)

n=int(input("entrer un nombre:"))
print("le nombre des chiffres sont:",chiff(n))

#ex6:

def bulle(l):
    n=len(l)
    #pour traverser tous les éléments du tableau
    for i in range(n):
        for j in range(n-i-1):
    #pour changer les places
            if l[j]>l[j+1]:
                a=l[j]
                l[j]=l[j+1]
                l[j+1]=a
#un exemple
l=[98, 22, 1, 89, 4, 75, 0, 2]
print("la liste principale",l)
bulle(l)
print("la liste tri a bulle",l)

#ex7:

def inverse(l):
    n=len(l)
    t=[]
    for i in range(n):
#ajouter la dernier chaine de caractères.
        t.append(l[-i]) 
#inverser la place            
        t[i]=l[-(i+1)]                 
        print(t[i],end='')
text=input("entrer le mot:")
inverse(text)

#ex8:

#une fonction peut trouver la frequence d'un caractère
def count(str,c):
    return str.count(c)
st=input("entrer le mot:")
c=input("entrer votre caractère:")
print(count(st,c))

#ex9:

def trouve(l,e):
#pour circuler dans la liste
    for i in range(len(l)):
        for j in range(len(m[i])):
            if m[i][j] == e:
                return (i,j)
#un exemple d'une matrice
m=[[1,2],[5,6]]
e=int(input("entrer l element:"))
print(trouve(m,e))

#atelier 2:

#ex1:

#Créer une liste en choisissant des éléments d'index impair 
# dans la première liste et des éléments d'index pair dans la seconde. 
def fonction(l1,l2):
#creer un liste vide
    l3=[]
    for i in l1:
        if l1.index(i)%2 != 0:
            l3.append(i)
    for i in l2:
        if l2.index(i)%2 == 0: 
            l3.append(i)
    print(l3)
#exemple des liste
a=[3, 6, 9, 12, 15, 18, 21]
b=[4, 8, 12, 16, 20, 24, 28]
fonction(a,b)

#ex2:

#Deviser la liste en 3 morceaux égaux et inverser chaque morceau
a=[11, 45, 8, 23, 14, 12, 78, 45, 89]
x=len(a)//3
liste1=a[:x]
liste2=a[x:2*x]
liste3=a[2*x:]
# on peut utiliser liste.sort(reverse=true) mais pour cette exemple 
# on peut que chamger le premier element averc le dernier
print(liste1[::-1],liste2[::-1],liste3[::-1])  

#ex3

#Écrire un programme pour itérer une liste donnée et compter l'occurrence de chaque 
# élément etcréer un dictionnaire pour montrer le nombre de chaque élément.

l=[11, 45, 8, 11, 23, 45, 23, 45, 89,89]
n=len(l)
d={}
for i in l:
    if l.count(i)==1:
        d.update({i:l.count(i)})
    #pour eviter la repition
        del(i) 
    else:
        d.update({i:l.count(i)})
print(d)

#ex4:

x={23, 42, 65, 57, 78, 83, 29}
y={57, 83, 29, 67, 73, 43, 48}
#pour trouver l'intersection.
z= x.intersection(y)  
#supprimez ces éléments.
a=x.difference(z)
print("Intersection:",z)
print("Set 1 après suppression :",a)

#ex5:

l1=[47, 64, 69, 37, 76, 83, 95, 97]
d={'Yassine':47, 'Imane':69, 'Mohammed':76, 'Abir':97}
l2=[]
for i in l1:
#chercher un élément dans le dictionaire si il existe  
    for j in d.values():
        if i==j:
          l2.append(j)
print(l2)
