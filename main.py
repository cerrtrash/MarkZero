import os
import shutil
import time
import argparse
from threading import Thread
from http.server import SimpleHTTPRequestHandler, HTTPServer
from functools import partial
from core.parser import MarkDownParser
from core.templates import ESTRUCTURA_HEAD, ESTRUCTURA_FOOT

LAST_BUILD_TIME = time.time()
DEV_MODE = False

def build(clean=True):
    global LAST_BUILD_TIME
    LAST_BUILD_TIME = time.time()
    
    folder_input = 'content'
    folder_output = 'dist'
    public_dir = 'public'
    
    if clean and os.path.exists(folder_output):
        shutil.rmtree(folder_output)
    
    os.makedirs(folder_output, exist_ok=True)
    print("Generando las paginas....")
    
    menu_html = '<nav class="menu">'
    paginas = [f for f in os.listdir(folder_input) if f.endswith('.md')]

    for p in paginas:
        nombre = p.replace('.md', '')
        display_name = "Inicio" if nombre.lower() == "index" else nombre
        enlace = p.replace('.md', '.html')
        menu_html += f'<a href="{enlace}">{display_name}</a>'
    menu_html += '</nav>'

    content_menu = ESTRUCTURA_HEAD.replace('{{MENU}}', menu_html)

    if os.path.exists(public_dir):
        for item in os.listdir(public_dir):
            s = os.path.join(public_dir, item)
            d = os.path.join(folder_output, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
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
            
            if DEV_MODE:
                print(f"  [Dev] Inyectando script de recarga en {filename}")
                reload_script = """
<script>
    let lastBuild = null;
    async function check() {
        try {
            const res = await fetch('/live-reload-check');
            const time = await res.text();
            if (lastBuild && lastBuild !== time) location.reload();
            lastBuild = time;
        } catch(e) {}
    }
    setInterval(check, 1000);
</script>"""
                contenido_final = contenido_final.replace('</body>', f'{reload_script}\n</body>')

            with open(path_output, 'w', encoding='utf-8') as f:
                f.write(contenido_final)
                
            print(f"Generado: {path_output}")


class LiveReloadHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='dist', **kwargs)

    def do_GET(self):
        if self.path == '/live-reload-check':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(str(LAST_BUILD_TIME).encode())
        else:
            super().do_GET()

def serve(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, LiveReloadHandler)
    print(f"Servidor corriendo en http://localhost:{port}")
    httpd.serve_forever()

def watch():
    last_mtimes = {}
    print("Vigilando cambios en 'content/' y 'public/'...")
    while True:
        changed = False
        for folder in ['content', 'public']:
            if not os.path.exists(folder): continue
            for root, dirs, files in os.walk(folder):
                for f in files:
                    path = os.path.join(root, f)
                    try:
                        mtime = os.path.getmtime(path)
                        if path not in last_mtimes or last_mtimes[path] < mtime:
                            last_mtimes[path] = mtime
                            changed = True
                    except FileNotFoundError:
                        continue
        
        if changed:
            print(' Cambio detectado. Actualizando...')
            build(clean=False)
        time.sleep(1)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MarkZero Engine")
    parser.add_argument('--build', action = 'store_true', help="Genera el sitio una sola vez")
    parser.add_argument('--dev', action='store_true', help="Modo desarrollo: Auto build y servidor local")

    args = parser.parse_args()

    if args.dev:
        DEV_MODE = True
        build(clean=True)
        server_thread = Thread(target=serve, daemon=True)
        server_thread.start()
        watch()
    elif args.build:
        build(clean=True)
    else:
        print("\n Tip: Usa 'python main.py --dev' para el modo live")