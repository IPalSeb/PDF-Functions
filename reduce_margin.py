import fitz  # PyMuPDF

def mm_to_points(mm):
    # Convierte milímetros a puntos
    return mm * 2.83465

def reduce_pdf_margins(input_pdf, output_pdf, margin_reduction_mm):
    # Convierte la reducción de margen de milímetros a puntos
    margin_reduction = mm_to_points(margin_reduction_mm)

    # Abre el PDF
    document = fitz.open(input_pdf)

    # Itera sobre cada página del documento
    for page_num in range(document.page_count):
        page = document[page_num]

        # Obtén el tamaño de la página (bounding box)
        rect = page.rect

        # Calcula las nuevas dimensiones reduciendo los márgenes
        new_rect = fitz.Rect(
            rect.x0 + margin_reduction,
            rect.y0 + margin_reduction,
            rect.x1 - margin_reduction,
            rect.y1 - margin_reduction
        )

        # Recorta la página a las nuevas dimensiones
        page.set_cropbox(new_rect)

    # Guarda el nuevo archivo PDF con los márgenes reducidos
    document.save(output_pdf)
    document.close()

# Ejemplo de uso
input_pdf = "libro.pdf"
output_pdf = "libro_reducido.pdf"
margin_reduction_mm = 9.6

reduce_pdf_margins(input_pdf, output_pdf, margin_reduction_mm)
