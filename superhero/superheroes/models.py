from django.db import models

# Create your models here.

class Superhero(models.Model):
    name = models.CharField(max_length=50)
    alter_ego = models.CharField(max_length=50)
    primary_superhero_ability = models.CharField(max_length=50)
    secondary_superhero_ability = models.CharField(max_length=50)
    catchphrase = models.CharField(max_length=50)

    def __str__(self):
        return self.name, self.alter_ego, self.primary_superhero_ability, self.secondary_superhero_ability, self.catchphrase

