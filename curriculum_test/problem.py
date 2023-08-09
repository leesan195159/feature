import os, django, csv, sys

os.chdir('')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "curriculum_test.settings")

django.setup()
from curriculum.models import *

PATH = 'curriculum/problem/독해끝 문제스킬편2_1~16강_feature.problem'
def insert():
    with open(PATH, encoding='utf-8') as csvfile:
        data_reader = csv.reader(csvfile)
        next(data_reader, None)
        count_create = 0
        count_update = 0
        for row in data_reader:
            if Feature.objects.filter(feature_id=row[1]).exists():
                feature = Feature.objects.get(feature_id=row[1])
                feature.feature_id = row[1]
                feature.feature_name = row[2]
                feature.description = row[2]
                feature.curriculum = 'dhg4'
                count_update+=1
                feature.save()
            else:
                Feature.objects.create(
                    feature_id=row[1],
                    feature_name=row[2],
                    description=row[2],
                    curriculum=''
                )
                count_create+=1
        print('수정: ' + str(count_update) + '   신규: ' + str(count_create))
def run():
    insert()
