function startsWithSequence(word, sequence) {
    const regex = new RegExp(`^${sequence}`, 'i');
    return regex.test(word);
}

function find_instance(elementObject){
    const elementObject_value=elementObject.value
    const aim_alements_class=elementObject.getAttribute('data-aim');
    const aim_alements=document.getElementsByClassName(aim_alements_class);
    const selected_aim_element=Array.from(aim_alements).find(element => startsWithSequence(element.innerText.trim().toLowerCase(),elementObject_value.trim().toLowerCase()));
    selected_aim_element.scrollIntoView({ behavior: 'smooth', block: 'center' });
    selected_aim_element.classList.add('text-primary')
    setTimeout(()=>{
        selected_aim_element.classList.remove('text-primary')
    },1000)
}
