const sidebar = document.getElementById('sidebar');
const sidebarButton = document.getElementById('sidebarButton');
const main=document.getElementById('main-container');

sidebarButton.addEventListener('click', () => {
    if (sidebar.style.transform === 'translateX(-100%)') {
        sidebar.style.transform = 'translateX(0)';
        sidebar.style.display='block'

    } else {
        sidebar.style.transform = 'translateX(-100%)';
        sidebar.style.display='none'
    }
});
