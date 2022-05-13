from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _



# Create your models here.
class Column(models.Model):
    name = models.CharField(max_length=20)
    

    class Meta:
        verbose_name = _("Column")
        verbose_name_plural = _("Columns")

    def __str__(self):
        return self.name





class Card(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name="cards")
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _("Card")
        verbose_name_plural = _("Cards")

    def __str__(self):
        return self.title

