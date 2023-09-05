# API de acceso para consultas
import pandas as pd
from fastapi import FastAPI



#Consultas de la API usando framework FastAPI

def userdata(user_id: str):
    """
    Retorna la cantidad de dinero gastado por el usuario y su porcentaje de recomendación 
    en base a las reviews positivas que tuvo sobre los distintos juegos.
    
    Parameters:
        user_id (str): ID del usuario.
        
    Returns:
        tuple: Una tupla que contiene la cantidad de dinero gastado 
        y el porcentaje de recomendación segun el usuario.
    """
   # Carga el dataset de api_userdata.csv
    userdata = pd.read_csv('api_userdata.csv')
    # Convierte la columna 'usuario' al tipo de dato string
    userdata['usuario'] = userdata['usuario'].astype(str)
    # Convierte la columna 'dinero_gastado' al tipo de dato float
    userdata['dinero_gastado'] = userdata['dinero_gastado'].astype(float)
    # Convierte la columna 'porcentaje_recomendacion' al tipo de dato float
    userdata['porcentaje_recomendacion'] = userdata['porcentaje_recomendacion'].astype(float)
    
    # Filtra los datos del usuario especificado
    filtered_userdata = userdata.loc[userdata['usuario'] == user_id]
    
    # Si el usuario no existe, retorna un mensaje de error
    if filtered_userdata.empty:
        return 'El usuario especificado no existe'
    
    # Si el usuario existe, retorna la cantidad de dinero gastado y el porcentaje de recomendación
    else:
        money_spent = filtered_userdata['dinero_gastado'].values[0]
        recommendation_percentage = filtered_userdata['porcentaje_recomendacion'].values[0]
        return money_spent, recommendation_percentage
    
    

def counterviews(start_date, end_date):
    """
    Cuenta la cantidad de usuarios únicos que realizaron revisiones entre dos fechas
    y calcula el porcentaje de recomendación promedio.

    Parameters:
        start_date (str): Fecha de inicio en formato 'YYYY-MM-DD'.
        end_date (str): Fecha de fin en formato 'YYYY-MM-DD'.

    Returns:
        tuple: Una tupla que contiene la cantidad de usuarios únicos y el porcentaje promedio de recomendación.
    """
    # Carga el dataset de api_counterviews.csv
    reviews = pd.read_csv('api_counterviews.csv')
    # Convierte la columna 'fecha' al tipo de dato datetime
    reviews['fecha'] = pd.to_datetime(reviews['fecha'])

    # Filtra las revisiones dentro del rango de fechas especificado
    filtered_reviews = reviews.loc[(reviews['fecha'] >= start_date) & (reviews['fecha'] <= end_date)]

    # Cuenta la cantidad de usuarios únicos que realizaron revisiones en ese rango
    unique_users_count = filtered_reviews['usuario'].nunique()

    # Calcula el porcentaje de recomendación promedio
    average_recommendation_percentage = filtered_reviews['recommend'].mean() * 100

    # Imprime los resultados
    print(f'Cantidad de usuarios que realizaron revisiones entre {start_date} y {end_date}: {unique_users_count}')
    print(f'Porcentaje de recomendación promedio: {average_recommendation_percentage:.2f}%')
    
    
