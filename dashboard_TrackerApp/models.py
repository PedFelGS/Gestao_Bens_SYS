from django.db import models

class DashboardAccessLog(models.Model):
    access_time = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=255)

    def __str__(self):
        return f"Acesso em {self.access_time} por {self.user}"