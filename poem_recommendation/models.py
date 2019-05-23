from django.db import models


# class Poetry(models.Model):
#
#     class Meta:
#         db_table = 'poetry'
#
#     id = models.AutoField(primary_key=True)
#     author = models.ForeignKey('poet_recommendation.PoetryAuthor', to_field='id', on_delete=models.CASCADE, related_name='poetry', db_column='author_id')
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     yunlv_rule = models.TextField()


class Poem(models.Model):
    class Meta:
        db_table = 'poem'

    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(
        'poet_recommendation.Poet', to_field='id', on_delete=models.CASCADE, related_name='poems', db_column='author_id'
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    yunlv_rule = models.TextField()
    poem_type = models.CharField(max_length=20)

    def content_as_line(self):
        return self.content.split('|')


# class Poem2(models.Model):
#     class Meta:
#         db_table = 'poems'
#
#     id = models.AutoField(primary_key=True)
#     author = models.ForeignKey('poet_recommendation.PoemAuthor', to_field='id', on_delete=models.CASCADE, related_name='poems', db_column='author_id')
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#
#     def content_as_line(self):
#         return self.content.split('|')

