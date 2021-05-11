"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as mp
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Cargar la Informacion")
    print("2- REQ. 1: Caracterizar las reproducciones ")
    print("3- REQ. 2: Encontrar música para festejar")
    print("4- REQ. 3:Encontrar música para estudiar")
    print("5- REQ. 4: Estimar las reproduccionesde los géneros musicales")
    print("6- REQ. 5: Indicar el género musical más escuchado en un tiempo") 
    print("0- Salir")
    print("*******************************************")

crimefile = 'crime-utf8.csv'
cont = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()
        cont=controller.loadData(cont)
        conta=cont[0]
        print("Tiempo [ms]: ", f"{cont[1]:.3f}", "  ||  ",
        "Memoria [kB]: ", f"{cont[2]:.3f}")
        print("El total de registros de eventos de escucha cargados: " + str(lt.size(mp.keySet(conta['contextContent']))))
        #print("El total de artistas únicos cargados:" + str(lt.size(mp.keySet(cont['authors']))))
        print("El total de pistas de audio únicas cargadas:" + str(lt.size(mp.keySet(conta['contextContent']))))
        print("Mostrar los primeros 5 y últimos 5 eventos de escucha cargados con sus características de contenido y de contexto.")

    elif int(inputs[0]) == 2:
        caract=input("Característica de contenido (ej.: valencia, sonoridad, etc.) a buscar:")
        mini=str(input("El valor mínimo de la característica de contenido:"))
        maxi=str(input("El valor máximo de la característica de contenido:"))
        result=controller.caracterizaReproducciones(cont[0],caract,mini,maxi)
        ans=result[0]
        print ("Total of reproductions: {0} | Total of unique artists: {1}".format(ans[0],ans[1]))
        data=result[1]
        print("Tiempo [ms]: ", f"{data[0]:.3f}", "  ||  ",
        "Memoria [kB]: ", f"{data[1]:.3f}")
    elif int(inputs[0]) == 3:
        minid=str(input("El valor mínimo de Danceability de contenido:"))
        maxid=str(input("El valor máximo de Danceability de contenido:"))
        minie=str(input("El valor mínimo de Energy de contenido:"))
        maxie=str(input("El valor máximo de Energy de contenido:"))
        result=controller.musicFest(cont[0],minie,maxie,minid,maxid)
        ans=result[0]
        print("Total of unique tracks in events: {0}".format(ans[0]))
        for a in ans[1]['elements']: 
            print(a)
        data=result[1]
        print("Tiempo [ms]: ", f"{data[0]:.3f}", "  ||  ",
        "Memoria [kB]: ", f"{data[1]:.3f}")
    #elif int(inputs[0]) == 4:
    elif int(inputs[0]) == 4:
        minIn=str(input("El valor mínimo de instrumentalness de contenido:"))
        maxIn=str(input("El valor máximo de instrumentalness de contenido:"))
        minTe=str(input("El valor mínimo de Tempo de contenido:"))
        maxTe=str(input("El valor máximo de Tempo de contenido:"))
        result=controller.Req3(cont[0],minIn,maxIn,minTe,maxTe)
        ans=result[0]
        print("Total of unique tracks in events: {0}".format(ans[0]))
        for a in ans[1]['elements']: 
            print(a)
        data=result[1]
        print("Tiempo [ms]: ", f"{data[0]:.3f}", "  ||  ",
        "Memoria [kB]: ", f"{data[1]:.3f}")
    elif int(inputs[0]) == 5:
        tipo=input("la lista de géneros musicales que se desea buscar, separado por comas:")
        tipo=list(tipo.split(", "))
        result=controller.generosMusicales(cont[0],tipo)
        ans=result[0]
        print("Total of reproductions:"+ str(ans[0]))
        #print(lt.size(ans[1]))
        for a in range(0,(lt.size(ans[1]))):
            b=lt.getElement(ans[1], a)
            print("__________{0}__________".format(b[0]))
            print('{0} reproductions: {1} with {2} different artists'.format(b[0],b[1],b[2]))
            for i in range (0,10):
                c=lt.getElement(b[3], i)
                print()
                print('artist {0}: {1}'.format(i+1,c))
        data=result[1]
        print("Tiempo [ms]: ", f"{data[0]:.3f}", "  ||  ",
        "Memoria [kB]: ", f"{data[1]:.3f}")

    #elif int(inputs[0]) == 6:
        
    else:
        sys.exit(0)
sys.exit(0)
