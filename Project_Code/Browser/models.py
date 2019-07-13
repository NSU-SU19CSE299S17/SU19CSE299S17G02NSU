from django.db import models

class Books(models.Model):

    Book_ID = models.IntegerField(primary_key=True)
    Title  = models.CharField(max_length=150)
    Author = models.CharField(max_length=150)
    Genre1 = models.CharField(max_length=150)
    Genre2 = models.CharField(max_length=150)
    Plot   = models.TextField()

#'Books' is populated with data from 'DATA set.csv' using csv.py package


def __str__(self):
    return self.title

