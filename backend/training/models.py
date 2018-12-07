from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()


class Sport(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

# Create your models here.
class Training(models.Model):
    trainee = models.ForeignKey(User,on_delete=models.CASCADE, related_name="taken_trainings")
    coach = models.ForeignKey(User,on_delete=models.DO_NOTHING, related_name="given_trainings")
    name = models.CharField(max_length=255)
    progress = models.IntegerField(default=0,
                                   validators=[
                                       MaxValueValidator(100),
                                       MinValueValidator(0)
                                   ])
    sport = models.ForeignKey(Sport,on_delete=models.CASCADE)