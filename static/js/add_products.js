const totalFormsInput=document.getElementById('id_form-TOTAL_FORMS')
const addProductButton=document.getElementById('add-form')
const productsTableBody=document.getElementById('table-products')
const rows=Array.from(document.querySelectorAll('tr td'))

function getNewTotalFormsValue(){
    const currentTotalFormsValue=Number(totalFormsInput.value)
    let newCurrentTotalFormsValue=currentTotalFormsValue+1
    return newCurrentTotalFormsValue
}

function getNewRowForm(){
    const lastForm=[rows[rows.length-3].innerHTML,rows[rows.length-2].innerHTML,rows[rows.length-1].innerHTML]
    const lastFormNumber = Number(lastForm[1].split("").filter(char => /\d/.test(char))[0])
    const newFormNumber=lastFormNumber+1
    const newFormProductList=lastForm[0].replace(/\d+/g,newFormNumber)
    const newFormRow = document.createElement('tr')
    newFormRow.className = 'd-flex w-100'
    newFormRow.innerHTML = `
        <td class="col-4">
            ${newFormProductList}
        </td>
        <td class="col-4">
            <input type="number" name="form-${newFormNumber}-quantity" value="1" min="0" 
                id="id_form-${newFormNumber}-quantity" 
                class="form-control border-primary bg-transparent">
        </td>
        <td class="col-4">
            <input type="number" name="form-${newFormNumber}-price" step="0.01" 
                id="id_form-${newFormNumber}-price" 
                class="form-control border-primary bg-transparent" disabled="disabled">
        </td>
    `.trim();
    return(newFormRow)
}


addProductButton.addEventListener('click',(e)=>{
    e.preventDefault()
    totalFormsInput.value=getNewTotalFormsValue()
    productsTableBody.appendChild(getNewRowForm())
})
