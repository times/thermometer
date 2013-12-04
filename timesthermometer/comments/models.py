from django.db import models

class User(models.Model):
  avatar = models.CharField(max_length=200, blank=True)
  name = models.CharField(max_length=200)
  def __unicode__(self):
    return self.name

class Comment(models.Model):
  pub_date = models.DateTimeField('date published')
  user = models.ForeignKey(User)
  comment = models.TextField()