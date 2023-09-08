from django.db import models
from django.contrib.auth.models import User

class Hospitals:
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Visitor:
    user = models.OneToOneField(User, on_delete=models.CASCADE)