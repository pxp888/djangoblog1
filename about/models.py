from django.db import models

# Create your models here.
class AboutPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return f'{self.updated_on} - {self.title}'

