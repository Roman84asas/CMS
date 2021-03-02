(function () {
    const addDiv = document.querySelector('#add_div');
    const close = document.querySelector('#close');
    const dataSp = document.querySelectorAll('.data_sp');
    const selectSp = document.querySelectorAll('.select_sp');

    addDiv.addEventListener('click', function (){
        const popup = document.querySelector('#hidden_popup');
        popup.style.display = 'block';
    })

    close.addEventListener('click', function (){
        const popup = document.querySelector('#hidden_popup');
        popup.style.display = 'none';
    })
    dataSp.forEach(function (element) {
        element.addEventListener('click', function () {
            dataSp.forEach(function (element) {
                element.classList.remove('active')
            })
            element.classList.add('active')
        })
    })
    selectSp.forEach(function (element) {
        element.addEventListener('click', function () {
            selectSp.forEach(function (element) {
                element.classList.remove('active')
            })
            element.classList.add('active')
        })
    })
})()