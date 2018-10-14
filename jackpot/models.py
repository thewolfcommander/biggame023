from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class GameJackpot(models.Model):
    bet = models.IntegerField(validators=[MinValueValidator(0)])
    amount_for_bet = models.DecimalField(max_digits = 20, decimal_places = 2, default = 10.00)
    amount_won = models.DecimalField(max_digits = 20, decimal_places = 2, default = 0.00)
    amount_credit = models.DecimalField(max_digits = 20, decimal_places = 2, default = 0.00)
    counter = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    win_counter = models.IntegerField(validators=[MinValueValidator(0)], default=0)