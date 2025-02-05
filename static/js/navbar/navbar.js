const sidebar = document.getElementById('sidebar');
const sidebarButton = document.getElementById('sidebarButton');
sidebarButton.addEventListener('click', () => {
    if (sidebar.style.width=='0px') {
        sidebar.style.width='300px';

    } else {
        sidebar.style.width = '0px';
    }
});
