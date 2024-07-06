from django.db import models

class DisplayMenuModel(models.Model):
    menu_name = models.CharField(max_length=200)
    menu_ingredients = models.TextField()
    menu_instructions = models.TextField()
    menu_category = models.CharField(max_length=100)

    def __str__(self):
        return self.menu_name