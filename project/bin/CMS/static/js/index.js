(function () {
   const itemBody = document.querySelectorAll('.item-body');
   const itemDive = document.querySelectorAll('.item-dive');
   const itemHtml = document.querySelectorAll('.item-html');

   itemBody.forEach(function (element) {
       element.addEventListener('click', function (){
           const valueData = element.getAttribute('data-bodys');
           const hrefBody = document.querySelector('#bodys');
           const allAddress = '/bodys/create/'+valueData
           hrefBody.removeAttribute('href');
           hrefBody.setAttribute('href', allAddress);
       })
   })
    itemDive.forEach(function (element) {
       element.addEventListener('click', function (){
           const valueData = element.getAttribute('data-dive');
           const hrefBody = document.querySelector('#dives');
           const allAddress = '/dives/create/'+valueData
           hrefBody.removeAttribute('href');
           hrefBody.setAttribute('href', allAddress);
       })
   })
    itemHtml.forEach(function (element) {
       element.addEventListener('click', function (){
           const valueData = element.getAttribute('data-htmle');
           const hrefBody = document.querySelector('#htmles');
           const allAddress = '/htmles/create/'+valueData
           hrefBody.removeAttribute('href');
           hrefBody.setAttribute('href', allAddress);
       })
   })
})()