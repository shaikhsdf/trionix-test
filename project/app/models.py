from django.db import models

class student(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=300)
    lastname = models.CharField(max_length=300)
    dob = models.DateField()
    email = models.EmailField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
