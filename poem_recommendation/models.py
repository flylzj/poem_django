from django.db import models
from poet_recommendation.models import PoemAuthor, PoetryAuthor

class Poetry(models.Model):

    class Meta:
        db_table = 'poetry'

    id = models.AutoField()
    author = models.ForeignKey(PoetryAuthor, to_field='author_id', on_delete=models.CASCADE, related_name='poetry')


