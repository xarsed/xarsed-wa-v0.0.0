from django.db import models


class Article(models.Model):
    
    Title = models.CharField(max_length=200, unique=True) 
    Content = models.TextField()
    Description = models.CharField(max_length=250)
    Keywords = models.CharField(max_length=150)

    def __str__(self):
        return self.Title
    
    def get_absolute_url(self):
        return "/documentation/open_article/" + self.Title
