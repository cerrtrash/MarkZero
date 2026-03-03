![logo de markzero](logo2.png)

# MarkZero
### El motor estático más ligero para tus documentos

> **Escribe en Markdown.** Compila a HTML. Publica donde quieras.

---

## ¿Qué es MarkZero?

MarkZero no es solo otro generador de sitios estáticos. Es un **micro-ecosistema** diseñado para minimalistas que valoran la velocidad y la simplicidad.

- **Escritura Fluida**: Concéntrate en el contenido, no en las etiquetas HTML.
- **Arquitectura Limpia**: Sin dependencias pesadas ni configuraciones complejas.
- **Feedback Instantáneo**: Mira tus cambios reflejados al segundo con *Live Reload*.

Ideal para **documentación técnica**, bases de conocimientos personales o blogs minimalistas.

---

## Características Principales

### Motor de Parseo Nativo
Contamos con un motor desarrollado desde cero que interpreta la esencia de Markdown de forma eficiente:
- Encabezados jerárquicos.
- Listas inteligentes (anidadas y de tareas).
- Tablas de datos elegantes.
- Citas (Blockquotes) con estilo.
- Bloques de código con utilidades integradas.

### Portapapeles Inteligente
Cada bloque de código viene con un **botón de copiado** integrado. Un detalle pequeño que marca la diferencia en la experiencia de usuario y la productividad.

### Live Reload (Modo Dev)
Olvídate de apretar F5. Activa el modo desarrollo y observa cómo la página se actualiza sola cada vez que guardas tu archivo `.md`.

---

## Estructura del Proyecto

```text
MarkZero/
├── main.py           # El cerebro: orquestador de la build y servidor
├── content/          # Tu santuario: coloca aquí tus archivos .md
│   ├── index.md      # Página de inicio
│   └── docs.md       # Páginas adicionales
├── core/
│   ├── parser.py     # El motor de traducción Markdown -> HTML
│   └── templates.py  # Plantillas base (HEAD, FOOT, NAV)
├── public/
│   ├── css/          # Directorio de estilos (docu.css)
│   ├── js/           # Scripts del sitio (main.js)
│   └── media/        # Tus imágenes y assets
└── dist/             # El resultado: tu sitio web listo para producción
```

---

## Guía Rápida

### 1. Iniciar Desarrollo
Levanta el servidor con detección de cambios automática:
```bash
python main.py --dev
```

### 2. Estructura de Navegación
MarkZero es inteligente. Solo crea un `.md` en `content/` y aparecerá mágicamente en el menú superior. El archivo `index.md` siempre será tu página de aterrizaje.

### 3. Personalización Total
¿Quieres cambiar el look? Todo el poder está en:
```text
public/css/docu.css
```
Modifica variables, tipografías y sombras para que el sitio refleje tu identidad.

---

## Filosofía
*   **Markdown Primero**: Tu contenido es el activo más importante.
*   **Cero Fricción**: Del teclado a la web en segundos.
*   **Rendimiento**: Cargas instantáneas, código limpio.

---

##### Diseñado con pasión por [cerrtrash](https://bydaniel.site). Si te gusta MarkZero, apóyanos en [GitHub](https://github.com/cerrtrash/MarkZero).
