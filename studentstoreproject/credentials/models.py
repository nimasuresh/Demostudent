from django.db import models
class place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100,)
    def __str__(self):
        return self.name

class Courses(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,)
    def __str__(self):
        return self.name
class Purpose(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name