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
from DISClib.DataStructures import listiterator as lit
assert cf
import sys
import random
from random import seed
from random import randint
import datetime
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
                'features':None}

    analyzer['sentiment'] = om.newMap(omaptype='BST',
                                     comparefunction=compareNames)
    analyzer['contextContent'] = mp.newMap(maptype='CHAINING')
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
                            "key":om.newMap(omaptype='RBT',comparefunction=compareIds)}
    analyzer['dates'] = om.newMap(omaptype='RBT', comparefunction=compareIds)
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

    features=["instrumentalness","liveness","speechiness","danceability","valence","loudness","tempo","acousticness","energy","mode","key"]
    cara=analyzer['features']
    for car in features:
        r=data[car]
        exists= om.contains(cara[car],data[car])
        if exists:
            entry=om.get(cara[car],data[car])
            newL=me.getValue(entry)
        else:  
            mewL=lt.newList()
            wewL=lt.newList()
            newL=(mewL,wewL)
        lt.addLast(newL[0],data['track_id'])
        lt.addLast(newL[1],data['artist_id'])
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

def addDate(analyzer, data):
    horaN =str(data['created_at'].split(" ")[1].split(":")[0])
    horaM =str(data['created_at'].split(" ")[1].split(":")[1])
    hora=(horaN+horaM)
    horas=int(hora)
    fecha = datetime.time(int(horaN[0]),int(horaN[1]))
    exists= om.contains(analyzer['dates'],horas)
    if exists:
        entry=om.get(analyzer['dates'],horas)
        newL=me.getValue(entry)
    else:
        newL=lt.newList()
    lt.addLast(newL,data)
    om.put(analyzer['dates'],horas,newL)
# Funciones para creacion de datos
def oneList(li):
    lis=lt.newList('ARRAY_LIST')
    size=(lt.size(li))+1
    for a in range(1,size):
        element=lt.getElement(li, a)
        si=(lt.size(element[0]))+1
        for j in range (1,si):
            ine=lt.getElement(element[0], j)
            lt.addLast(lis, ine)
    return lis 
def oneList1(li):
    lis=lt.newList('ARRAY_LIST')
    size=(lt.size(li))+1
    for a in range(1,size):
        element=lt.getElement(li, a)
        si=(lt.size(element))+1
        for j in range (1,si):
            ine=lt.getElement(element, j)
            lt.addLast(lis, ine)
    return lis 
# Funciones de consulta
def caracterizaReproducciones (analyzer,caracteristica,mini,maxi):
    feat=analyzer['features']
    cara=feat[caracteristica]
    rango=om.values(cara,mini,maxi)
    b=lit.newIterator(rango)
    mew=lt.newList('ARRAY_LIST',cmpfunction=compareNames)
    tot=lt.newList('ARRAY_LIST',cmpfunction=compareNames)
    size=0
    while lit.hasNext(b):
        video=lit.next(b)
        sixe=lt.size(video[0])
        size+=sixe
        e=lit.newIterator(video[1])
        while lit.hasNext(e):
            objeto=lit.next(e)
            a=lt.isPresent(mew, objeto)
            if a==0: 
                lt.addLast(mew, objeto)
    sizea=lt.size(mew)
    return(size,sizea)

def musicFest(analyzer,mine,maxe,mind,maxd):
    feat=analyzer['features']
    rangod=om.values(feat["danceability"],mind,maxd)
    rangoe=om.values(feat["energy"],mine,maxe)
    da=lt.newList('ARRAY_LIST',cmpfunction=compareNames)
    en=lt.newList('ARRAY_LIST',cmpfunction=compareNames)
    mew=lt.newList('ARRAY_LIST',cmpfunction=compareNames)
    da=oneList(rangod)
    en=oneList(rangoe)
    b=lit.newIterator(da)
    while lit.hasNext(b):
        objeto=lit.next(b)
        a=lt.isPresent(en, objeto)
        c=lt.isPresent(mew,objeto)
        if a!=0 and c==0: 
            lt.addLast(mew, objeto)
    size=lt.size(mew)
    seed(1)
    num=lt.newList('ARRAY_LIST')
    for a in range (1,6):
        value=randint(1,size)
        track=lt.getElement(mew, value)
        entry=mp.get(analyzer['contextContent'],track)
        newL=me.getValue(entry)
        d=(newL['first']['info']['danceability'])
        e=(newL['first']['info']['energy'])
        trackr="track{0}:{1} with energy of {2} and danceability of {3}.".format(a,track,e,d)
        lt.addLast(num, trackr)
    return (size,num)

def Req3(analyzer,minIn,maxIn,minTe,maxTe):
    feat=analyzer['features']
    rangoIn=om.values(feat["instrumentalness"],minIn,maxIn)
    rangoTe=om.values(feat["tempo"],minTe,maxTe)
    da=lt.newList('ARRAY_LIST',cmpfunction=compareNames)
    en=lt.newList('ARRAY_LIST',cmpfunction=compareNames)
    mew=lt.newList('ARRAY_LIST',cmpfunction=compareNames)
    da=oneList(rangoIn)
    en=oneList(rangoTe)
    b=lit.newIterator(da)
    while lit.hasNext(b):
        objeto=lit.next(b)
        a=lt.isPresent(en, objeto)
        c=lt.isPresent(mew,objeto)
        if a!=0 and c==0: 
            lt.addLast(mew, objeto)
    size=lt.size(mew)
    seed(1)
    num=lt.newList('ARRAY_LIST')
    for a in range (1,6):
        value=randint(1,size)
        track=lt.getElement(mew, value)
        entry=mp.get(analyzer['contextContent'],track)
        newL=me.getValue(entry)
        d=(newL['first']['info']['instrumentalness'])
        e=(newL['first']['info']['tempo'])
        trackr="track{0}:{1} with tempo of {2} and instrumentalness of {3}.".format(a,track,e,d)
        lt.addLast(num, trackr)
    return (size,num)

def generosMusicales(analyzer,tipo):
    feat=analyzer['features']
    total=0
    nom=lt.newList()
    for gen in tipo:
        if gen=="Reggae":
            minn='60'
            maxx='90'
        elif  gen=="Down-tempo":
            minn='70'
            maxx='100'
        elif gen=='Chill-out':
            minn='90'
            maxx='120'
        elif gen=='Hip-hop':
            minn='85'
            maxx='115'
        elif gen=='Jazz and Funk':
            minn='120'
            maxx='125'
        elif gen=='Pop':
            minn='100'
            maxx='130'
        elif gen=='R&B':
            minn='60'
            maxx='80'
        elif gen=='Rock':
            minn='110'
            maxx='140'
        elif gen=='Metal':
            minn='100'
            maxx='160'
        else:
            minn=str(input("Valor mínimo del Tempo del género musical:"))
            maxx=str(input("Valor maximo del Tempo del género musical:"))
        size=0
        rango=om.values(feat["tempo"],minn,maxx)
        b=lit.newIterator(rango)
        mew=lt.newList()
        while lit.hasNext(b):
            video=lit.next(b)
            sixe=lt.size(video[0])
            size+=sixe
            e=lit.newIterator(video[1])
            si=lt.size(mew)
            while lit.hasNext(e):
                objeto=lit.next(e)
                a=lt.isPresent(mew, objeto)
                if a==0: 
                    lt.addLast(mew, objeto) 
            sizea=lt.size(mew)
        ap= (gen,size,sizea,mew)
        lt.addLast(nom, ap)
        total+=size
    return (total,nom)
def Req5(analyzer, minH, maxH):
    analyzer=analyzer[0]
    tiempoMin=minH.split(':')
    f=minH.split(':')[0]
    g=minH.split(':')[1]
    tmin=(f+g)
    Tmin=int(tmin)
    tiempoMax=maxH.split(':')
    f2=minH.split(':')[0]
    g2=minH.split(':')[1]
    tmax=(f2+g2)
    Tmax=int(tmax)
    feat=analyzer['dates']
    feat2=analyzer['features']
    feat3=analyzer['contextContent']

    rangoHoras=om.values(feat,Tmin,Tmax)
    print(rangoHoras)
    
    
    mapa1 = {'reggae':[60,90],'down-tempo':[70,100],'chill-out':[90,120],'hip-hop':[85,115],'jazzandfunk':[120,150],'pop':[100,130],'r&b':[60,80],'rock':[110,140],'metal':[100,160]}
    
    b=oneList1(rangoHoras)
    reggae = lt.newList('ARRAY_LIST')
    down = lt.newList('ARRAY_LIST')
    chillOut = lt.newList('ARRAY_LIST')
    hipHop = lt.newList('ARRAY_LIST')
    jazzandfunk = lt.newList('ARRAY_LIST')
    pop = lt.newList('ARRAY_LIST')
    ryb = lt.newList('ARRAY_LIST')
    rock = lt.newList('ARRAY_LIST')
    metal = lt.newList('ARRAY_LIST')

    a=lit.newIterator(b)
    mew=lt.newList()
    
    while lit.hasNext(a):
        video=lit.next(a)
        sixe=lt.size(video[0])
        size+=sixe
        e=lit.newIterator(video[1])
        si=lt.size(mew)
        while lit.hasNext(e):
                objeto=lit.next(e)
                a=lt.isPresent(mew, objeto)
                if a==0: 
                    lt.addLast(mew, objeto) 
    
    contador = 0
    max = 0
    maximom=""
    maximo = None

    for i in lt.iterator(mew):
        if i[feat2]["tempo"]  > 60 and i[feat2]["tempo"] < 90:
            lt.addLast(reggae, i)
        if i[feat2]["tempo"]  > 70 and i[feat2]["tempo"] < 100:
            lt.addLast(down, i) 
        if i[feat2]["tempo"]  > 90 and i[feat2]["tempo"] < 120:
            lt.addLast(chillOut, i) 
        if i[feat2]["tempo"]  > 85 and i[feat2]["tempo"] < 115:
            lt.addLast(hipHop, i) 
        if i[feat2]["tempo"]  > 120 and i[feat2]["tempo"] < 125:
            lt.addLast(jazzandfunk, i) 
        if i[feat2]["tempo"]  > 100 and i[feat2]["tempo"] < 130:
            lt.addLast(pop, i) 
        if i[feat2]["tempo"]  > 60 and i[feat2]["tempo"] < 80:
            lt.addLast(ryb, i) 
        if i[feat2]["tempo"]  > 110 and i[feat2]["tempo"] < 140:
            lt.addLast(rock, i) 
        if i[feat2]["tempo"]  > 100 and i[feat2]["tempo"] < 160:
            lt.addLast(metal, i) 
    
        
         
         
                




        
    
        
    


    
    

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