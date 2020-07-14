from django.db import models
from django.core.validators import FileExtensionValidator


class Question(models.Model):
    title = models.CharField(max_length=100)
    question = models.TextField()
    solution = models.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['txt'])])


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    output = models.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['txt'])])
