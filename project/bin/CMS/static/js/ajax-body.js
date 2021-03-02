$(document).ready(function() {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const itemBody = document.querySelectorAll('.item-body');
    const itemDive = document.querySelectorAll('.item-dive');
    const addSp = document.querySelector('#del-bodys');
    const diveSp = document.querySelector('#del-dive');

    $('#del-bodys').on('click',function(e){
        e.preventDefault();
        let valueData = addSp.getAttribute('data-bodys');
        if (valueData) {
            $.post('/bodys/delete_id/',
                {
                    'id_delete': valueData,
                    csrfmiddlewaretoken: csrftoken
                },
                function(response){
                    if (response.msg) {
                        itemBody.forEach(function (element){
                            const valueDataId = element.getAttribute('data-bodys');
                            if (valueDataId == valueData) element.remove();
                        })
                    }
                }
            );
        }
    });
    $('#del-dive').on('click',function(e){
        e.preventDefault();
        let valueData = diveSp.getAttribute('data-dive');
        if (valueData) {
            $.post('/dives/delete_id/',
                {
                    'id_delete': valueData,
                    csrfmiddlewaretoken: csrftoken
                },
                function(response){
                    if (response.msg) {
                        itemDive.forEach(function (element){
                            const valueDataId = element.getAttribute('data-dive');
                            if (valueDataId == valueData) element.remove();
                        })
                    }
                }
            );
        }
    });
    $('#del-htmle').on('click',function(e){
        e.preventDefault();
        let valueData = diveSp.getAttribute('data-dive');
        if (valueData) {
            $.post('/htmles/delete_id/',
                {
                    'id_delete': valueData,
                    csrfmiddlewaretoken: csrftoken
                },
                function(response){
                    if (response.msg) {
                        itemDive.forEach(function (element){
                            const valueDataId = element.getAttribute('data-dive');
                            if (valueDataId == valueData) element.remove();
                        })
                    }
                }
            );
        }
    });
})
