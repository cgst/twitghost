from django.db import models
from datetime import datetime


class Tweet(models.Model):
  tweet = models.CharField(max_length=140)
  created_on = models.DateTimeField(default=datetime.now)
  processed = models.BooleanField(default=False)
  error_message = models.TextField(blank=True)

  def __str__(self):
    return self.tweet

  @staticmethod
  def next_tweet():
    tweet = Tweet.objects.filter(processed=False).order_by('-created_on')[:1]
    if not tweet:
      return None
    else:
      return tweet[0]

