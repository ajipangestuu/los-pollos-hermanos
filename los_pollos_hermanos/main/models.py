from django.db import models

class Menu(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.PositiveIntegerField()
    gambar = models.ImageField(upload_to="menu_images/")

    def __str__(self):
        return self.nama
