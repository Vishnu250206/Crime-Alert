from django.db import models

# Create your models here.
class SignupDetail(models.Model):
    username = models.CharField(max_length=200, unique=True)  # Unique constraint added
    password = models.CharField(max_length=200)
    contact = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()

    class Meta:
        db_table = "Signup"

class TipsDetail(models.Model):
    username = models.CharField(max_length=200)  # Assuming you want to store the username
    address = models.CharField(max_length=200)
    activity = models.CharField(max_length=200)
    description = models.TextField()
    hashcode = models.CharField(max_length=200)
    timestamp = models.DateTimeField()
    filename = models.CharField(max_length=200)
    prediction = models.CharField(max_length=200)

    class Meta:
        db_table = "TipsDetail"

class FeedbackModel(models.Model):
    username = models.CharField(max_length=200,null=True)
    message = models.TextField(null=True)
    class Meta:
        db_table="Feedback"