from django.db import models


class Flat(models.Model):

    class Meta:
        db_table = 'flats'
        default_permissions = ()

    id = models.AutoField(primary_key=True)
    title = models.TextField()
    image_url = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.image_url}"