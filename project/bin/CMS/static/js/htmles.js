(function () {
    const addDiv = document.querySelector('#add_div');
    const addBlock = document.querySelector('#add_block');
    const addHeader = document.querySelector('#add_header');
    const addSp = document.querySelector('#add_sp');
    const addSpH = document.querySelector('#add_sp_h');
    const close = document.querySelector('#close');
    const deleteBlock = document.querySelector('#delete_block');
    const closeHead = document.querySelector('#close_head');
    const deleteDiv = document.querySelector('#delete_div');
    const dataSp = document.querySelectorAll('.data_sp');
    const dataSpH = document.querySelectorAll('.data_sp_h');

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
    dataSpH.forEach(function (element) {
        element.addEventListener('click', function () {
            dataSpH.forEach(function (element) {
                element.classList.remove('active')
            })
            element.classList.add('active')
            const valueData = element.getAttribute('data-id');
            addSpH.setAttribute('data-add', valueData);
        })
    })
    addBlock.addEventListener('click', function () {
        const idHidden = document.querySelector('#id_hidden').value;
        const headerHidden = document.querySelector('#header_hidden').value;
        const titleForm = document.querySelector('#title_form').value;
        const allElements = document.querySelector('#all_elements');
        const selectSp = document.querySelectorAll('.select_sp');
        const uniqe = document.querySelector('.uniqe');

        let span = document.createElement('span');
        span.innerText = titleForm;
        if (headerHidden !== '') span.setAttribute('data-header', headerHidden);
        if (idHidden !== '') span.setAttribute('data-select', idHidden);
        span.classList.add('select_sp');

        if(!addBlock.hasAttribute('data-id-element')) {
            allElements.append(span);
            addBlock.removeAttribute('data-id-element');
            deleteBlock.removeAttribute('data-id-select');
            selectSp.forEach(function (element) {
                element.classList.remove('active')
                element.classList.remove('uniqe')
            })
        } else {
            uniqe.after(span);
            addBlock.removeAttribute('data-id-element');
            deleteBlock.removeAttribute('data-id-select');
            selectSp.forEach(function (element) {
                element.classList.remove('active')
                element.classList.remove('uniqe')
            })
        }

        selectSp.forEach(function (element) {
            element.addEventListener('click', function () {
                selectSp.forEach(function (element) {
                    element.classList.remove('active')
                    element.classList.remove('uniqe')
                })
                element.classList.add('active')
                element.classList.add('uniqe')
                if(element.hasAttribute('data-header')) {
                    let value = element.getAttribute('data-header');
                    addBlock.setAttribute('data-id-element', value)
                    deleteBlock.setAttribute('data-id-select', value)
                }
                if(element.hasAttribute('data-select')) {
                    let value = element.getAttribute('data-select');
                    addBlock.setAttribute('data-id-element', value)
                    deleteBlock.setAttribute('data-id-select', value)
                }
            })
        })
        deleteBlock.addEventListener('click', function (){
            if(deleteBlock.hasAttribute('data-id-select')) {
                $('.uniqe').remove();
            }
            selectSp.forEach(function (element) {
                element.classList.remove('active')
                element.classList.remove('uniqe')
            })
            deleteBlock.removeAttribute('data-id-select');
            addBlock.removeAttribute('data-id-element')
        })
    })
    deleteDiv.addEventListener('click', function () {
        const idHidden = document.querySelector('#id_hidden');
        const headerHidden = document.querySelector('#header_hidden');
        const titleForm = document.querySelector('#title_form');
        const contentForm = document.querySelector('#content_form');
        idHidden.value = ''
        headerHidden.value = ''
        titleForm.value = ''
        contentForm.value = ''
    })
})()
$(document).ready(function() {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const idHidden = document.querySelector('#id_hidden');
    const headerHidden = document.querySelector('#header_hidden');
    const titleForm = document.querySelector('#title_form');
    const contentForm = document.querySelector('#content_form');
    const addSp = document.querySelector('#add_sp');
    const addSpH = document.querySelector('#add_sp_h');
    const popup = document.querySelector('#hidden_popup');
    const popupH = document.querySelector('#hidden_popup_header');

    $('#add_sp').on('click',function(e){
        e.preventDefault();
        idHidden.value = ''
        headerHidden.value = ''
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
    $('#add_sp_h').on('click',function(e){
        e.preventDefault();
        idHidden.value = ''
        headerHidden.value = ''
        titleForm.value = ''
        contentForm.value = ''
        let valueData = addSpH.getAttribute('data-add');
        if (valueData) {
            $.post('/htmles/add_header/',
                {
                    'get_data': valueData,
                     csrfmiddlewaretoken: csrftoken
                },
                function(response){
                    if (response) {
                        headerHidden.value = response.data_id;
                        titleForm.value = response.data_name;
                        contentForm.value = response.data_text;
                        popupH.style.display = 'none';
                    }
                }
            );
        }
    });
    $('#create').on('click',function(e){
        e.preventDefault();
        let value = [];
        const selectSp = document.querySelectorAll('.select_sp');
        selectSp.forEach(function (element) {
            if(element.hasAttribute('data-header')) {
                value.push(element.getAttribute('data-header'))
            }
            if(element.hasAttribute('data-select')) {
                value.push(element.getAttribute('data-select'))
            }
        })
        let name = $('#name_form').val();
        let use_name = $('#id_form').val();
        let jsonString = JSON.stringify(value);
        if (value) {
            $.post('/htmles/create_html/',
                {
                    'name': name,
                    'use_name': use_name,
                    'body_numbers': jsonString,
                     csrfmiddlewaretoken: csrftoken
                },
                function(response){
                    if (response) {
                        let div = document.createElement('div');
                        div.innerText = response.data_name;
                        div.setAttribute('data-htmle', response.data_id)
                        div.classList.add('item-html');
                        div.classList.add('item');
                        $('#html_id').append(div);
                    }
                }
            );
        }
    });
    $('#update').on('click',function(e){
        e.preventDefault();
        let value = [];
        const selectSp = document.querySelectorAll('.select_sp');
        selectSp.forEach(function (element) {
            if(element.hasAttribute('data-header')) {
                value.push(element.getAttribute('data-header'))
            }
            if(element.hasAttribute('data-select')) {
                value.push(element.getAttribute('data-select'))
            }
        })
        let name = $('#top_form').val();
        let use_name = $('#id_form').val();
        let element = document.querySelector('#update')
        let id_el = element.getAttribute('data-update');
        let jsonString = JSON.stringify(value);
        if (value) {
            $.post('/htmles/update_html/',
                {
                    'id_el': id_el,
                    'name': name,
                    'use_name': use_name,
                    'body_numbers': jsonString,
                     csrfmiddlewaretoken: csrftoken
                },
                function(response){
                    if (response) {
                        alert('В обновили свой файл, можете его распечатать тепер');
                    }
                }
            );
        }
    });
    $('#writeUp').on('click',function(e){
        e.preventDefault();
        let value = [];
        const selectSp = document.querySelectorAll('.select_sp');
        selectSp.forEach(function (element) {
            if(element.hasAttribute('data-header')) {
                value.push(element.getAttribute('data-header'))
            }
            if(element.hasAttribute('data-select')) {
                value.push(element.getAttribute('data-select'))
            }
        })
        let name = $('#top_form').val();
        let use_name = $('#id_form').val();
        let element = document.querySelector('#update')
        let id_el = element.getAttribute('data-update');
        let jsonString = JSON.stringify(value);
        if (value) {
            $.post('/htmles/update_create_html/',
                {
                    'id_el': id_el,
                    'name': name,
                    'use_name': use_name,
                    'body_numbers': jsonString,
                     csrfmiddlewaretoken: csrftoken
                },
                function(response){
                    if (response) {
                        alert('Ваш файл сгенерирован');
                    }
                }
            );
        }
    });
    $('#write').on('click',function(e){
        e.preventDefault();
        let value = [];
        const selectSp = document.querySelectorAll('.select_sp');
        selectSp.forEach(function (element) {
            if(element.hasAttribute('data-header')) {
                value.push(element.getAttribute('data-header'))
            }
            if(element.hasAttribute('data-select')) {
                value.push(element.getAttribute('data-select'))
            }
        })
        let name = $('#name_form').val();
        let use_name = $('#id_form').val();
        let jsonString = JSON.stringify(value);
        if (value) {
            $.post('/htmles/write_html/',
                {
                    'name': name,
                    'use_name': use_name,
                    'body_numbers': jsonString,
                     csrfmiddlewaretoken: csrftoken
                },
                function(response){
                    if (response) {
                        let div = document.createElement('div');
                        div.innerText = response.data_name;
                        div.setAttribute('data-htmle', response.data_id)
                        div.classList.add('item-html');
                        div.classList.add('item');
                        $('#html_id').append(div);
                    }
                }
            );
        }
    });
})