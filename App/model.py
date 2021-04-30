"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
assert cf
import sys

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
sys.setrecursionlimit(999999)
# Construccion de modelos
def newAnalyzer():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los crimenes
    Se crean indices (Maps) por los siguientes criterios:
    Retorna el analizador inicializado.
    """
    analyzer = {'sentiment': None,
                'contextContent': None,
                'features':None,
                'authors':None}

    analyzer['sentiment'] = om.newMap(omaptype='BST',
                                     comparefunction=compareNames)
    analyzer['contextContent'] = mp.newMap(maptype='BST')
                                      #comparefunction=compareIds)
    analyzer['features'] = {"instrumentalness":om.newMap(omaptype='RBT',comparefunction=compareIds),
                            "liveness":om.newMap(omaptype='RBT',comparefunction=compareIds),
                            "speechiness":om.newMap(omaptype='RBT',comparefunction=compareIds),
                            "danceability":om.newMap(omaptype='RBT',comparefunction=compareIds),
                            "valence":om.newMap(omaptype='RBT',comparefunction=compareIds),
                            "loudness":om.newMap(omaptype='RBT',comparefunction=compareIds),
                            "tempo":om.newMap(omaptype='RBT',comparefunction=compareIds),
                            "acousticness":om.newMap(omaptype='RBT',comparefunction=compareIds),
                            "energy":om.newMap(omaptype='RBT',comparefunction=compareIds),
                            "mode":om.newMap(omaptype='RBT',comparefunction=compareIds),
                            "key":om.newMap(omaptype='RBT',comparefunction=compareIds),
                            "artist_id":om.newMap(omaptype='RBT',comparefunction=compareIds)}
                                      #comparefunction=compareIds)
    analyzer['authors'] = om.newMap(omaptype='BST',comparefunction=compareIds)
    return analyzer

# Funciones para agregar informacion al catalogo
def addSentiment(analyzer,data):
    exists= om.contains(analyzer['sentiment'],data['hashtag'])
    if exists:
        entry=om.get(analyzer['sentiment'],data['hashtag'])
        newL=me.getValue(entry)
    else: 
        newL=lt.newList()
    lt.addLast(newL,data)
    om.put(analyzer['sentiment'],data['hashtag'],newL)
    
def addContextContent(analyzer, data):
    exists= mp.contains(analyzer['contextContent'],data['track_id'])
    if exists:
        entry=mp.get(analyzer['contextContent'],data['track_id'])
        newL=me.getValue(entry)
    else: 
        newL=lt.newList()
    lt.addLast(newL,data)
    
    mp.put(analyzer['contextContent'],data['track_id'],newL)

    exists= om.contains(analyzer['authors'],data['artist_id'])
    if exists:
        entry=om.get(analyzer['authors'],data['artist_id'])
        newL=me.getValue(entry)
    else: 
        newL=lt.newList()
    lt.addLast(newL,data)
    om.put(analyzer['authors'],data['artist_id'],newL)

    features=["instrumentalness","liveness","speechiness","danceability","valence","loudness","tempo","acousticness","energy","mode","key"]
    cara=analyzer['features']
    for car in features:
        exists= om.contains(cara[car],data[car])
        if exists:
            entry=om.get(cara[car],data[car])
            newL=me.getValue(entry)
        else:  
            newL=lt.newList()
        lt.addLast(newL,data['track_id'])
        om.put(cara[car],data[car],newL)


def addUsertrack(analyzer, data):
    exists= mp.contains(analyzer['contextContent'],data['track_id'])
    if exists:
        entry=mp.get(analyzer['contextContent'],data['track_id'])
        newL=me.getValue(entry)
    else: 
        newL=lt.newList()
    lt.addLast(newL,data['hashtag'])
    mp.put(analyzer['contextContent'],data['track_id'],newL)
# Funciones para creacion de datos

# Funciones de consulta
def caracterizaReproducciones (analyzer,caracteristica,mini,maxi):
    feat=analyzer['features']
    cara=feat[caracteristica]
    
    

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

def compareIds(id1, id2):
    """
    Compara dos crimenes
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1
def compareNames(countryname, entry):
    """
    Compara dos ids de videos, id es un identificador
    y entry una pareja llave-valor
    """
    if countryname == entry :
        return 0
    elif countryname > entry:
        return 1
    else:
        return -1