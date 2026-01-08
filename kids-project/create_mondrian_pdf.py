#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing, Rect
from reportlab.graphics import renderPDF

# Colores de Mondrian
MONDRIAN_RED = colors.HexColor('#E03C31')
MONDRIAN_BLUE = colors.HexColor('#0C5DA5')
MONDRIAN_YELLOW = colors.HexColor('#FFC300')
MONDRIAN_BLACK = colors.HexColor('#1a1a1a')

def create_mondrian_grid():
    """Crea una cuadrícula al estilo Mondrian para actividad"""
    d = Drawing(400, 400)
    
    # Grosor de las líneas
    line_width = 4
    
    # Rectángulos con colores de Mondrian
    rectangles = [
        # Fila 1
        (0, 300, 150, 100, colors.white),
        (150, 300, 100, 100, MONDRIAN_RED),
        (250, 300, 150, 100, colors.white),
        
        # Fila 2
        (0, 200, 100, 100, MONDRIAN_BLUE),
        (100, 200, 150, 100, colors.white),
        (250, 200, 150, 100, MONDRIAN_YELLOW),
        
        # Fila 3
        (0, 100, 150, 100, colors.white),
        (150, 100, 250, 100, colors.white),
        
        # Fila 4
        (0, 0, 100, 100, MONDRIAN_YELLOW),
        (100, 0, 150, 100, colors.white),
        (250, 0, 150, 100, MONDRIAN_BLUE),
    ]
    
    # Dibujar rectángulos
    for x, y, width, height, color in rectangles:
        rect = Rect(x, y, width, height)
        rect.fillColor = color
        rect.strokeColor = MONDRIAN_BLACK
        rect.strokeWidth = line_width
        d.add(rect)
    
    return d

def create_activity_grid():
    """Crea una cuadrícula vacía para que el niño coloree"""
    d = Drawing(350, 350)
    
    line_width = 3
    cell_size = 70
    
    # Crear cuadrícula 5x5
    for i in range(5):
        for j in range(5):
            x = i * cell_size
            y = j * cell_size
            rect = Rect(x, y, cell_size, cell_size)
            rect.fillColor = colors.white
            rect.strokeColor = MONDRIAN_BLACK
            rect.strokeWidth = line_width
            d.add(rect)
    
    return d

def create_pdf():
    import os
    # Create outputs directory if it doesn't exist
    os.makedirs("outputs", exist_ok=True)

    # Crear documento
    doc = SimpleDocTemplate("outputs/piet_mondrian.pdf",
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )
    
    # Estilos
    styles = getSampleStyleSheet()
    
    # Estilo para el título principal
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=MONDRIAN_RED,
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    # Estilo para subtítulos
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=18,
        textColor=MONDRIAN_BLUE,
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    # Estilo para texto normal
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=10,
        alignment=TA_JUSTIFY,
        leading=16
    )
    
    # Estilo para curiosidades
    fact_style = ParagraphStyle(
        'FactStyle',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=8,
        leftIndent=15,
        bulletIndent=0,
        leading=14
    )
    
    # Contenido
    story = []
    
    # Portada
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph("🎨 Piet Mondrian 🎨", title_style))
    story.append(Paragraph("El Pintor de las Líneas y Colores", subtitle_style))
    story.append(Spacer(1, 0.5*cm))
    
    # Añadir cuadrícula de ejemplo de Mondrian
    story.append(create_mondrian_grid())
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("<i>Trabajo escolar - 3º de Primaria</i>",
                          ParagraphStyle('Italic', parent=styles['Normal'],
                                       fontSize=10, alignment=TA_CENTER, textColor=colors.grey)))
    
    story.append(PageBreak())
    
    # Sección 1: ¿Quién fue Piet Mondrian?
    story.append(Paragraph("¿Quién fue Piet Mondrian?", subtitle_style))
    
    intro_text = """
    <b>Piet Mondrian</b> fue un pintor muy especial de los <b>Países Bajos</b> (también llamado Holanda). 
    Nació hace muchísimo tiempo, en el año <b>1872</b>, y vivió hasta 1944.
    <br/><br/>
    Lo más increíble de Mondrian es que pintaba de una manera <b>única en el mundo</b>: 
    usaba solo <b>líneas negras rectas</b> y los colores <b>rojo, azul y amarillo</b>, 
    además de blanco y negro. ¡Imagínate hacer cuadros famosísimos con solo líneas rectas y tres colores!
    <br/><br/>
    Sus cuadros parecen muy simples, pero son el resultado de mucho trabajo y pensamiento. 
    Mondrian creía que el arte debía mostrar la <b>armonía perfecta</b> del universo usando 
    las formas y colores más básicos.
    """
    story.append(Paragraph(intro_text, normal_style))
    story.append(Spacer(1, 0.5*cm))
    
    # Sección 2: Curiosidades
    story.append(Paragraph("🌟 Curiosidades Súper Divertidas 🌟", subtitle_style))
    
    facts = [
        ("🌳 <b>Al principio pintaba árboles</b>", 
         "Cuando Mondrian era joven, pintaba árboles y paisajes normales, como muchos otros pintores. "
         "Pero con el tiempo, empezó a hacer los árboles cada vez más simples, hasta que solo quedaron... ¡líneas! "
         "Así descubrió su estilo único."),
        
        ("🎵 <b>Le encantaba el jazz y bailar</b>", 
         "Mondrian amaba la música jazz y era muy buen bailarín. Decía que sus cuadros eran como música, "
         "pero con colores. Cuando veas sus líneas y cuadrados de colores, piensa en una canción alegre."),
        
        ("🎨 <b>Solo 3 colores + blanco y negro</b>", 
         "Mondrian decidió usar SOLO rojo, azul y amarillo (los colores primarios). "
         "También usaba blanco, negro y a veces gris. ¿Por qué? Porque creía que estos colores "
         "eran los más puros y perfectos. ¡Con solo 5 colores creó obras maestras!"),
        
        ("🏙️ <b>Nueva York lo inspiró mucho</b>", 
         "Cuando Mondrian fue a vivir a Nueva York, quedó fascinado por la ciudad llena de rascacielos, "
         "luces y movimiento. Uno de sus últimos cuadros se llama 'Broadway Boogie Woogie' y parece "
         "las calles de Nueva York vistas desde arriba."),
        
        ("📏 <b>Usaba regla y cinta adhesiva</b>", 
         "Para hacer sus líneas tan perfectamente rectas, Mondrian usaba una regla y cinta adhesiva especial. "
         "¡Era súper perfeccionista! A veces tardaba muchos meses en terminar un solo cuadro porque "
         "quería que todo estuviera perfecto."),
        
        ("✨ <b>Creó un estilo nuevo llamado 'De Stijl'</b>", 
         "El estilo de Mondrian también se llama 'Neoplasticismo' o 'De Stijl' (que significa 'El Estilo' en holandés). "
         "¡Fue tan especial que hoy en día vemos su influencia en todas partes: en muebles, ropa, diseño de edificios "
         "y hasta en videojuegos!"),
    ]
    
    for emoji_title, text in facts:
        story.append(Paragraph(emoji_title, fact_style))
        story.append(Paragraph(text, fact_style))
        story.append(Spacer(1, 0.3*cm))
    
    story.append(PageBreak())
    
    # Sección 3: Línea de tiempo
    story.append(Paragraph("📅 La Vida de Mondrian en 5 Momentos 📅", subtitle_style))
    story.append(Spacer(1, 0.3*cm))

    # Estilo para celdas de la tabla
    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontSize=9,
        leading=11,
        fontName='Helvetica'
    )

    timeline_data = [
        [Paragraph('1872', table_cell_style),
         Paragraph('Nace en Holanda 🇳🇱', table_cell_style),
         Paragraph('Piet Mondrian nació el 7 de marzo en Amersfoort, una ciudad de los Países Bajos. '
                  'Su familia era muy religiosa y su padre era maestro de dibujo.', table_cell_style)],

        [Paragraph('1911', table_cell_style),
         Paragraph('Se muda a París 🗼', table_cell_style),
         Paragraph('Mondrian se fue a vivir a París, Francia, donde conoció a otros artistas modernos. '
                  'Allí empezó a cambiar su manera de pintar y hacer las cosas más simples.', table_cell_style)],

        [Paragraph('1917', table_cell_style),
         Paragraph('Crea su estilo único', table_cell_style),
         Paragraph('Junto con otros artistas fundó el movimiento "De Stijl" y empezó a pintar solo con '
                  'líneas rectas y los tres colores primarios. ¡Nació el estilo Mondrian!', table_cell_style)],

        [Paragraph('1940', table_cell_style),
         Paragraph('Viaja a Nueva York 🗽', table_cell_style),
         Paragraph('Durante la Segunda Guerra Mundial, Mondrian se mudó a Nueva York. '
                  'La ciudad moderna lo inspiró muchísimo y pintó algunas de sus obras más famosas.', table_cell_style)],

        [Paragraph('1944', table_cell_style),
         Paragraph('Su legado continúa ✨', table_cell_style),
         Paragraph('Mondrian murió en Nueva York, pero su arte sigue siendo super famoso. '
                  'Sus cuadros están en los museos más importantes del mundo y valen millones de euros.', table_cell_style)],
    ]

    # Crear tabla para la línea de tiempo
    timeline_table = Table(timeline_data, colWidths=[2.5*cm, 4*cm, 10*cm])
    timeline_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), MONDRIAN_YELLOW),
        ('BACKGROUND', (1, 0), (1, -1), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, -1), MONDRIAN_BLACK),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 2, MONDRIAN_BLACK),
        ('ROWBACKGROUNDS', (2, 0), (2, -1), [colors.white, colors.lightgrey]),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))

    story.append(timeline_table)
    story.append(Spacer(1, 0.5*cm))
    
    # Sección 4: Obras famosas
    story.append(Paragraph("🖼️ Sus Cuadros Más Famosos 🖼️", subtitle_style))
    
    famous_works = """
    Estos son algunos de los cuadros más conocidos de Piet Mondrian:
    <br/><br/>
    <b>• "Composición con Rojo, Azul y Amarillo" (1930)</b><br/>
    Es uno de sus cuadros más famosos. Tiene rectángulos de colores separados por líneas negras gruesas.
    <br/><br/>
    <b>• "Broadway Boogie Woogie" (1942-1943)</b><br/>
    ¡Este cuadro parece las calles de Nueva York vistas desde el cielo! Usó pequeños cuadraditos de colores 
    para mostrar el ritmo y la energía de la ciudad.
    <br/><br/>
    <b>• "Composición con Amarillo, Azul y Rojo" (1937-1942)</b><br/>
    Otro ejemplo perfecto de su estilo: equilibrio perfecto entre colores y líneas.
    <br/><br/>
    <b>💡 Dato curioso:</b> Los cuadros de Mondrian son tan famosos que han inspirado ropa, zapatos, 
    edificios e incluso decoraciones de pasteles. ¡Su arte está por todas partes!
    """
    story.append(Paragraph(famous_works, normal_style))
    story.append(Spacer(1, 0.5*cm))
    
    # Sección 5: Actividad
    story.append(PageBreak())
    story.append(Paragraph("🎨 ¡Ahora te toca a ti! 🎨", subtitle_style))
    story.append(Paragraph("<b>Actividad: Crea tu propio cuadro al estilo Mondrian</b>", 
                          ParagraphStyle('ActivityTitle', parent=styles['Normal'], 
                                       fontSize=13, textColor=MONDRIAN_RED, 
                                       spaceAfter=10, fontName='Helvetica-Bold')))
    
    activity_instructions = """
    <b>Instrucciones:</b>
    <br/>
    1. Usa solo lápices o rotuladores de colores <b>ROJO, AZUL y AMARILLO</b>
    <br/>
    2. Colorea algunos cuadrados (no todos, ¡deja algunos en blanco!)
    <br/>
    3. Recuerda: Mondrian dejaba mucho espacio blanco en sus cuadros
    <br/>
    4. Puedes colorear los cuadrados que quieras, no hay una forma correcta o incorrecta
    <br/>
    5. ¡Diviértete creando tu propia obra de arte!
    """
    story.append(Paragraph(activity_instructions, normal_style))
    story.append(Spacer(1, 0.5*cm))
    
    # Añadir cuadrícula para colorear
    story.append(create_activity_grid())
    story.append(Spacer(1, 0.5*cm))
    
    # Actividad adicional
    story.append(PageBreak())
    story.append(Paragraph("✏️ Más Actividades ✏️", subtitle_style))
    
    more_activities = """
    <b>1. Dibuja tu propia composición Mondrian</b>
    <br/>
    En una hoja en blanco, dibuja líneas rectas con una regla (horizontales y verticales). 
    Luego colorea algunos espacios con rojo, azul o amarillo. ¡Deja otros en blanco!
    <br/><br/>
    <b>2. Busca el estilo Mondrian en tu vida diaria</b>
    <br/>
    ¿Puedes encontrar cosas a tu alrededor que parezcan cuadros de Mondrian? 
    Tal vez una ventana, un edificio, o un diseño en la ropa. ¡Haz una lista!
    <br/><br/>
    <b>3. Crea una historia</b>
    <br/>
    Imagina que eres Mondrian viviendo en Nueva York. ¿Qué verías? ¿Qué te inspiraría? 
    Escribe un pequeño cuento o dibuja un cómic.
    <br/><br/>
    <b>4. Investiga más</b>
    <br/>
    Puedes buscar en internet (con ayuda de un adulto) imágenes de los cuadros de Mondrian. 
    También hay videos que muestran cómo pintaba. ¡Es muy interesante!
    """
    story.append(Paragraph(more_activities, normal_style))
    story.append(Spacer(1, 0.5*cm))
    
    # Conclusión
    story.append(Paragraph("🌟 Para recordar 🌟", subtitle_style))
    
    conclusion = """
    <b>Piet Mondrian nos enseñó que:</b>
    <br/><br/>
    • El arte no siempre tiene que ser realista o complicado
    <br/>
    • A veces, lo más simple puede ser lo más hermoso
    <br/>
    • Con solo tres colores y líneas rectas puedes crear algo increíble
    <br/>
    • El arte puede estar en todas partes: en la música, en las ciudades, en nuestra vida diaria
    <br/>
    • Ser diferente y tener tu propio estilo es algo maravilloso
    <br/><br/>
    <i>"La posición del artista es humilde. Esencialmente es un canal."</i> - Piet Mondrian
    <br/><br/>
    <b>¡Esperamos que hayas disfrutado aprendiendo sobre Piet Mondrian!</b> 
    Ahora ya sabes por qué sus cuadros de líneas y colores son tan famosos en todo el mundo.
    """
    story.append(Paragraph(conclusion, normal_style))
    
    # Construir PDF
    doc.build(story)
    print("PDF creado exitosamente: outputs/piet_mondrian.pdf")

if __name__ == "__main__":
    create_pdf()
