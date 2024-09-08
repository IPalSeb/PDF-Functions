import fitz  # PyMuPDF

def mm_to_points(mm):
    # Convierte milímetros a puntos
    return mm * 2.83465

def inches_to_points(inches):
    return inches * 72


def add_custom_margins(input_pdf, output_pdf, left_margin_mm, right_margin_mm, top_margin_mm, bottom_margin_mm):
    # Convierte la adición de márgenes de milímetros a puntos
    left_margin = inches_to_points(left_margin_mm)
    right_margin = inches_to_points(right_margin_mm)
    top_margin = inches_to_points(top_margin_mm)
    bottom_margin = inches_to_points(bottom_margin_mm)

# Abre el PDF de entrada
    document = fitz.open(input_pdf)

    # Crea un nuevo documento temporal para almacenar las páginas ajustadas
    temp_doc = fitz.open()

    # Itera sobre cada página del documento original
    for page_num in range(document.page_count):
        page = document[page_num]

        # Obtén el tamaño de la página original
        rect = page.rect

        # Calcula las nuevas dimensiones con los márgenes añadidos
        new_width = rect.width + left_margin + right_margin
        new_height = rect.height + top_margin + bottom_margin

        # Añade una nueva página al documento temporal con las dimensiones ampliadas
        new_page = temp_doc.new_page(width=new_width, height=new_height)

        # Define la posición para insertar la página original en la nueva página
        insert_rect = fitz.RecADt(left_margin, top_margin, left_margin + rect.width, top_margin + rect.height)

        # Inserta la página original en la nueva página con los márgenes añadidos
        new_page.show_pdf_page(insert_rect, document, page_num)

    # Guarda el nuevo documento con las páginas ajustadas
    temp_doc.save(output_pdf)
    temp_doc.close()
    document.close()

# Ejemplo de uso
input_pdf = "portada.pdf"
output_pdf = "portada_con_margenes.pdf"
left_margin_mm = 0.276
right_margin_mm = 0.276
top_margin_mm = 0.123
bottom_margin_mm = 0.123

add_custom_margins(input_pdf, output_pdf, left_margin_mm, right_margin_mm, top_margin_mm, bottom_margin_mm)
