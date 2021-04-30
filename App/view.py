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
        print("El total de registros de eventos de escucha cargados: " + str(lt.size(om.keySet(cont['contextContent']))))
        print("El total de artistas únicos cargados:" + str(lt.size(om.keySet(cont['authors']))))
        print("El total de pistas de audio únicas cargadas:" + str(lt.size(om.keySet(cont['usertrack']))))
        print("Mostrar los primeros 5 y últimos 5 eventos de escucha cargados con sus características de contenido y de contexto.")

    elif int(inputs[0]) == 2:
        caracteristica=input("Característica de contenido (ej.: valencia, sonoridad, etc.) a buscar:")
        mini= int(input("El valor mínimo de la característica de contenido:"))
        maxi=int(input("El valor máximo de la característica de contenido:"))

    #elif int(inputs[0]) == 3:
    #elif int(inputs[0]) == 4:
   # elif int(inputs[0]) == 5:
    #elif int(inputs[0]) == 6:
        
    else:
        sys.exit(0)
sys.exit(0)


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()

    elif int(inputs[0]) == 2:
        print("\nCargando información de crimenes ....")
        controller.loadData(cont, crimefile)
        print('Crimenes cargados: ' + str(controller.crimesSize(cont)))
        print('Altura del arbol: ' + str(controller.indexHeight(cont)))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont)))
        print('Menor Llave: ' + str(controller.minKey(cont)))
        print('Mayor Llave: ' + str(controller.maxKey(cont)))

    elif int(inputs[0]) == 3:
        print("\nBuscando crimenes en un rango de fechas: ")
        initialDate = input("Fecha Inicial (YYYY-MM-DD): ")
        finalDate = input("Fecha Final (YYYY-MM-DD): ")
        total = controller.getCrimesByRange(cont, initialDate, finalDate)
        print("\nTotal de crimenes en el rango de fechas: " + str(total))

    elif int(inputs[0]) == 4:
        print("\nBuscando crimenes x grupo de ofensa en una fecha: ")
        initialDate = input("Fecha (YYYY-MM-DD): ")
        offensecode = input("Ofensa: ")
        numoffenses = controller.getCrimesByRangeCode(cont, initialDate,
                                                      offensecode)
        print("\nTotal de ofensas tipo: " + offensecode + " en esa fecha:  " +
              str(numoffenses))

    else:
        sys.exit(0)
sys.exit(0)
