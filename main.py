import os
import shutil
from core.parser import MarkDownParser
from core.templates import ESTRUCTURA_HEAD, ESTRUCTURA_FOOT

def main():
    menu_html = '<nav class="menu">'
    folder_input = 'content'
    folder_output = 'dist'
    public_dir = 'public'
    paginas = [f for f in os.listdir(folder_input) if f.endswith('.md')]

    os.makedirs(folder_output, exist_ok=True)

    for p in paginas:
        nombre = p.replace('.md', '')
        enlace = p.replace('.md', '.html')
        menu_html += f'<a href="{enlace}">{nombre}</a>'
    menu_html += '</nav>'

    content_menu = ESTRUCTURA_HEAD.replace('{{MENU}}', menu_html)

    if os.path.exists(public_dir):
        for item in os.listdir(public_dir):
            s = os.path.join(public_dir, item)
            d = os.path.join(folder_output, item)
            if os.path.isdir(s):
                if os.path.exists(d): shutil.rmtree(d)
                shutil.copytree(s, d)
            else:
                shutil.copy2(s, d)
        
        css_file = os.path.join(folder_output, 'css', 'style.css')
        if os.path.exists(css_file):
            shutil.copy2(css_file, os.path.join(folder_output, 'style.css'))

    for filename in os.listdir(folder_input):
        if filename.endswith('.md'):
            path_input = os.path.join(folder_input, filename)
            path_output = os.path.join(folder_output, filename.replace('.md', '.html'))
            
            parser = MarkDownParser()
            lineas_resultantes = []

            with open(path_input, 'r', encoding='utf-8') as f:
                for linea in f:
                    resultado = parser.parse_line(linea)
                    if resultado:
                        lineas_resultantes.append(resultado)
            
            contenido_final = content_menu + "\n".join(lineas_resultantes) + ESTRUCTURA_FOOT
            
            with open(path_output, 'w', encoding='utf-8') as f:
                f.write(contenido_final)
                
            print(f"Generado: {path_output}")

if __name__ == "__main__":
    main()