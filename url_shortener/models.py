from django.db import models


# Create your models here.
class ShortUrl(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=500)
    short_url = models.CharField(max_length=15, null=False, blank=False)
    original_url = models.CharField(max_length=1000)
    add_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + '# - ' + self.short_url
