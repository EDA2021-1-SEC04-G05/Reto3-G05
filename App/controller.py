﻿"""
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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
# Inicialización del Catálogo de libros
def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    return analyzer
# Funciones para la carga de datos
def loadData(analyzer):
    loadSentiment(analyzer)
    loadContextContent(analyzer)
    loadUsertrack(analyzer)
    return analyzer
def loadSentiment(catalog):
    sfile = cf.data_dir + 'subsamples-small/sentiment_values.csv'
    input_file = csv.DictReader(open(sfile, encoding='utf-8'),delimiter=",")
    for line in input_file:
        model.addSentiment(catalog, line)

def loadContextContent(catalog):
    sfile = cf.data_dir + 'subsamples-small/context_content_features-small.csv'
    input_file = csv.DictReader(open(sfile, encoding='utf-8'),delimiter=",")
    for line in input_file:
        model.addContextContent(catalog, line)
    
def loadUsertrack(catalog):
    sfile = cf.data_dir + 'subsamples-small/user_track_hashtag_timestamp-small.csv'
    input_file = csv.DictReader(open(sfile, encoding='utf-8'),delimiter=",")
    for line in input_file:
        model.addUsertrack(catalog, line)
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def caracterizaReproducciones (catalog,caracteristica,mini,maxi):
    ans=model.caracterizaReproducciones(catalog,caracteristica,mini,maxi)
    return ans 
def musicFest(catalog,mine,maxe,mind,maxd):
    ans=model.musicFest(catalog,mine,maxe,mind,maxd)
    return ans