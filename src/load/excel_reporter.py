import pandas as pd
import os

def save_formatted_excel(df, filename="reporte_actores.xlsx"):
    """
    Guarda un DataFrame en Excel con formato profesional.
    - Cabeceras en azul oscuro con letra blanca.
    - Bordes en todas las celdas.
    - Formato de moneda ($) para la columna de ingresos.
    - Ancho de columna ajustado automáticamente.
    """
    # 1. Asegurar que la carpeta 'reports' existe (la crea si no está)
    os.makedirs("reports", exist_ok=True)
    filepath = os.path.join("reports", filename)
    
    print(f"📁 Generando archivo: {filepath} ...")
    
    # 2. Usamos 'xlsxwriter' como motor para dar formato profesional
    with pd.ExcelWriter(filepath, engine='xlsxwriter') as writer:
        # 3. Volcamos el DataFrame a la hoja "Top Actores" (sin el índice)
        df.to_excel(writer, sheet_name='Top Actores', index=False)
        
        # 4. Obtenemos el libro y la hoja para aplicar formatos
        workbook = writer.book
        worksheet = writer.sheets['Top Actores']
        
        # 5. Definimos los "estilos" (como si fueran plantillas de Word)
        #    - Cabecera: Negrita, azul marino, letra blanca, borde
        header_format = workbook.add_format({
            'bold': True,
            'fg_color': '#1F4E78',   # Azul corporativo
            'font_color': 'white',
            'border': 1
        })
        #    - Dinero: con signo $ y dos decimales
        money_format = workbook.add_format({'num_format': '$#,##0.00', 'border': 1})
        #    - Números enteros: con separador de miles
        int_format = workbook.add_format({'num_format': '#,##0', 'border': 1})
        #    - Texto normal: solo con borde
        text_format = workbook.add_format({'border': 1})
        
        # 6. Aplicar el formato de cabecera a la primera fila (fila 0)
        for col_num, value in enumerate(df.columns.values):
            worksheet.write(0, col_num, value, header_format)
        
        # 7. Ajustar el ancho de las columnas automáticamente
        #    Recorre cada columna, calcula el texto más largo y añade 2 espacios
        for i, col in enumerate(df.columns):
            max_len = max(df[col].astype(str).map(len).max(), len(col)) + 2
            worksheet.set_column(i, i, max_len)
        
        # 8. Rellenar las filas de datos con el formato correspondiente
        #    Recorre fila por fila y columna por columna
        for row_num in range(len(df)):
            for col_num, col_name in enumerate(df.columns):
                value = df.iloc[row_num, col_num]
                # Aplica formato según el nombre de la columna
                if col_name == 'ingreso_total':
                    worksheet.write(row_num + 1, col_num, value, money_format)
                elif col_name == 'total_alquileres':
                    worksheet.write(row_num + 1, col_num, value, int_format)
                else:
                    worksheet.write(row_num + 1, col_num, value, text_format)
    
    print(f"✅ Archivo guardado exitosamente en: {filepath}")
    return filepath