from django.db import models


class PoemAuthor(models.Model):
    class Meta:
        db_table = 'poems_author'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    intro_l = models.TextField()
    intro_s = models.TextField()


class PoetryAuthor(models.Model):
    class Meta:
        db_table = 'poetry_author'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    intro = models.TextField()
    dynasty = models.CharField(max_length=10)


