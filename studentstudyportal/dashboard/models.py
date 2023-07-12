from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self):
        return self.title
    #this is to display the title name in the admin portal

    class Meta:
        verbose_name="notes"
        verbose_name_plural="notes"
        #By default django adds an extra 's' to notes hence to change that we use verbose

class Homework(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    description=models.TextField()
    due=models.DateTimeField()
    is_finished=models.BooleanField(default=False)

    def __str__(self):
        return self.subject
    
class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    is_finished=models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    

    
    
