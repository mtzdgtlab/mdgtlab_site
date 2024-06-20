import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Cargar los datos de Excel
df = pd.read_excel("/Users/ismartinez/Sites/mdgt_finalsite/products_mdgt.xlsx")

# Configurar Jinja2 para cargar la plantilla
env = Environment(
    loader=FileSystemLoader(searchpath="./"),
    autoescape=select_autoescape(['html', 'xml'])
)

# Cargar la plantilla
template = env.get_template("plantilla.html")

# Verificar si las columnas de variantes existen
has_size = 'size' in df.columns
has_quantity = 'quantity' in df.columns
has_price = 'price' in df.columns

# Iterar sobre cada fila del DataFrame
product_data = None

for index, row in df.iterrows():
    # Si 'name' no es NaN, es una línea principal de producto
    if pd.notna(row['name']):
        # Si hay un producto actual, renderizarlo antes de proceder con el siguiente
        if product_data is not None:
            html_content = template.render(product_data)
            with open(f"{product_data['page_title']}.html", "w", encoding='utf-8') as f:
                f.write(html_content)
            print(f"Archivo generado: {product_data['page_title']}.html")
        
        product_data = row.fillna('').to_dict()
        product_data['variants'] = []

        # Verifica si los campos críticos están presentes y no son NaN
        required_fields = ['name', 'metad', 'productt', 'category', 'subcategory', 'img1', 'secalt', 'description']
        if not all([pd.notna(row[field]) for field in required_fields]):
            print(f"Faltan datos críticos en el índice {index}, se omite este registro.")
            product_data = None
            continue

    # Si 'name' es NaN, es una línea de variante
    elif product_data is not None:
        variant = {}
        if has_size:
            variant['size'] = row['size']
        if has_quantity:
            variant['quantity'] = row['quantity']
        if has_price:
            variant['price'] = row['price']
        
        if variant:
            product_data['variants'].append(variant)

# Renderizar el último producto si existe
if product_data is not None:
    html_content = template.render(product_data)
    with open(f"{product_data['page_title']}.html", "w", encoding='utf-8') as f:
        f.write(html_content)
    print(f"Archivo generado: {product_data['page_title']}.html")
