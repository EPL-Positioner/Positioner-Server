from django.db import models

class Soccer(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name