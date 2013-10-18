from django.db import models

class Positive(models.Model):
  label = models.CharField(max_length=200)
  weight = models.IntegerField(default=0)
  def __unicode__(self):
    return self.label

class Negative(models.Model):
  label = models.CharField(max_length=200)
  weight = models.IntegerField(default=0)
  def __unicode__(self):
    return self.label

# e.g. too, very
class Incrementer(models.Model):
  label = models.CharField(max_length=200)
  def __unicode__(self):
    return self.label

# e.g. little, barely
class Decrementer(models.Model):
  label = models.CharField(max_length=200)
  def __unicode__(self):
    return self.label

# e.g. this is not bad
class Inverter(models.Model):
  label = models.CharField(max_length=200)
  def __unicode__(self):
    return self.label