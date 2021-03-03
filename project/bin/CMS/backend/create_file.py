from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from backend.shablon import select_template_create

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = Path.joinpath(BASE_DIR, "production")


def create_file(use_name, items):
    all_file = []
    for item in items:
        section = select_template_create(item)
        all_file.append(section)
    footer = '<script src="./js/index.js"></script></body></html>'
    all_file.append(footer)
    complete_name = Path.joinpath(TEMPLATE_DIR, use_name+'.html')
    file = open(complete_name, 'w', encoding='utf-8')
    for index in all_file:
        file.write(index+'\n')
    file.close()

