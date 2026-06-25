from src.extract.mysql_queries import load_top_actors
from src.load.excel_reporter import save_formatted_excel

def main():
    print("=" * 50)
    print("🚀 INICIANDO PIPELINE DE NEGOCIO - SAKILA")
    print("=" * 50)
    
    # 1. Extraer datos (llama a la consulta SQL)
    print("\n[1/3] Extrayendo datos desde MySQL...")
    df_actores = load_top_actors(limit=10)  # Cambia el 10 por 20 si quieres más
    
    # 2. Mostrar en consola para verificar
    print("\n[2/3] Mostrando Top 10 en consola:")
    print(df_actores.to_string(index=False))
    
    # 3. Guardar en Excel (llama al generador de reportes)
    print("\n[3/3] Cargando reporte a Excel...")
    archivo_generado = save_formatted_excel(df_actores, "top_10_actores_ingresos.xlsx")
    
    print("\n" + "=" * 50)
    print(f"🎉 PIPELINE COMPLETADO CON ÉXITO")
    print(f"📂 Abre el archivo: {archivo_generado}")
    print("=" * 50)

# Este es el "punto de entrada" estándar de Python.
# Solo se ejecuta si corres este archivo directamente (no si lo importas).
if __name__ == "__main__":
    main()