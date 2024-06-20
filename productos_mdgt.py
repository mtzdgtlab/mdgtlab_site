import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Cargar los datos de Excel
df = pd.read_excel("/Users/ismartinez/Sites/mdgt_finalsite/assets/db/products_mdgt.xlsx")

# Imprime los nombres de las columnas para verificar
print(df.columns)

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
    
    # Asegúrate de que 'product_uses' corresponde a una columna en tu Excel.
    product_uses = row.get('product_uses', 'N/A')  # 'N/A' en caso de que falte 'product_uses'
    
    # Asegúrate de que 'size', 'quantity' y 'price' correspondan a columnas en tu Excel.
    size = row.get('size', None)
    quantity = row.get('quantity', None)
    price = row.get('price', None)
    
    # Actualiza el diccionario de datos para la plantilla
    product_data = row.fillna('').to_dict()  # Reemplaza NaN con cadenas vacías
    product_data['product_uses'] = product_uses
    product_data['size'] = size
    product_data['quantity'] = quantity
    product_data['price'] = price
    
    # Renderizar la plantilla con los datos del producto
    html_content = template.render(product_data)
    
    # Guardar el contenido en un nuevo archivo HTML
    with open(f"{nombre_archivo}.html", "w", encoding='utf-8') as f:
        f.write(html_content)
