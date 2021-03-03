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
