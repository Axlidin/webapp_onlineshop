from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    category_icon = models.URLField(verbose_name="Kategoriya iconi", max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    productname = models.CharField(verbose_name="Mahsulot nomi", max_length=50)
    photo = models.URLField(verbose_name="Rasm url", max_length=200, blank=True, null=True)
    price = models.IntegerField(verbose_name="Narx")
    description = models.TextField(verbose_name="Mahsulot haqida", max_length=3000, null=True)

    category = models.ForeignKey(Category, verbose_name="Kategoriya nomi", on_delete=models.CASCADE)

    def __str__(self):
        return f"№{self.id} - {self.productname}"