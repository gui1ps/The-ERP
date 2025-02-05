const getElement = (selector) => document.querySelector(selector);
const totalFormsInput = getElement('#id_form-TOTAL_FORMS');
const addProductButton = getElement('#add-product');
const productsTableBody = getElement('#table-products');
const productPriceDisplay = getElement('#product-selector-price');
const productTotalDisplay = getElement('#product-selector-total');
const productQuantityInput = getElement('#product-selector-quantity');
const productSelector = getElement('#product-selector');
const deleteButton= getElement('.delete-product');
const totalSUm=getElement('#id_total');

async function fetchProducts() {
    const url = 'http://127.0.0.1:8000/products/list/';
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error('Erro ao carregar produtos!');
        }
        return await response.json();
    } catch (error) {
        console.error('Erro ao buscar dados:', error.message);
        throw error;
    }
}

function populateProductSelector(products) {
    const options = products.map(product => 
        `<option data-price="${product.p_sell}" value="${product.id}">${product.name}</option>`
    ).join('');
    productSelector.innerHTML += options;
}

function updateTotalForms(signal) {
    if (signal==='+'){
        totalFormsInput.value = Number(totalFormsInput.value) + 1;
    }else if(signal==='-'){
        totalFormsInput.value = Number(totalFormsInput.value) - 1;
    }
}

function getSelectedProductOption() {
    const selectedOption = productSelector.options[productSelector.selectedIndex];
    if (!selectedOption || selectedOption.innerText==='---------') {
        alert('Selecione um produto!');
        return null;
    }
    return selectedOption.outerHTML;
}

function getSelectedProductOptionValue(){
    const selectedOption = productSelector.options[productSelector.selectedIndex];
    if (!selectedOption || selectedOption.innerText==='---------') {
        return null;
    }
    return selectedOption.innerText;
}

function getSelectedQuantity() {
    return Number(productQuantityInput.value) || 1;
}

function getSelectedPrice() {
    return parseFloat(productPriceDisplay.innerText) || 0;
}

function calculateProductTotal() {
    return getSelectedQuantity() * getSelectedPrice();
}

function updateTotalDisplay() {
    productTotalDisplay.innerText = calculateProductTotal().toFixed(2);
}

function verifyList(product) {
    let allProducts = Array.from(document.getElementsByClassName('product'));
    for (let currentProduct of allProducts) {
        let selectedOption = currentProduct.options[currentProduct.selectedIndex].text;
        if (selectedOption === product) {
            return true;
        }
    }
    return false;
}

function updateTotalSUm(){
    let productsTotalPrices=Array.from(document.getElementsByClassName('product-total-value'));
    let total=0;
    productsTotalPrices.map(e=>total+=Number(e.value));
    totalSUm.value=total;
}

function createProductRow() {
    const lastRow = productsTableBody.querySelector('tr:last-child');
    const lastFormNumber = lastRow
        ? Number(lastRow.querySelector('input[name*="-quantity"]').name.match(/\d+/)[0])
        : -1;

    const selectedProductOption = getSelectedProductOption();
    if (!selectedProductOption) return null;

    const newFormNumber = lastFormNumber + 1;

    const newRow = document.createElement('tr');
    newRow.className = 'd-flex w-100';
    newRow.innerHTML = newRow.innerHTML = `
        <td class="col-2">
            <select name="form-${newFormNumber}-product" id="id_form-${newFormNumber}-product" 
                class="form-select bg-transparent border-0 product" readonly>
                ${selectedProductOption}
            </select>
        </td>
        <td class="col-2">
            <input type="number" name="form-${newFormNumber}-quantity" value="${getSelectedQuantity()}" min="1" 
                id="id_form-${newFormNumber}-quantity" 
                class="form-control bg-transparent border-0 product-quantity" readonly>
        </td>
        <td class="col-2 d-flex align-items-center justify-content-start">
            R$
            <input type="number" name="form-${newFormNumber}-price" step="0.01" 
                id="id_form-${newFormNumber}-price" value="${getSelectedPrice()}"
                class="form-control bg-transparent border-0" readonly>
        </td>
        <td class="col-2 d-flex align-items-center justify-content-start">
            R$
            <input type="number" name="form-${newFormNumber}-total" step="0.01" 
                id="id_form-${newFormNumber}-total" value="${calculateProductTotal()}"
                class="form-control bg-transparent border-0 product-total-value" readonly>
        </td>
        <td class="col-4 text-center">
            <button class="btn btn-danger delete-prduct" onclick="this.closest('tr').remove();updateTotalForms('-');updateTotalSUm();">
                <i class="fa-solid fa-trash fa-lg"></i>
            </button>
        </td>
    `.trim();
    return newRow;
}

fetchProducts()
    .then(products => populateProductSelector(products))
    .catch(error => console.error('Erro ao carregar e preencher os produtos:', error.message));

addProductButton.addEventListener('click', (e) => {
    e.preventDefault();
    if (verifyList(getSelectedProductOptionValue())){
        alert('Produto já adicionado');
    }else{
        const newRow = createProductRow();
        if (newRow) {
            productsTableBody.appendChild(newRow)
            updateTotalForms('+');
            updateTotalSUm();
        }
    }
});

productSelector.addEventListener('change', (e) => {
    const selectedOption = e.target.options[e.target.selectedIndex];
    const price = selectedOption.getAttribute('data-price') || 0;
    productPriceDisplay.innerText = price;
    productQuantityInput.value = 1;
    updateTotalDisplay();
});

productQuantityInput.addEventListener('input', updateTotalDisplay);

