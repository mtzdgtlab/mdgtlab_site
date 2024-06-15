import pandas as pd

# Cargar los datos desde el archivo Excel
df = pd.read_excel('/Users/ismartinez/Library/Mobile Documents/com~apple~CloudDocs/mdgt_files/site/mdgtlab_site/assets/db/mdgtlab_productos.xlsx')

# Función para generar HTML para cada producto
def generate_product_html(row):
    return f'''
        <div class="col-lg-4 col-md-6 sm-6 ">
            <div class="swiper-slide align-items-center">
                <div class="latest-blog__item-slide-inner align-items-center">
                    <div class="latest-blog__item-media align-items-center">
                        <a href="{row['product_link']}">
                            <img src="{row['preview_path1']}" alt="{row['product_sectionalt']}" class="img-fluid">
                        </a>
                    </div>
                    <div class="latest-blog__item-text align-items-center text-center">
                        <div class="latest-blog__item-text-meta d-flex flex-column align-items-center">
                            <div class="latest-blog__item-text-meta-calender align-items-center">
                                <a href="{row['product_link']}">
                                    <h4>{row['product_name']}</h4>
                                    <span class="meta-comment">{row['category']}</span>
                                </a>
                            </div>
                        </div>
                        <div class="latest-blog__item-text-bottom" style="text-align: justify;">
                            <p>{row['product_description']}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    '''

# Generar el HTML para todos los productos y dividirlos en grupos de 6 (2 filas de 3 productos)
all_products_html = [generate_product_html(row) for index, row in df.iterrows()]
products_pages = [all_products_html[i:i + 6] for i in range(0, len(all_products_html), 6)]

# Leer el archivo HTML original
with open('/Users/ismartinez/Library/Mobile Documents/com~apple~CloudDocs/mdgt_files/site/mdgtlab_site/assets/db/print.html', 'r') as file:
    html_content = file.read()

# Punto de inserción para los productos
start_insert_point = ' <!-- Print area start -->'
end_insert_point = ' <!-- Print area end -->'

# Encontrar la posición donde comienza el punto de inserción de inicio
start_index = html_content.find(start_insert_point) + len(start_insert_point)

# Encontrar la posición donde termina el punto de inserción de inicio
end_index = html_content.find(end_insert_point)

# Insertar todos los productos y la paginación en el HTML
updated_html = html_content[:start_index]
for page_number, page_products in enumerate(products_pages, start=1):
    row_html = ''
    for i in range(0, len(page_products), 3):  # Asegurar 2 filas de 3 productos
        row_html += f'<div class="row">{"".join(page_products[i:i+3])}</div>'
    display_style = 'block' if page_number == 1 else 'none'
    updated_html += f'''
    <div class="product-page" id="page-{page_number}" style="display: {display_style};">
        {row_html}
    </div>
    '''
updated_html += html_content[end_index:]

# Guardar el archivo actualizado
with open('/Users/ismartinez/Library/Mobile Documents/com~apple~CloudDocs/mdgt_files/site/mdgtlab_site/assets/db/printservice.html', 'w') as f:
    f.write(updated_html)
