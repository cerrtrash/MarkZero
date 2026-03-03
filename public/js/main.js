function copy(boton) {
    const code = boton.nextElementSibling.innerText;
    const oldSVG = boton.innerHTML;

    navigator.clipboard.writeText(code).then(() => {
        boton.innerHTML = '<svg viewBox="0 0 24 24" width="16" height="16" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>';
        boton.style.color = '#10b981';
        setTimeout(() => {
            boton.innerHTML = oldSVG;
            boton.style.color = '';
        }, 2000);
    });
}

function toggleMenu() {
    const menuItems = document.getElementById('menu-items');
    menuItems.classList.toggle('active');
}
