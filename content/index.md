![logo de markzero](logo2.png)


## Genera sitios web estáticos usando solo Markdown

MarkZero es un entorno minimalista que convierte archivos `.md` en páginas HTML listas para producción.

Escribe en Markdown.  
Compila a HTML.  
Publica en cualquier hosting.

---

## ¿Qué es MarkZero?

MarkZero no es solo un conversor.

Es un pequeño ecosistema diseñado para:

- Escribir contenido rápidamente
- Generar sitios estáticos organizados
- Mantener una estructura limpia
- Visualizar cambios en tiempo real

Ideal para documentación técnica, blogs personales o proyectos simples.

---

## Características Principales

### Motor de Parseo Propio

Incluye un motor desarrollado desde cero que interpreta:

- Encabezados
- Listas anidadas
- Tablas
- Citas
- Bloques de código
- Separadores

No depende de frameworks pesados.

---

### Botón de Copiado en Bloques de Código

Todos los bloques de código incluyen un botón funcional que permite copiar el contenido directamente al portapapeles.

Especialmente útil para documentación técnica.

---

### Live Reload

Modo desarrollo con recarga automática.

Cada vez que guardas un archivo `.md`, el navegador se actualiza automáticamente sin necesidad de refrescar manualmente.

---

## Estructura del Proyecto

# Estructura del proyecto
```
  MarkZero/
├── main.py --> El archivo principal
├── content/ ---> Carpeta donde deben ir tus archivos .md
│   ├── index.md
│   └── prueba.md
├── core/
│   ├── parser.py --> Aqui se encuentran el motor para traducir a html
│   └── templates.py --> Aqui se define la estructura del sitio (cabeceras, pie de pagina, etc)
├── public/
│   ├── css/
│   │   └── style.css --> Puedes modificar el estilo de las paginas a tu gusto
│   └── icon.png 
└── dist/ ---> Esta carpeta es tu build con los .md traducidos a html
    ├── index.html 
    ├── prueba.html
    └── style.css

```

## Modo Desarrollo

```bash
python main.py --dev
```

Si usas una versión específica:

```bash
python3.11 main.py --dev
```

Luego abre:

```
http://localhost:8000
```

---

## Sistema de Navegación Automático

MarkZero detecta automáticamente los archivos dentro de `content/` y:

1. Genera una página HTML por cada archivo `.md`.
2. Construye el menú de navegación superior automáticamente.
3. Trata `index.md` como la página principal.
4. Actualiza el menú al agregar o renombrar archivos.

---

## Personalización Visual

Edita:

```bash
public/css/style.css
```

Puedes modificar:

- Colores
- Tipografía
- Layout
- Espaciado
- Estilos de código

---

## Flujo de Trabajo

1. Crea o edita un archivo `.md` dentro de `content/`.
2. Ejecuta el servidor en modo desarrollo.
3. Guarda el archivo.
4. Visualiza los cambios automáticamente.
5. Sube la carpeta `dist/` a cualquier hosting estático.

---

## Filosofía

- Simplicidad
- Control
- Rendimiento
- Markdown como fuente única de verdad

---

###### Proyectado y construido por [cerrtrash](https://bydaniel.site). MarkZero es una herramienta ligera para desarrolladores que aman markdown. Regalame una estrellita en github -> [MarkZero](https://github.com/cerrtrash/MarkZero) 
