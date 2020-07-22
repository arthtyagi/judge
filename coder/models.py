from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse
from ckeditor.fields import RichTextField


class Question(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    iscorrect = models.BooleanField(default=False)
    solution = models.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['txt'])], upload_to='media')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('coder:detail', kwargs={'pk': self.pk})


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    iscorrect = models.BooleanField(default=False)
    result = models.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['txt'])], upload_to='media', blank=True, null=True)
   # result = models.FileField( null= True, blank=True, default = 'media/media/output.txt',
    #   validators=[FileExtensionValidator(allowed_extensions=['txt'])], upload_to= 'media')
