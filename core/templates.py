ESTRUCTURA_HEAD = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>MarkZero</title>
    <link rel="stylesheet" href="style.css"> 
    <link rel="icon" type="image/png" href="icon.png">
</head>
<body>
    {{MENU}}
    <div class="contenedor">
"""




ESTRUCTURA_FOOT = """
        </div>
    </body>
    <script>
        function copy(boton){
            var code = boton.nextElementSibling.innerText;
            var oldSVG = boton.innerHTML;
            
            navigator.clipboard.writeText(code).then(() => {
                boton.innerHTML = '<svg viewBox="0 0 24 24" width="16" height="16" stroke="#58a6ff" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>';
                setTimeout(() => { boton.innerHTML = oldSVG; }, 2000);
            });        
        }
    </script>
</html>
"""

ESTRUCTURA_CODE_OPEN = '<div class="container-code"><button class="btn-copy" onclick="copy(this)"><svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg></button><pre><code>'
ESTRUCTURA_CODE_CLOSE = '</code></pre></div>'
