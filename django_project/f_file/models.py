from django.db import models


class File(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents', blank=False, null=False)

    class Meta:
        db_table = 'f_file'

    def __str__(self):
        return self.title

# class Image(models.Model):
#     url = models.CharField(max_length=100, null=False)
#
#     class Meta:
#         db_table = 'f_image'
