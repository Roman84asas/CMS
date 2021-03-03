from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


def create_file(use_name, items):
    for item in items:
        print(item['data_id'])
