import os, django, csv, sys

os.chdir('.')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "curriculum_test.settings")

django.setup()
from .models import *

PATH = 'curriculum/problem/독해끝 스킬편2_0731 (2).problem'
def insert():
    with open(PATH, encoding='utf-8') as csvfile:
        data_reader = csv.reader(csvfile)
        next(data_reader, None)
        for row in data_reader:
            # if not Category.objects.filter(name=row[1]).exists():
            if row[0]:
                feature_id, feature_name = row
                feature = Feature.objects.create(feature_id=feature_id, feature_name=feature_name)
                feature.save()
                # Feature.objects.create(
                #     feature_id, feature_name=row
                    # feature_id=row[1],
                    # feature_name=row[2],
                    # description=row[2],
                    # curriculum=A,
                    # chapter_id='',
                    # lecture_id=
                # )
def run():
    insert()