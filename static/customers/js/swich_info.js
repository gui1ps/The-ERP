'use strict'

const sections = {
    info: document.getElementById('info'),
    contacts: document.getElementById('contacts'),
    local: document.getElementById('local')
};

const buttons = {
    activate_info: document.getElementById('activate_info'),
    activate_contacts: document.getElementById('activate_contacts'),
    activate_local: document.getElementById('activate_local')
};

const close_modal_btn=document.getElementById('close-modal-btn')

function showSection(activeSection) {
    for (const section in sections) {
        if (section === activeSection) {
            sections[section].classList.remove('d-none');
            sections[section].classList.add('d-block');
        } else {
            sections[section].classList.add('d-none');
            sections[section].classList.remove('d-block');
        }
    }
}

buttons.activate_info.addEventListener("click", () => showSection('info'));
buttons.activate_contacts.addEventListener("click", () => showSection('contacts'));
buttons.activate_local.addEventListener("click", () => showSection('local'));
close_modal_btn.addEventListener("click", ()=> showSection('info'));
