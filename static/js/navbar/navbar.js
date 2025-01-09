const sidebar = document.getElementById('sidebar');
const sidebarButton = document.getElementById('sidebarButton');
const main=document.getElementById('main-container');

sidebarButton.addEventListener('click', () => {
    if (sidebar.style.width=='0px') {
        sidebar.style.width='20%';

    } else {
        sidebar.style.width = '0px';
    }
});
