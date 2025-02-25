from django.db import models

class Subscription(models.Model):
    DURATION_CHOICES = [
        (1, "1 месяц"),
        (3, "3 месяца"),
        (6, "6 месяцев"),
        (12, "1 год"),
    ]

    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(choices=DURATION_CHOICES)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def final_price(self):
        return self.price * (1 - self.discount / 100)

    def __str__(self):
        return f"Подписка на {self.get_duration_display()} - {self.final_price()} руб."
