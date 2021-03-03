(function () {
    window.addEventListener('scroll', function() {
        if (document.body.clientWidth > 995){
            var header_block = document.querySelector(".header_block");
            if(pageYOffset > 200){
                header_block.style.backgroundColor = 'rgba(0, 170, 255, 0.7)';
            } else {
                header_block.style.backgroundColor = 'rgba(44, 60, 76, 0)';
            }
        }
    });
    var mobileBurger = document.querySelector(".mobile_burger");
    mobileBurger.addEventListener('click', function () {
        var mobileContainer = document.querySelector(".mobile");
        var headerBlock = document.querySelector(".header_block");
        mobileContainer.classList.contains('mobile_burger_opened') ?
            mobileContainer.classList.remove('mobile_burger_opened') :
            mobileContainer.classList.add('mobile_burger_opened');
        headerBlock.classList.contains('header_block_hidden') ?
            headerBlock.classList.remove('header_block_hidden') :
            headerBlock.classList.add('header_block_hidden');
    })
})()