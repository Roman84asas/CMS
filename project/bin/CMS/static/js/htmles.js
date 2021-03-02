(function () {
    const addDiv = document.querySelector('#add_div');
    const addHeader = document.querySelector('#add_header');
    const addSp = document.querySelector('#add_sp');
    const close = document.querySelector('#close');
    const closeHead = document.querySelector('#close_head');
    const dataSp = document.querySelectorAll('.data_sp');
    const selectSp = document.querySelectorAll('.select_sp');

    addDiv.addEventListener('click', function (){
        const popup = document.querySelector('#hidden_popup');
        popup.style.display = 'block';
    })
    addHeader.addEventListener('click', function (){
        const popup = document.querySelector('#hidden_popup_header');
        popup.style.display = 'block';
    })

    close.addEventListener('click', function (){
        const popup = document.querySelector('#hidden_popup');
        popup.style.display = 'none';
    })
    closeHead.addEventListener('click', function (){
        const popup = document.querySelector('#hidden_popup_header');
        popup.style.display = 'none';
    })
    dataSp.forEach(function (element) {
        element.addEventListener('click', function () {
            dataSp.forEach(function (element) {
                element.classList.remove('active')
            })
            element.classList.add('active')
            const valueData = element.getAttribute('data-id');
            addSp.setAttribute('data-add', valueData);
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
$(document).ready(function() {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const idHidden = document.querySelector('#id_hidden');
    const titleForm = document.querySelector('#title_form');
    const contentForm = document.querySelector('#content_form');
    const addSp = document.querySelector('#add_sp');
    const popup = document.querySelector('#hidden_popup');

    $('#add_sp').on('click',function(e){
        e.preventDefault();
        idHidden.value = ''
        titleForm.value = ''
        contentForm.value = ''
        let valueData = addSp.getAttribute('data-add');
        if (valueData) {
            $.post('/htmles/add_data/',
                {
                    'get_data': valueData,
                     csrfmiddlewaretoken: csrftoken
                },
                function(response){
                    if (response) {
                        idHidden.value = response.data_id;
                        titleForm.value = response.data_name;
                        contentForm.value = response.data_text;
                        popup.style.display = 'none';
                    }
                }
            );
        }
    });
})