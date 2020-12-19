from django.db import models

# Create your models here.
class Participant(models.Model):
    name = models.CharField(max_length=60)
    student_id = models.IntegerField(default=000000, blank=True)
    programme_code = models.CharField(max_length=6, blank=True)
    faculty = models.CharField(max_length=100, blank=True)
    campus = models.CharField(max_length=100, blank=True)
    unique = models.CharField(max_length=60)
    location = models.CharField(max_length=100, blank=True)
    class_attended = models.CharField(max_length=100, blank=True)
    lecturer = models.CharField(max_length=100, blank=True)
    time = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return self.name
