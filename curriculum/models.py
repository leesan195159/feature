from django.db import models

class Curriculum(models.Model):
    curriculum = models.CharField(max_length=50)
    sort_no = models.IntegerField(null=True)
    full_name = models.CharField(max_length=50, null=True)
    short_name = models.CharField(max_length=50, null=True)
    korean_name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=100, null=True)
    version_code = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'curriculums'

class Lecture(models.Model):
    curriculum = models.CharField(max_length=50)
    lecture = models.IntegerField()
    lec_title = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'lectures'

class Feature(models.Model):
    feature_id = models.CharField(max_length=50)
    feature_name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    curriculum = models.CharField(max_length=50)
    chapter_id = models.IntegerField(null=True)
    pages = models.IntegerField(null=True)
    category = models.CharField(max_length=50, null=True)
    remark = models.CharField(max_length=150, null=True)
    idx = models.CharField(max_length=150, null=True)
    lecture_idx = models.CharField(max_length=150, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'features'

class FeatureProblem(models.Model):
    feature_id = models.CharField(max_length=50)
    problem_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'featureproblems'

class LectureIndice(models.Model):
    curriculum = models.CharField(max_length=50)
    problem_id = models.IntegerField()
    lecture_id = models.IntegerField()
    lecture_idx = models.CharField(max_length=100)
    end_idx = models.IntegerField()
    page = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'lectureindices'

class Problem(models.Model):
    layout_id = models.IntegerField()
    elements = models.CharField(max_length=2000)
    name = models.CharField(max_length=200)
    answer = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    type2 = models.CharField(max_length=100)
    type3 = models.CharField(max_length=100)
    question = models.CharField(max_length=200)
    random = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'problems'

class RevStruct(models.Model):
    parent = models.IntegerField()
    child = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'revstructs'

class LectureTemp(models.Model):
    curriculum = models.CharField(max_length=50)
    lecture_id = models.IntegerField()
    temp = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'lecturetemps'