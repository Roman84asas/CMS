(function () {
   const itemBody = document.querySelectorAll('.item-body');
   const itemDive = document.querySelectorAll('.item-dive');
   const itemHtml = document.querySelectorAll('.item-html');

   itemBody.forEach(function (element) {
       element.addEventListener('click', function (){
           itemBody.forEach(function (elements){
               elements.classList.remove('active')
           })
           element.classList.add('active');

           const valueData = element.getAttribute('data-bodys');

           const hrefBody = document.querySelector('#bodys');
           const hrefUpd = document.querySelector('#bodys-update');
           const delBody = document.querySelector('#del-bodys');

           const allAddress = '/bodys/create/'+valueData
           const allAddressUp = '/bodys/'+valueData

           hrefBody.removeAttribute('href');
           hrefBody.setAttribute('href', allAddress);

           hrefUpd.removeAttribute('href');
           hrefUpd.setAttribute('href', allAddressUp);

           delBody.setAttribute('data-bodys', valueData);
       })
   })
    itemDive.forEach(function (element) {
       element.addEventListener('click', function (){
           itemDive.forEach(function (elements){
               elements.classList.remove('active')
           })
           element.classList.add('active');

           const valueData = element.getAttribute('data-dive');

           const hrefBody = document.querySelector('#dives');
           const hrefUpd = document.querySelector('#dives-update');
           const delBody = document.querySelector('#del-dive');

           const allAddress = '/dives/create/'+valueData
           const allAddressUp = '/dives/'+valueData

           hrefBody.removeAttribute('href');
           hrefBody.setAttribute('href', allAddress);

           hrefUpd.removeAttribute('href');
           hrefUpd.setAttribute('href', allAddressUp);

           delBody.setAttribute('data-dive', valueData);
       })
   })
    itemHtml.forEach(function (element) {
       element.addEventListener('click', function (){
           itemHtml.forEach(function (elements){
               elements.classList.remove('active')
           })
           element.classList.add('active');

           const valueData = element.getAttribute('data-htmle');

           const hrefBody = document.querySelector('#htmles');
           const hrefUpd = document.querySelector('#htmles-update');
           const delBody = document.querySelector('#del-htmle');

           const allAddress = '/htmles/create/'+valueData
           const allAddressUp = '/htmles/'+valueData

           hrefBody.removeAttribute('href');
           hrefBody.setAttribute('href', allAddress);

           hrefUpd.removeAttribute('href');
           hrefUpd.setAttribute('href', allAddressUp);

           delBody.setAttribute('data-htmle', valueData);
       })
   })
})()