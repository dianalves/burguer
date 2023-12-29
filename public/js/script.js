document.addEventListener('DOMContentLoaded', function () {
    const fixedMenuButton = document.getElementById('menu_collapse');
    const menu = document.getElementById('menu-fixed');

    fixedMenuButton.addEventListener('click', function () {
        menu.classList.toggle('open');
    });
});
