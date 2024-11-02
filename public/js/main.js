let all_burguers = {}
// requisição à API carrinho, para comunicação  da API com o html
const add_carrinho = (lanche_name) => {
    $.ajax({
        url:`${host}/api/v1.0/carrinho`,
        method: 'POST',
        headers:{
                    "Authorization": "123",
                    'Content-Type': 'application/json',
                    // 'Accept': 'application/json',
                },
        data: JSON.stringify(all_burguers[lanche_name]),
        success: fire_toast(`${lanche_name} adicionado no carrinho`)
    })
}

// Fazendo a requisição à API Burgers usando AJAX method GET
$(document).ready(function(){
    // const host = 'http://192.168.0.201:3001'

    $.ajax({
        url:`${host}/api/v1.0/burgers`,
        method: 'GET',
        headers:{"Authorization": "123"},
        success:function(data, status){
            all_burguers = data

            Object.entries(data).forEach(([key, value]) => {
                const lanche_name = key
                const image = value['image']
                const ingredients = value['ingredients']
                const id = `${lanche_name.replace(' ', '_')}-price`

            // adicionando as informações no card e depois dentro do caroussel
                $('#carousel').append(`
                    <article onClick="add_carrinho('${lanche_name}')">
                        <h3>${lanche_name}</h3>
                        <img src="${host}${image}">
                        <p>Ingredientes: ${ingredients.join(', ')}</p>
                        <p id="${id}"></p>
                    </article>
                `);
            // Fazendo a requisição à API Calculate usando AJAX, method POST
                $.ajax({
                    url:`${host}/api/v1.0/calculate`,
                    headers:{
                        "Authorization": "123",
                        'Content-Type': 'application/json',
                        // 'Accept': 'application/json',
                    },
                    data: JSON.stringify({name: lanche_name}),
                    method: 'POST',
                    success: response => {
                        all_burguers[lanche_name].price = response
                        all_burguers[lanche_name].name = lanche_name

                        return $(`#${id}`).text(`Apartir de R$ ${response.originalPrice}`)},
                    error: error => console.error(error)
                })

            })
    }});
});