$(document).ready(function() {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const itemBody = document.querySelectorAll('.item-body');

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
})
