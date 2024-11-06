from django.db import models
from django.contrib.auth.models import User 

class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    size = models.PositiveIntegerField(default=0)  # Taille du fichier en octets

    def save(self, *args, **kwargs):
        self.size = self.file.size  # Enregistrer la taille du fichier
        super().save(*args, **kwargs)




