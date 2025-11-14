


def decorateur01(func):
    def wrapper(*args, **kwargs):
        print(f"Exécution de {func.__name__} avec les arguments {args} et {kwargs}")
        result = func(*args, **kwargs)
        print(f"Résultat : {result}")
        return result
    return wrapper

@decorateur01
def addition(a:any , b:any)-> any:
    return a+b | None



class Utilisateur:
    def __init__(self, num, email , age = None):
        self.num = num
        self.email = email  # Peut être None si non fourni
        self.age =  age 

    def affichage(self,p):
        print (self.num,"---------", p.num)
        print (p.num,"---------", p.num)
    
    def compare(self,p) -> None:
        if self.num > p.num:
            print ("objet de base plus grand")
        elif self.num < p.num : 
            print("nouveau object plus grand",p.num)
        else: 
            print("le meme nombre")


    



a = Utilisateur(2,5)

b = Utilisateur(2,5)

a.compare(a)



a.affichage(b)