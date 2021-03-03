def select_template_create(item):
    if item['data_id'] == '111111':
        return item['data_text']

    if item['data_id'] == '222222':
        return item['data_text']

    print(item['data_text'])
