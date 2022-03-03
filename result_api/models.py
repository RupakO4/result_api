from django.db import models

# Create your models here.
class Exam(models.Model):
    exam_id = models.SlugField(primary_key=True, max_length=255)
    exam_name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.exam_name

    class Meta:
        ordering = ('-created',)

class Result(models.Model):
    student_id = models.CharField(primary_key=True, max_length=255)
    pass_fail = models.CharField(max_length=255)
    exam_id = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_id