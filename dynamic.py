from datetime import datetime
# Algoritmo basado de pseudocódigo https://iq.opengenus.org/word-break-problem-dp/
class WordBreak:   
 
    def wrapper (self, string, dictionary): 
        memorization = {}
        array = self.helper(string, dictionary, memorization)
        print(array)
        return len(array)
	
	# s es el tamaño del string de entrada
    def helper(self, s, dictionary, memorization):
        if s in memorization.keys():  #Se utiliza  memorización para limitar el proceso de solapamiento          
            return memorization.get(s)		
        res = []
        for word in dictionary :
            if s.startswith(word): 
                following = s[len(word):]
                if  len(following) == 0:
                    res.append(word)
                else :
                    for sub in self.helper(following, dictionary, memorization): 
                        res.append(word + " " + sub)
        memorization[s]=res #Se guardan los resultados parciales
        return res
 
wordbreak = WordBreak()
dictionary = ["la", "clase", "de", "analisis", "y", "algoritmos", "es", "lo", "maximo"];    	

#100 words
large_dictionary = [
"solo",
"si",
"contrario",
"una",
"uno",
"comer",
"dormir",
"solitario",
"decidir",
"el",
"la",
"soldado",
"que",
"no",
"se",
"si",
"un",
"una",
"para",
"por",
"mi",
"tu",
"y",
"con",
"unos",
"unas",
"dos",
"se",
"ha",
"reir",
"quiere",
"quiero",
"como",
"cual",
"donde",
"estar",
"estoy",
"mis",
"tus",
"puente",
"diente",
"camino",
"compu",
"reloj",
"saber",
"cuanto",
"numeros",
"salsa",
"angel",
"martir",
"dulce",
"andres",
"solo",
"dime",
"carretera",
"contra",
"in",
"joder",
"kilo",
"nunca",
"luis",
"fregar",
"jabali",
"teclado",
"musica",
"dosis",
"armado",
"caballero",
"dama",
"almeja",
"santo",
"santa",
"hace",
"gringo",
"cobarde",
"hombre",
"mujer",
"musico",
"bella",
"muerte",
"dormitorio",
"cabeza",
"guardar",
"salvar",
"tarjeta",
"lapiz",
"telefono",
"ordenador",
"turing",
"caja",
"negra",
"recurso",
"punta",
"inutil",
"camello",
"camisa",
"papel",
"dermis",
"dante",
"comerdor",
"salir",
"tucan"]

#50 words
medium_dictionary = [
"solo",
"si",
"contrario",
"una",
"uno",
"comer",
"dormir",
"solitario",
"decidir",
"el",
"la",
"soldado",
"que",
"no",
"se",
"si",
"un",
"una",
"para",
"por",
"mi",
"tu",
"y",
"con",
"unos",
"unas",
"dos",
"se",
"ha",
"reir",
"quiere",
"quiero",
"como",
"cual",
"donde",
"estar",
"estoy",
"mis",
"tus",
"puente",
"diente",
"camino",
"compu",
"reloj",
"saber",
"cuanto",
"numeros",
"salsa",
"angel",
"martir",
"dulce",
"andres",
"solo",
"dime"]

#10 words
small_dictionary = [
"solo",
"si",
"contrario",
"una",
"uno",
"comer",
"dormir",
"solitario",
"decidir",
"el"]

s = "eldecidirsolitariodormircomerunounacontrariosisolo"; 

start = datetime.now()
print("small dictionary ===>", wordbreak.wrapper(s, small_dictionary)); 
end = datetime.now()
print("small dictionary time ===>", str(end-start)[5:]); 
start2 = datetime.now()
print("medium dictionary ===>", wordbreak.wrapper(s, medium_dictionary));  
end2 = datetime.now()
print("medium dictionary time ===>", str(end2-start2)[5:]); 
start3 = datetime.now()
print("large dictionary ===>", wordbreak.wrapper(s, large_dictionary));  
end3 = datetime.now()
print("large dictionary time ===>", str(end3-start3)[5:]); 

