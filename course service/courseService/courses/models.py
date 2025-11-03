from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    schedule = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class StudentCourse(models.Model):
    student_id = models.IntegerField()  # linked to student from Spring Boot
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
