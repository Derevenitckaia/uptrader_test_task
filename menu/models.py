from django.db import models
from django.core.exceptions import ValidationError


#Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    title = models.CharField(max_length=20)

    cat = models.ForeignKey('Menu', on_delete=models.CASCADE)

    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def get_ancestor_ids(self):
        if self.parent:
            return self.parent.get_ancestor_ids() + [self.parent.id]
        else:
            return []


    def __str__(self):
        return self.title

    def clean(self):
        if self.cat != self.parent.cat:
            raise ValidationError('Item and parent has different menu\'s category')









