import os, django, csv, sys

from curriculum.models import Feature, Lecture, Curriculum
from django.db import transaction

os.chdir('.')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "curriculum_test.settings")

django.setup()

PATH = './curriculum/csv/feature/독해끝 문제스킬편2_1~16강_feature.csv'


@transaction.atomic()
def insert():
    with open(PATH, encoding='utf-8') as csvfile:
        data_reader = csv.reader(csvfile)
        next(data_reader, None)
        count_create = 0
        count = 0,
        count_update = 0
        curr = 'dhg4'
        for row in data_reader:
            if not Curriculum.objects.filter(curriculum=curr).exists():
                print('커리큘럼을 먼저 생성해주세요')
                raise Curriculum.DoesNotExist
            if Feature.objects.filter(feature_id=row[1]).exists():
                feature = Feature.objects.get(feature_id=row[1])
                feature.feature_id = row[1],
                feature.feature_name = row[2]
                feature.description = row[2]
                feature.curriculum = curr,
                count_update += 1
                count += 1
            else:
                Feature.objects.create(
                    feature_id=row[1],
                    feature_name=row[2],
                    description=row[2],
                    curriculum=curr
                )
                count_create += 1
                count += 1
            if not Lecture.objects.filter(curriculum=Feature.objects.get(feature_id=row[1]).curriculum, lecture=count).exists():
                Lecture.objects.create(
                    curriculum=Feature.objects.get(feature_id=row[1]).curriculum,
                    lecture=count,
                    lec_title=''
                )
            else:
                lecture = Lecture.objects.get()
    print('수정: ' + str(count_update) + '   신규: ' + str(count_create))


def run():
    insert()
