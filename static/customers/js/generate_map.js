function generate_map(){
    const map=document.getElementById('mapIframe')
    const location={
        street: document.getElementById('rua').value,
        neighborhood: document.getElementById('neighborhood').value,
        number: document.getElementById('numero').value,
        city: document.getElementById('cidade').value,
        state: document.getElementById('estado').value
    }
    const src=`https://www.google.com/maps/embed/v1/place?key=AIzaSyBFw0Qbyq9zTFTd-tUY6dZWTgaQzuU17R8&q=${location.street}, ${location.number}, ${location.neighborhood},${location.city},${location.state}&zoom=15&maptype=roadmap`
    map.src=src
}