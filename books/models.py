from django.db import models


# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Book(models.Model):
    name = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    page = models.IntegerField()
    exist = models.BooleanField(default=True)

    def __str__(self):
        return "%s, %s, %s" % (self.name, self.author, str(self.page))
