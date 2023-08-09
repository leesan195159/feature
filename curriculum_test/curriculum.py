import os, django, sys
from curriculum.models import Curriculum
from django.db import transaction

os.chdir('.')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "curriculum_test.settings")

django.setup()


@transaction.atomic()
def insert():
    name = 'dhg3'
    if Curriculum.objects.filter(curriculum=name).exists():
        print(f'{name}는 이미 생성되어 있는 커리큘럼입니다')
    else:
        Curriculum.objects.create(
            curriculum=name,
            sort_no=Curriculum.objects.count(),
            full_name='독해끝 스킬편1',
            short_name='독해끝 스킬편1',
            korean_name='독해끝 스킬편1',
            description='',
            version_code='1'
        )


def run():
    insert()

