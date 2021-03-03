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
