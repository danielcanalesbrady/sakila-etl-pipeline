import pandas as pd
from config.db import get_engine

def load_top_actors(limit=10):
    """
    Extrae el Top N de actores con mayores ingresos por alquiler.
    La consulta cruza 6 tablas para calcular el total generado por cada actor.
    """
    # Obtenemos el motor de conexión (el "enchufe")
    engine = get_engine()
    
    # Consulta SQL con JOINs y agregación
    query = f"""
    SELECT 
        a.actor_id,
        CONCAT(a.first_name, ' ', a.last_name) AS nombre_actor,
        COUNT(r.rental_id) AS total_alquileres,
        SUM(p.amount) AS ingreso_total
    FROM actor a
    JOIN film_actor fa ON a.actor_id = fa.actor_id
    JOIN film f ON fa.film_id = f.film_id
    JOIN inventory i ON f.film_id = i.film_id
    JOIN rental r ON i.inventory_id = r.inventory_id
    JOIN payment p ON r.rental_id = p.rental_id
    GROUP BY a.actor_id, nombre_actor
    ORDER BY ingreso_total DESC
    LIMIT {limit};
    """
    
    print("📊 Ejecutando consulta en Sakila...")
    # Pandas ejecuta la consulta y devuelve un DataFrame
    df = pd.read_sql(query, engine)
    return df