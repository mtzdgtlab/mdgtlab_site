import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Cargar los datos de Excel
df = pd.read_excel("/Users/ismartinez/Sites/mdgt_finalsite/assets/db/products_mdgt.xlsx")

# Configurar Jinja2 para cargar la plantilla
env = Environment(
    loader=FileSystemLoader(searchpath="./"),
    autoescape=select_autoescape(['html', 'xml'])
)

# Cargar la plantilla
template = env.get_template("plantilla.html")

# Iterar sobre cada fila del DataFrame
for index, row in df.iterrows():
    try:
        nombre_archivo = row['page_title']
    except KeyError:
        print(f"Columna 'page_title' no encontrada para el índice {index}, se omite este registro.")
        continue
    
    # Verifica si los campos críticos están presentes y no son NaN
    required_fields = ['product_name', 'meta_description', 'product_tittle', 'category', 'subcategory', 'image_path1', 'product_sectionalt', 'body_description']
    if not all([pd.notna(row[field]) for field in required_fields]):
        print(f"Faltan datos críticos en el índice {index}, se omite este registro.")
        continue
    
    # Asegúrate de que 'product_uses' corresponde a una columna en tu Excel.
    product_uses = row.get('product_uses', None)  # None en caso de que falte 'product_uses'
    
    # Actualiza el diccionario de datos para la plantilla
    product_data = row.fillna('').to_dict()  # Reemplaza NaN con cadenas vacías
    product_data['product_uses'] = product_uses
    
    # Renderizar la plantilla con los datos del producto
    html_content = template.render(product_data)
    
    # Guardar el contenido en un nuevo archivo HTML
    with open(f"{nombre_archivo}.html", "w", encoding='utf-8') as f:
        f.write(html_content)
