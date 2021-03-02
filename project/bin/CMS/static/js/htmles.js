(function () {
   const addDiv = document.querySelector('#add_div');
   const close = document.querySelector('#close');

   addDiv.addEventListener('click', function (){
       const popup = document.querySelector('#hidden_popup');
       popup.style.display = 'block';
   })

   close.addEventListener('click', function (){
       const popup = document.querySelector('#hidden_popup');
       popup.style.display = 'none';
   })
})()