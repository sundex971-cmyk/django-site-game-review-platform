from django.db import models

from games.models import Game

from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):

    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    text = models.TextField()

    rating = models.IntegerField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.user} - {self.game}'