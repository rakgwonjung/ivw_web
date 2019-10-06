from django.db import models

class Author(models.Model):

    nick_name = models.CharField(max_length=30)
    mail = models.CharField(max_length=30)


    def __str__(self):
        """A string representation of the model."""
        return self.nick_name

class Article(models.Model):

    title = models.CharField(max_length=40)
    content = models.CharField(max_length=1000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        """A string representation of the model."""
        return self.title


class Reply(models.Model):

    article = models.ForeignKey(Article, related_name='replies', on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        """A string representation of the model."""
        return self.content
