from django.db import models

# Create your models here.

class Author(models.Model):
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    birthdate = models.DateField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"



class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.RESTRICT)
    genre = models.CharField(max_length=100)
    release = models.DateField()

    def __str__(self):
        return self.title
    
