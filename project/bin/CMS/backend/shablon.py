def select_template_create(item):
    if item['data_id'] == '111111':
        return item['data_text']

    if item['data_id'] == '222222':
        return item['data_text']

    if item['data_id'] == '333333':
        return item['data_text']

    if item['data_id'] == '1':
        title = item['data_header']
        body = item['data_text']
        all = '<header><div class="mobile"><div class="mobile_container"><div class="mobile_text"><div>'+title+'</div></div><div class="mobile_burger"><span></span><span></span><span></span><span></span></div></div></div><div class="header_block header_block_fixed"><div class="wrapper">'+body+'<div class="header_block_right_hr"><hr></div></div></div><script>window.addEventListener("scroll",function(){if (document.body.clientWidth > 995){var header_block = document.querySelector(".header_block");if(pageYOffset > 200){header_block.style.backgroundColor = "rgba(0, 170, 255, 0.7)";} else {header_block.style.backgroundColor = "rgba(44, 60, 76, 0)";}}});var mobileBurger=document.querySelector(".mobile_burger");mobileBurger.addEventListener("click",function(){var mobileContainer=document.querySelector(".mobile");var headerBlock=document.querySelector(".header_block");mobileContainer.classList.contains("mobile_burger_opened") ? mobileContainer.classList.remove("mobile_burger_opened") : mobileContainer.classList.add("mobile_burger_opened"); headerBlock.classList.contains("header_block_hidden") ? headerBlock.classList.remove("header_block_hidden") : headerBlock.classList.add("header_block_hidden"); })</script></header>'
        return all

    if item['data_id'] == '2':
        title = item['data_header']
        body = item['data_text']
        all = '<section class="top_section_t"><div class="wrapper"><div class="top_section_body" id="top_section_body_1"><div class="background_top"></div>'+title+body+'</div></div></section>'
        return all

    if item['data_id'] == '3':
        title = item['data_header']
        body = item['data_text']
        all = '<section class="decision_section opacity_all prime" id="tth"><div class="wrapper"><div class="decision_section_body lll-b">'+title+body+'</div></div></section>'
        return all


    if item['data_id'] == '4':
        title = item['data_header']
        all = '<section class="arrow_to_down"><div class="arrow_to_down_body""><div class="arrow_to_down_all">'+title+'</div></div></section>'
        return all

    if item['data_id'] == '5':
        title = item['data_header']
        body = item['data_text']
        all = '<section class="connections_provides opacity_all"><div class="wrapper"><div class="connections_provides_body">'+title+body+'</div></div></section>'
        return all

    if item['data_id'] == '6':
        title = item['data_header']
        body = item['data_text']
        all = '<section class="custom_block_text opacity_all"><div class="wrapper"><div class="custom_block_body">'+title+body+'</div></div></section>'
        return all

    if item['data_id'] == '7':
        title = item['data_header']
        body = item['data_text']
        all = '<section class="decision_section opacity_all"><div class="wrapper"><div class="decision_section_body lll">'+title+body+'</div></div></section>'
        return all

    if item['data_id'] == '8':
        title = item['data_header']
        body = item['data_text']
        all = '<section class="connections_provides opacity_all"><div class="wrapper"><div class="connections_provides_body">'+title+body+'</div></div></section>'
        return all

    if item['data_id'] == '9':
        title = item['data_header']
        body = item['data_text']
        all = '<section class="connections_provides opacity_all"><div class="wrapper"><div class="connections_provides_body">'+title+body+'</div></div></section>'
        return all

    if item['data_id'] == '10':
        title = item['data_header']
        body = item['data_text']
        all = '<section class="decision_section opacity_all"><div class="wrapper"><div class="decision_section_body lll">'+title+body+'</div></div></section>'
        return all

    if item['data_id'] == '11':
        title = item['data_header']
        body = item['data_text']
        all = '<section class="connections_provides opacity_all"><div class="wrapper"><div class="connections_provides_body">'+title+body+'</div></div></section>'
        return all

    if item['data_id'] == '12':
        title = item['data_header']
        body = item['data_text']
        all = '<section class="connections_provides opacity_all"><div class="wrapper"><div class="connections_provides_body">'+title+body+'</div></div></section>'
        return all

    if item['data_id'] == '13':
        title = item['data_header']
        body = item['data_text']
        all = '<section class="connections_provides opacity_all"><div class="wrapper"><div class="connections_provides_body">'+title+body+'</div></div></section>'
        return all

    if item['data_id'] == '14':
        title = item['data_header']
        body = item['data_text']
        all = '<section class="connections_provides opacity_all"><div class="wrapper"><div class="connections_provides_body">'+title+body+'</div></div></section>'
        return all

    if item['data_id'] == '15':
        title = item['data_header']
        body = item['data_text']
        all = '<section class="decision_section opacity_all"><div class="wrapper"><div class="decision_section_body lll">'+title+body+'</div></div></section>'
        return all

    if item['data_id'] == '16':
        title = item['data_header']
        body = item['data_text']
        all = '<section class="connections_provides opacity_all"><div class="wrapper"><div class="connections_provides_body">'+title+body+'</div></div></section>'
        return all

    if item['data_id'] == '17':
        title = item['data_header']
        body = item['data_text']
        all = '<section class="connections_provides opacity_all"><div class="wrapper"><div class="connections_provides_body">'+title+body+'</div></div></section>'
        return all

    if item['data_id'] == '18':
        title = item['data_header']
        body = item['data_text']
        all = '<section class="connections_provides opacity_all"><div class="wrapper"><div class="connections_provides_body">'+title+body+'</div></div></section>'
        return all

    if item['data_id'] == '19':
        title = item['data_header']
        body = item['data_text']
        all = '<footer><div class="wrapper">'+title+body+'</div></footer>'
        return all

    if item['data_id'] == '20':
        title = item['data_header']
        body = item['data_text']
        all = '<header><div class="mobile"><div class="mobile_container"><div class="mobile_text">'+title+'</div><div class="mobile_burger"><span></span><span></span><span></span><span></span></div></div></div><div class="header_block header_block_fixed"><div class="wrapper">'+body+'<div class="header_block_right_hr"><hr></div></div></div><script>window.addEventListener("scroll", function() { if (document.body.clientWidth > 995){var header_block = document.querySelector(".header_block"); if(pageYOffset > 200){header_block.style.backgroundColor = "rgba(44, 60, 76, 0.2)";} else {header_block.style.backgroundColor = "rgba(44, 60, 76, 0)";}}});var mobileBurger = document.querySelector(".mobile_burger");mobileBurger.addEventListener("click", function () {var mobileContainer = document.querySelector(".mobile");var headerBlock = document.querySelector(".header_block");mobileContainer.classList.contains("mobile_burger_opened") ? mobileContainer.classList.remove("mobile_burger_opened") : mobileContainer.classList.add("mobile_burger_opened");headerBlock.classList.contains("header_block_hidden") ? headerBlock.classList.remove("header_block_hidden") : headerBlock.classList.add("header_block_hidden");})</script></header>'
        return all

    if item['data_id'] == '21':
        title = item['data_header']
        body = item['data_text']
        all = '<section class="top_section"><div class="wrapper"><div class="top_section_body" id="top_section_body_1"><div class="background_top"></div>'+title+body+'</div></div><script>if (document.body.clientWidth > 995){var topSectionBody = document.querySelector(".top_section").clientHeight;ar backgroundTop = document.querySelector(".background_top");backgroundTop.style.minHeight = topSectionBody + "px";}</script></section>'
        return all

    if item['data_id'] == '22':
        title = item['data_header']
        body = item['data_text']
        all = '<section class="decision_section opacity_all prime"><div class="wrapper"><div class="decision_section_body">'+title+body+'</div></div></section>'
        return all

    if item['data_id'] == '23':
        body = item['data_text']
        all = '<section class="section_image opacity_all"><div class="wrapper"><div class="section_VC_body flex-center-jc-sp-between">'+body+'</div></div></section>'
        return all

    if item['data_id'] == '24':
        body = item['data_text']
        all = '<section class="implementation_result opacity_all"><div class="wrapper"><div class="implementation_result_body flex-wrap-wrap">'+body+'</div></div></section>'
        return all

    if item['data_id'] == '25':
        body = item['data_text']
        all = '<section class="implementation_result opacity_all"><div class="wrapper"><div class="implementation_result_body_right flex-wrap-wrap">'+body+'</div></div></section>'
        return all

    if item['data_id'] == '26':
        body = item['data_text']
        all = '<section class="link_demo opacity_all"><div class="wrapper">'+body+'</div></section>'
        return all

    if item['data_id'] == '27':
        title = item['data_header']
        body = item['data_text']
        all = '<section class="decision_section line_top opacity_all"><div class="wrapper"><div class="decision_section_body short_section">'+title+body+'</div></div></section>'
        return all

    if item['data_id'] == '28':
        body = item['data_text']
        all = '<section class="connection_manager opacity_all"><div class="wrapper"><div class="connection_manager_body flex-wrap-wrap">'+body+'</div></div></section>'
        return all

    if item['data_id'] == '29':
        body = item['data_text']
        all = '<section class="custom_block_text opacity_all"><div class="wrapper"><div class="custom_block_body">'+body+'</div></div></section>'
        return all

    if item['data_id'] == '30':
        body = item['data_text']
        all = '<section class="section_image opacity_all"><div class="wrapper">'+body+'</div></section>'
        return all

    if item['data_id'] == '31':
        body = item['data_text']
        all = '<section class="custom_block_text opacity_all"><div class="wrapper">'+body+'</div></section>'
        return all

    if item['data_id'] == '32':
        body = item['data_text']
        all = '<section class="connection_manager_tasks opacity_all"><div class="wrapper"><div class="connection_manager_tasks_body flex-wrap-wrap">'+body+'</div></div></section>'
        return all

    if item['data_id'] == '33':
        title = item['data_header']
        body = item['data_text']
        all = '<section class="decision_section line_top opacity_all"><div class="wrapper"><div class="decision_section_body short_section">'+title+body+'</div></div></section>'
        return all

    if item['data_id'] == '34':
        body = item['data_text']
        all = '<section class="table_small opacity_all" ><div class="wrapper"><div class="arrow_to_down_all">'+body+'</div></div></section>'
        return all

    if item['data_id'] == '35':
        body = item['data_text']
        all = '<section class="link_demo plus-bb opacity_all"><div class="wrapper">'+body+'</div></section>'
        return all

    if item['data_id'] == '36':
        title = item['data_header']
        body = item['data_text']
        all = '<section class="decision_section line_top opacity_all"><div class="wrapper"><div class="decision_section_body short_section">'+title+body+'</div></div></section>'
        return all

    if item['data_id'] == '37':
        body = item['data_text']
        all = '<section class="implementation_result opacity_all"><div class="wrapper sm-wrapper"><div class="implementation_result_body flex-wrap-wrap">'+body+'</div></div></section>'
        return all

    if item['data_id'] == '38':
        body = item['data_text']
        all = '<section class="implementation_result lll opacity_all"><div class="wrapper sm-wrapper lll"><div class="implementation_result_body_right flex-wrap-wrap">'+body+'</div></div></section>'
        return all

    if item['data_id'] == '39':
        body = item['data_text']
        all = '<section class="implementation_result lll-b opacity_all"><div class="wrapper sm-wrapper"><div class="implementation_result_body flex-wrap-wrap">'+body+'</div></div></section>'
        return all

    if item['data_id'] == '40':
        title = item['data_header']
        body = item['data_text']
        all = '<section class="decision_section line_top opacity_all"><div class="wrapper"><div class="decision_section_body short_section">'+title+body+'</div></div></section>'
        return all

    if item['data_id'] == '41':
        body = item['data_text']
        all = '<div class="slider_section opacity_all"><div class="wrapper"><div class="arrow_right" style="width: 9px;"><svg style="display: block" viewBox="0 0 9.3 17" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><polyline fill="none" stroke="#000000" stroke-linecap="butt" stroke-width="1" points="0.5,0.5 8.5,8.5 0.5,16.5" /> </svg></div><div class="slider single-item">'+body+'</div><div class="arrow_left" style="width: 9px;"><svg style="display: block" viewBox="0 0 9.3 17" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><polyline fill="none" stroke="#000000" stroke-linecap="butt" stroke-width="1" points="0.5,0.5 8.5,8.5 0.5,16.5" /> </svg></div><script>$(".single-item").slick({dots: true,fade: true,cssEase: "linear",slidesToShow: 1,slidesToScroll: 1,speed: 300,adaptiveHeight: true,prevArrow: $(".arrow_right"),nextArrow: $(".arrow_left"),});</script></div></div>'
        return all

    if item['data_id'] == '42':
        title = item['data_header']
        body = item['data_text']
        all = '<section class="decision_section line_top opacity_all" id="contact"><div class="wrapper"><div class="decision_section_body short_section">'+title+body+'</div></div></section>'
        return all

    if item['data_id'] == '43':
        body = item['data_text']
        all = '<div id="rec41449744"  class="map opacity_all" ><div class="t117" id="map">'+body+'<script type="text/javascript"> var arMapMarkers41449744=[{title:"УВЕОН - ОБЛАЧНЫЕ ТЕХНОЛОГИИ",descr:"",lat:"55.6740282",lng:"37.5040360",},];$(document).ready(function(){t_appendYandexMap("41449744","");});</script></div></div>'
        return all

    if item['data_id'] == '44':
        body = item['data_text']
        all = '<footer><div class="wrapper">'+body+'</div></footer>'
        return all
