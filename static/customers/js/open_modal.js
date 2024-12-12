'use strict';

const modalParts = {
    'customers': {
        title: document.getElementById('modalTitle'),
        type: document.getElementById('tipoBadge'),
        id: document.getElementById('id'),
        name: document.getElementById('nome'),
        b_date: document.getElementById('data-nascimento'),
        age: document.getElementById('idade'),
        document: document.querySelector('input[id$="document"]'),
        observations: document.getElementById('obs'),
        phone: document.getElementById('phone'),
        email: document.getElementById('email'),
        postal_code: document.getElementById('pcode'),
        street: document.getElementById('rua'),
        neighborhood: document.getElementById('neighborhood'),
        number: document.getElementById('numero'),
        city: document.getElementById('cidade'),
        state: document.getElementById('estado')
    },
    'supplier':{
        title: document.getElementById('modalTitle'),
        id: document.getElementById('id'),
        name: document.getElementById('nome'),
        document: document.querySelector('input[id$="document"]'),
        observations: document.getElementById('obs'),
        phone: document.getElementById('phone'),
        email: document.getElementById('email'),
        postal_code: document.getElementById('pcode'),
        street: document.getElementById('rua'),
        neighborhood: document.getElementById('neighborhood'),
        number: document.getElementById('numero'),
        city: document.getElementById('cidade'),
        state: document.getElementById('estado')
    },
    'products':{
        title: document.getElementById('modalTitle'),
        type: document.getElementById('tipoBadge'),
        id: document.getElementById('id'),
        name: document.getElementById('nome'),
        reference: document.getElementById('referencia'),
        unit: document.getElementById('unidade'),
        local: document.getElementById('local'),
        cost: document.getElementById('custo'),
        sell: document.getElementById('venda'),
        profit: document.getElementById('lucro')
    }
};

function get_data(tagObject) {
    const source = tagObject.getAttribute('data-source');
    let data;
    switch (source) {
        case 'customers':
            data = {
                id: tagObject.getAttribute('data-id'),
                name: tagObject.getAttribute('data-name'),
                b_date: tagObject.getAttribute('data-b_date'),
                type: tagObject.getAttribute('data-type'),
                document: tagObject.getAttribute('data-document'),
                street: tagObject.getAttribute('data-street'),
                phone: tagObject.getAttribute('data-phone'),
                email: tagObject.getAttribute('data-email'),
                number: tagObject.getAttribute('data-number'),
                neighborhood: tagObject.getAttribute('data-neighborhood'),
                city: tagObject.getAttribute('data-city'),
                state: tagObject.getAttribute('data-state'),
                postal_code: tagObject.getAttribute('data-postal_code'),
                observations: tagObject.getAttribute('data-observations')
            };
            break;
        case 'products':
            data = {
                id: tagObject.getAttribute('data-id'),
                name: tagObject.getAttribute('data-name'),
                reference: tagObject.getAttribute('data-reference'),
                local: tagObject.getAttribute('data-local'),
                pcost: tagObject.getAttribute('data-pcost'),
                psell: tagObject.getAttribute('data-psell'),
                profit: tagObject.getAttribute('data-profit'),
                unit: tagObject.getAttribute('data-unit')
            };
            break;
        case 'supplier':
            data = {
                id: tagObject.getAttribute('data-id'),
                name: tagObject.getAttribute('data-name'),
                document: tagObject.getAttribute('data-document'),
                street: tagObject.getAttribute('data-street'),
                phone: tagObject.getAttribute('data-phone'),
                email: tagObject.getAttribute('data-email'),
                number: tagObject.getAttribute('data-number'),
                neighborhood: tagObject.getAttribute('data-neighborhood'),
                city: tagObject.getAttribute('data-city'),
                state: tagObject.getAttribute('data-state'),
                postal_code: tagObject.getAttribute('data-postal_code'),
                observations: tagObject.getAttribute('data-observations')
            }
            break;
        default:
            console.error(`Unknown data source: ${source}`);
            return null;
    }
    return data;
}

function modify_modal(tagObject) {
    const source = tagObject.getAttribute('data-source');
    const data = get_data(tagObject);
    const root=modalParts[source]
    if (!data) return;

    switch (source) {
        case 'customers':
            root.title.innerText = data.name;
            root.type.innerText = data.type;
            root.id.value = data.id;
            root.name.value = data.name;
            root.b_date.value = data.b_date;
            root.age.value = calculateAge(data.b_date);
            root.document.value = data.document;
            root.observations.innerText = data.observations;
            root.email.value = data.email;
            root.phone.value = data.phone;
            root.postal_code.value = data.postal_code;
            root.street.value = data.street;
            root.neighborhood.value = data.neighborhood;
            root.number.value = data.number;
            root.city.value = data.city;
            root.state.value = data.state;
            break;
        case 'products':
            root.title.innerText = data.name;
            root.type.innerText = 'Produto'; 
            root.id.value = data.id;
            root.name.value = data.name;
            root.reference.value = data.reference;
            root.unit.value = data.unit;
            root.local.value = data.local;
            root.cost.value = data.pcost;
            root.sell.value = data.psell;
            root.profit.value = data.profit;
            break;
        case'supplier':
            root.id.value = data.id;
            root.name.value = data.name;
            root.document.value = data.document;
            root.observations.innerText = data.observations;
            root.email.value = data.email;
            root.phone.value = data.phone;
            root.postal_code.value = data.postal_code;
            root.street.value = data.street;
            root.neighborhood.value = data.neighborhood;
            root.number.value = data.number;
            root.city.value = data.city;
            root.state.value = data.state;
        default:
            break
    }
}

function open_modal(button) {
    modify_modal(button);
}

function calculateAge(birthDate) {
    const today = new Date();
    const birth = new Date(birthDate);
    let age = today.getFullYear() - birth.getFullYear();
    const monthDiff = today.getMonth() - birth.getMonth();
    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birth.getDate())) {
        age--;
    }
    return age;
}

