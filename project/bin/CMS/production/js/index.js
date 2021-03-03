"use strict";
(function () {
    var opacity_all = document.querySelectorAll(".opacity_all");
    var right_marg = document.querySelectorAll(".right_marg");
    var left_marg = document.querySelectorAll(".left_marg");
    var section = document.querySelectorAll("section");
    for (let i = 0; i < section.length; i++) {
        if (i===0) section[i].classList.add('prime');
        if (i===1) section[i].classList.add('prime');
        if (i===2) section[i].classList.add('prime');
    }
    opacity_all.forEach(function (element) {
        let h_element = element.offsetHeight;
        let pageHeight = element.getBoundingClientRect().top;
        pageHeight = pageHeight - h_element;
        if (pageHeight <= 0) {
            element.style.opacity = 1;
            element.style.transition = 'opacity 0.8s ease';
        }
        window.addEventListener('scroll', function () {
            let hi_element = element.offsetHeight;
            let pageHeighti = element.getBoundingClientRect().top;
            pageHeighti = pageHeighti - hi_element - 700;
            if (pageHeighti <= 0) {
                element.style.opacity = 1;
                element.style.transition = 'opacity 1s ease';
            }
        })
    })
    right_marg.forEach(function (element) {
        let h_element = element.offsetHeight;
        let pageHeight = element.getBoundingClientRect().top;
        pageHeight = pageHeight - h_element;
        if (pageHeight <= 0) {
            element.style.marginRight = 0;
            element.style.transition = 'margin-right 1.5s ease';
        }
        window.addEventListener('scroll', function () {
            let hi_element = element.offsetHeight;
            let pageHeighti = element.getBoundingClientRect().top;
            pageHeighti = pageHeighti - hi_element - 750;
            if (pageHeighti <= 0) {
                element.style.marginRight = 0;
                element.style.transition = 'margin-right 1s ease';
            }
        })
    })
    left_marg.forEach(function (element) {
        let h_element = element.offsetHeight;
        let pageHeight = element.getBoundingClientRect().top;
        pageHeight = pageHeight - h_element;
        if (pageHeight <= 0) {
            element.style.marginLeft = 0;
            element.style.transition = 'margin-left 1.5s ease';
        }
        window.addEventListener('scroll', function () {
            let hi_element = element.offsetHeight;
            let pageHeighti = element.getBoundingClientRect().top;
            pageHeighti = pageHeighti - hi_element - 750;
            if (pageHeighti <= 0) {
                element.style.marginLeft = 0;
                element.style.transition = 'margin-left 1s ease';
            }
        })
    })
})()