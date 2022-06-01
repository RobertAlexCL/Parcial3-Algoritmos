
# Codigo extraido de https://www.geeksforgeeks.org/ por shinjanpatra

from datetime import datetime


import time 

# Devolvera verdadero si las palabras pueden ser divididas en palabras presentes en el diccionario 
def wordBreak(word):
	
	global dictionary1
	size = len(word)

	# Caso base (indivisible)
	if (size == 0):
		return True


	#Revisa contra todas las palabras
	for i in range(1,size + 1):

		##subdivide la palabra recursivamente 
		## la primera parte se revisa si esta presente en el diccionario; la segunda parte se envia como argumento a la misma fucion
		
		if (word[0:i] in dictionary and wordBreak(word[i: size])):
			
			return True

	# En caso que no se cumple 
	
	return False

# set to hold dictionary values
dictionary = set()


# 10 words
small_dictionary = [
"solo","si","contrario","una","uno","comer","dormir","solitario","decidir","el"]

#50 words
medium_dictionary = ["solo","si","contrario","una","uno","comer","dormir","solitario","decidir",
"el","la","soldado","que","no","se","si","un","una","para","por","mi","tu","y","con","unos","unas",
"dos","se","ha","reir","quiere","quiero","como","cual","donde","estar","estoy","mis","tus","puente","diente","camino","compu","reloj","saber","cuanto","numeros","salsa",
"angel","martir"
]


#100 words
large_dictionary = [
"solo","si","contrario","una","uno","comer","dormir","solitario","decidir","el","la","soldado","que","no","se","si","un","una","para","por","mi","tu","y","con","unos","unas","dos","se","ha","reir","quiere","quiero",
"como","cual","donde","estar","estoy","mis","tus","puente","diente","camino","compu","reloj",
"saber","cuanto","numeros","salsa","angel","martir","dulce","andres","solo","dime","carretera","contra","in","joder","kilo","nunca","luis","fregar",
"jabali","teclado","musica","dosis","armado","caballero","dama","almeja","santo",
"santa","hace","gringo","cobarde","hombre","mujer","musico","bella","muerte","dormitorio","cabeza","guardar","salvar","tarjeta","lapiz",
"telefono","ordenador","turing","caja","negra","recurso","punta","inutil","camello","camisa","papel",
"dermis","dante","comerdor","salir","tucan"]




# Guarda las palabras en diccionarios
for temp in large_dictionary:
	dictionary.add(temp)









start = datetime.now()
print("Para la palabra el:")
print("Yes" if wordBreak("el") else "No")
#print("--- %s seconds ---" % (time.time_ns() - start_time))
end = datetime.now()
print("The time of execution of above program is :",
      str(end-start)[1:])


start = datetime.now()
print("Para la plabra eldecidir:")
print("Yes" if wordBreak("eldecidir") else "No")
end = datetime.now()
print("The time of execution of above program is :",
      str(end-start)[1:])


start = datetime.now()
print("Para la palabra eldecidirsolitario:")
print("Yes" if wordBreak("eldecidirsolitario") else "No")
end = datetime.now()
print("The time of execution of above program is :",
      str(end-start)[1:])



start = datetime.now()
print("Para la palabre eldecidirsolitariodormir: " )
print("Yes" if wordBreak("eldecidirsolitariodormir") else "No")
end = datetime.now()
print("The time of execution of above program is :",
      str(end-start)[1:])


start = datetime.now()
print("Para la palabra eldecidirsolitariodormircomer:")
print("Yes" if wordBreak("eldecidirsolitariodormircomer") else "No")
end = datetime.now()
print("The time of execution of above program is :",
      str(end-start)[1:])

small_dictionary = [
"solo","si","contrario","una","uno","comer","dormir","solitario","decidir","el"]

##"solosicontrariounaunocomerdormirsolitariodecidirel"


start = datetime.now()
print("Para la palabra comerdormirsolitariodecidirel:")
print("Yes" if wordBreak("comerdormirsolitariodecidirel") else "No")
end = datetime.now()
print("The time of execution of above program is :",
      str(end-start)[1:])



start = datetime.now()
print("Para la palabra :unocomerdormirsolitariodecidirel")
print("Yes" if wordBreak("unocomerdormirsolitariodecidirel") else "No")
end = datetime.now()
print("The time of execution of above program is :",
      str(end-start)[1:])


start = datetime.now()
print("Para la palabra unaunocomerdormirsolitariodecidirel:")
print("Yes" if wordBreak("unaunocomerdormirsolitariodecidirel") else "No")
end = datetime.now()
print("The time of execution of above program is :",
      str(end-start)[1:])


start = datetime.now()
print("Para la palabra contrariounaunocomerdormirsolitariodecidirel:")
print("Yes" if wordBreak("contrariounaunocomerdormirsolitariodecidirel") else "No")
end = datetime.now()
print("The time of execution of above program is :",
      str(end-start)[1:])

start = datetime.now()
print("Para la palabra unaunocomerdormirsolitariodecidirel:")
print("Yes" if wordBreak("unaunocomerdormirsolitariodecidirel") else "No")
end = datetime.now()
print("The time of execution of above program is :",
      str(end-start)[1:])

