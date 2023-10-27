import csv

def traer_data():
    with open("dataset_animales.csv", "r") as f:
        lector = csv.reader(f, delimiter=",")
        animales = []
        titulos = []
        aux = 0
        for fila in lector:
            if aux == 0:
                titulo = [fila[0],fila[1],fila[2],fila[3],fila[4],fila[5]]
                titulos.append(titulo)
            else:
                # Guardar los valores en una variable
                animal = [fila[0],fila[1],fila[2],fila[3],fila[4],fila[5]]
                animales.append(animal)
            aux = aux + 1
    return titulos, animales

def calcular_gini(agrupamiento, animales):
    columnas = list(zip(*animales))
    n_animales = len(animales)
    for preguntas in agrupamiento:
        score = 9999
        columna = 0
        for pregunta in preguntas:
            #Aqui calcula el nodo principal
            lista_pregunta = [fila for fila in animales if fila[columna] == pregunta]
            lista_no_pregunta = [fila for fila in animales if fila[columna] != pregunta]
            num_pregunta = len(lista_pregunta)
            num_no_pregunta = n_animales - num_pregunta
            gini = []
            for clasificacion in agrupamiento[-1]:
                lista_clasificacion = [fila for fila in lista_pregunta if fila[-1] == clasificacion]
                num_clasificacion = len(lista_clasificacion)
                gini.append(num_clasificacion)
            print(gini)



#INICIO DEL CODIGO
titulos, animales = traer_data()
print(animales)

#SE DEFINE CUALES SERAN LAS BASES DE LAS PREGUNTAS POR CADA FEATURE
agrupamiento = []
for columna in list(zip(*animales)):
    nueva_lista = list(set(columna))
    agrupamiento.append(nueva_lista)

#SE CALCULA EL GINI CON EL AGRUPAMIENTO y EL SET
calcular_gini(agrupamiento, animales)



