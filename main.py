import re 

lineasConvertidas = []
on_lista = False
on_cita = False
on_code = False

estructura_html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>MarkZero</title>
    <link rel="stylesheet" href="style.css"> 
</head>
<body>
    <div class="contenedor">
"""

estructura_html_final = """
        </div>
    </body>
</html>
"""

with open('Readme.md', 'r') as archivo:
    contenido = archivo.readlines()

for linea in contenido:
    temp = linea.strip()
    cierre = ""

    if on_code:
        if temp.startswith('```'):
            temp = "</code></pre>"
            on_code = False
        else:
            temp = temp.replace('<', '&lt;').replace('>', '&gt;') + "<br>"
    else:
        if temp.startswith('```'):
            temp = "<pre><code>"
            on_code = True
        else:
            if on_lista and (not temp or temp.startswith('#') or temp.startswith('>')):
                cierre += "</ul>"
                on_lista = False
            if on_cita and (not temp or temp.startswith('#') or temp.startswith('-')):
                cierre += "</blockquote>"
                on_cita = False

            if temp.startswith('######'):
                temp = '<h6>' + temp.lstrip('#').strip() + '</h6>'
            elif temp.startswith('#####'):
                temp = '<h5>' + temp.lstrip('#').strip() + '</h5>'
            elif temp.startswith('####'):
                temp = '<h4>' + temp.lstrip('#').strip() + '</h4>'    
            elif temp.startswith('###'):
                temp = "<h3>" + temp.lstrip('#').strip() + '</h3>'
            elif temp.startswith('##'):
                temp = "<h2>" + temp.lstrip('#').strip() + '</h2>'
            elif temp.startswith('#'):
                temp = "<h1>" + temp.lstrip('#').strip() + '</h1>'   
            elif temp.startswith('-'):
                if not on_lista:
                    temp = '<ul><li>' + temp.lstrip('-').strip() + '</li>'
                    on_lista = True
                else:
                    temp = '<li>' + temp.lstrip('-').strip() + '</li>'
            elif temp.startswith('>'):
                if not on_cita:
                    temp = '<blockquote>' + temp.lstrip('>').strip()
                    on_cita = True
                else:
                    temp = temp.lstrip('>').strip() + "<br>"
            elif not temp:
                temp = ""
            elif on_lista or on_cita:
                temp = temp + "<br>"
            
            temp = cierre + temp
            temp = re.sub(r'`(.*?)`', r'<code>\1</code>', temp)
            temp = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', temp)
            temp = re.sub(r'\*(.*?)\*', r'<i>\1</i>', temp)
            temp = re.sub(r'__(.*?)__', r'<strong>\1</strong>', temp)
            temp = re.sub(r'_(.*?)_', r'<i>\1</i>', temp)
            temp = re.sub(r'\==(.*?)==', r'<mark>\1</mark>', temp)
            temp = re.sub(r'\!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', temp)
            temp = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', temp)

    if temp:
        lineasConvertidas.append(temp)

if on_lista: lineasConvertidas.append("</ul>")
if on_cita: lineasConvertidas.append("</blockquote>")
if on_code: lineasConvertidas.append("</code></pre>")

documento = "\n".join(lineasConvertidas)
html_archivo = estructura_html + documento + estructura_html_final

try:
    with open('index.html', 'w') as html:
        html.write(html_archivo)
    print("Archivo actualizado")
except Exception as e:
    print(f"Error: {e}")