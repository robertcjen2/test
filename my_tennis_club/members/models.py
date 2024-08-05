from django.db import models

"""class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)"""

class Post(models.Model):
  post = models.TextField()
  title = models.TextField()
  author = models.CharField(max_length=50)
  pub_date = models.DateTimeField()
  def __unicode__(self):
  	return self.title
