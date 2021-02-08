from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.TextField(max_length=255, blank=False, null=False)
    author = models.TextField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'description': self.description
        }

