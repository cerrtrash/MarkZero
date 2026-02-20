![logo de markzero](public/logo2.png)
# Guía Completa de MarkZero

## Inicio

Bienvenido a la guia de MarkZero, aqui estara escrito algunas sintaxis y pasos para que tus archivos .md se conviertan en una pagina web estatica.

---

## Caracteristicas Principales


MarkZero no solo es un conversor, es un entorno de escritura estatica con:

- **Motor de Parseo Propio**:
Traduce tablas, listas anidadas, citas y bloques de codigo.
- **Boton de Copiado:**
Todos los bloques de codigo incluyen un boton funcional para copiar al portapapeles
- **Live Reload**
Los cambios se ven al instante en el navegador sin necesidad de refrescar manualmente en cada momento


---

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

---

```

# Modo Live

Para poder visualizar las ediciones o los textos de **.md** en tiempo real tienes que escribir el siguiente comando:

``` 
  python[version] main.py --dev
```

en **version** tienes que poner tu version de python en caso uses una version especifica
---



## Apariencia y Estilo

Si quieres modificar el estilo de tu pagina para que se vea mas profecional o simplemente modificar unos colores..

```
|── public/
│   ├── css/
│   │   └── style.css 
│   └── icon.png 

```
Debes modificar el archivo **style.css** a tu gusto

---

## Gestion de Paginas y Navegacion

MarkZero gestiona automaticamente la estructura de tu sitio web basandose en los archivos que creas:

1. **Creacion de paginas**: Cada archivo .md que agregues a la carpeta content se convertira en una pagina HTML individual en la carpeta dist.
2. **Sistema de Menu**: El motor genera automaticamente un menu de navegacion superior. Todos los archivos detectados en content apareceran como enlaces en este menu con el mismo nombre del archivo.
3. **Pagina de Inicio**: El archivo index.md es tratado como la pagina principal del sitio.
4. **Actualizacion Dinamica**: Si agregas un nuevo archivo o renombras uno existente, el menu se actualizara automaticamente en la siguiente compilacion o recarga del modo desarrollo.

---

## Flujo de Trabajo

Para trabajar de manera eficiente con MarkZero, sigue estos pasos:

1. **Crea o edita**: Abre o crea un archivo `.md` dentro de la carpeta `content/`.
2. **Ejecuta el servidor**: Inicia el modo desarrollo con `python main.py --dev`.
3. **Visualiza**: Abre tu navegador en `http://localhost:8000`.
4. **Escribe y guarda**: Cada vez que guardes el archivo Markdown, verás el cambio reflejado al instante sin recargar la página.
5. **Produccion**: Una vez terminado, los archivos finales listos para subir a cualquier hosting estaran en la carpeta `dist/`.

---



> Proyectado y construido por [cerrtrash](https://bydaniel.site). MarkZero es una herramienta ligera para desarrolladores que aman markdown.