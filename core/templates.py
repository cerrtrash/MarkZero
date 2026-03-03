ESTRUCTURA_HEAD = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MarkZero</title>
    <link rel="stylesheet" href="docu.css"> 
    <link rel="icon" type="image/png" href="icon.png">
</head>
<body>
    <nav class="nav-container">
        <button class="menu-toggle" onclick="toggleMenu()">
            <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
        </button>
        <div class="menu-items" id="menu-items">
            {{MENU}}
        </div>
    </nav>
    <div class="contenedor">
"""

ESTRUCTURA_FOOT = """
        </div>
        <script src="main.js"></script>
    </body>
</html>
"""

ESTRUCTURA_CODE_OPEN = '<div class="container-code"><button class="btn-copy" onclick="copy(this)"><svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg></button><pre><code>'
ESTRUCTURA_CODE_CLOSE = '</code></pre></div>'
