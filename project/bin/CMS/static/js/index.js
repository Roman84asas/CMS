(function () {
   const itemBody = document.querySelectorAll('.item-body');
   const itemDive = document.querySelectorAll('.item-dive');
   const itemHtml = document.querySelectorAll('.item-html');

   itemBody.forEach(function (element) {
       element.addEventListener('click', function (){
           const valueData = element.getAttribute('data-bodys');
           const hrefBody = document.querySelector('#bodys');
           const hrefUpd = document.querySelector('#bodys-update');
           const allAddress = '/bodys/create/'+valueData
           const allAddressUp = '/bodys/'+valueData
           hrefBody.removeAttribute('href');
           hrefBody.setAttribute('href', allAddress);
           hrefUpd.removeAttribute('href');
           hrefUpd.setAttribute('href', allAddressUp);
       })
   })
    itemDive.forEach(function (element) {
       element.addEventListener('click', function (){
           const valueData = element.getAttribute('data-dive');
           const hrefBody = document.querySelector('#dives');
           const hrefUpd = document.querySelector('#dives-update');
           const allAddress = '/dives/create/'+valueData
           const allAddressUp = '/dives/'+valueData
           hrefBody.removeAttribute('href');
           hrefBody.setAttribute('href', allAddress);
           hrefUpd.removeAttribute('href');
           hrefUpd.setAttribute('href', allAddressUp);
       })
   })
    itemHtml.forEach(function (element) {
       element.addEventListener('click', function (){
           const valueData = element.getAttribute('data-htmle');
           const hrefBody = document.querySelector('#htmles');
           const hrefUpd = document.querySelector('#htmles-update');
           const allAddress = '/htmles/create/'+valueData
           const allAddressUp = '/htmles/'+valueData
           hrefBody.removeAttribute('href');
           hrefBody.setAttribute('href', allAddress);
           hrefUpd.removeAttribute('href');
           hrefUpd.setAttribute('href', allAddressUp);
       })
   })
})()