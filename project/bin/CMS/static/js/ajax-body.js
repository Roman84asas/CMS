$(document).ready(function() {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const itemBody = document.querySelectorAll('.item-body');
    const itemDive = document.querySelectorAll('.item-dive');

    $('#del-bodys').on('click',function(e){
        e.preventDefault();
        const valueData = $(this).data('bodys');
        console.log(valueData)
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
        const valueData = $(this).data('dive');
        console.log(valueData)
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
})
