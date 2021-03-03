$( document ).ready(function() {
    setTimeout(function() {
      const form = $('#form76265113');
      const successBox = form.find('.js-successbox');
      const inputBox = form.find('.t-form__inputsbox');
      const submitBtn = form.find('button[type=submit]').on('click', function(evt) {
        form.find('input[name=email]').attr('type', 'email');
        form.find('input[name=email]').attr('required', '');
        form.find('input[name=Input]').attr('name', 'sysuuid');
        form.find('input[name=sysuuid]').attr('required', '');
        form.find('input[name=name]').attr('required', '');

        form.find('.t-input-group').removeClass('js-error-control-box');
        evt.stopPropagation();
        evt.preventDefault();
        form.submit();
        //submitBtn.attr("disabled", "disabled");
      });
      form.on('submit', function(evt) {
        evt.stopPropagation();
        evt.preventDefault();
        //submitBtn.attr("disabled", "disabled");
        var fetchConfig = {
          method: 'POST',
          body: form.serialize(),
          mode: 'cors',
          headers: {
              "Content-Type": "application/x-www-form-urlencoded",
          },
        };
        fetch('https://termidesk.ru/demo-license',fetchConfig)
          .then(function(response) {
            return response.json();
          })
          .then(function(data) {
             if ( data.success ) {
               successBox.text('Запрос успешно отправлен');
               successBox.show();
               inputBox.hide();
             } else {
               //submitBtn.removeAttr("disabled");
               if ( data.errors.email ) {
                 form.find('input[name=email]').parent().parent().addClass('js-error-control-box');
               }
               if ( data.errors.name ) {
                 form.find('input[name=name]').parent().parent().addClass('js-error-control-box');
               }
               if ( data.errors.sysuuid ) {
                 form.find('input[name=sysuuid]').parent().parent().addClass('js-error-control-box');
               }
             }
          })
      })
    }, 1000);
  });