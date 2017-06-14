from django.db import models
from datetime import datetime

class Fecha(models.Model):
	hora_actual = models.DateTimeField(default=datetime.now(), blank=True)