import pandas as pd

# Cargar los datos desde el archivo Excel
df = pd.read_excel('/Users/ismartinez/Sites/mdgt_finalsite/assets/db/mdgtlab_productos.xlsx')

# Función para generar HTML para cada producto
def generate_product_html(row):
    return f'''
        <div class="col-lg-4 col-md-6 sm-6 {row['filter_id']}">
            <div class="swiper-slide align-items-center">
                <div class="latest-blog__item-slide-inner align-items-center">
                    <div class="latest-blog__item-media align-items-center">
                        <a href="{row['product_link']}" target="_blank">
                            <img src="{row['image_path1']}" alt="{row['product_sectionalt']}" class="img-fluid">
                        </a>
                    </div>
                    <div class="latest-blog__item-text align-items-center text-center">
                        <div class="latest-blog__item-text-meta d-flex flex-column align-items-center">
                            <div class="latest-blog__item-text-meta-calender align-items-center">
                                <a href="{row['product_link']}" target="_blank">
                                    <h4>{row['product_name']}</h4>
                                  
                                </a>
                            </div>
                        </div>
                        <div class="latest-blog__item-text-bottom" style="text-align: justify;">
                            <p>{row['meta_description']}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    '''

# Generar el HTML para todos los productos
all_products_html = ''.join([generate_product_html(row) for index, row in df.iterrows()])

# Leer el archivo HTML original
with open('/Users/ismartinez/Sites/mdgt_finalsite/assets/db/print.html', 'r') as file:
    html_content = file.read()

# Punto de inserción para los productos
start_insert_point = '<!-- Print area start -->'
end_insert_point = '<!-- Print area end -->'

# Encontrar la posición donde comienza el punto de inserción de inicio
start_index = html_content.find(start_insert_point) + len(start_insert_point)

# Encontrar la posición donde termina el punto de inserción de inicio
end_index = html_content.find(end_insert_point)

# Insertar todos los productos en el HTML
updated_html = html_content[:start_index] + all_products_html + html_content[end_index:]

# Guardar el archivo actualizado con un nuevo nombre
with open('/Users/ismartinez/Sites/mdgt_finalsite/assets/db/print_new.html', 'w') as f:
    f.write(updated_html)
