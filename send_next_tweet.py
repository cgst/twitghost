#!/usr/bin/env python
import logging
from os import path, environ
import sys

import twitter

environ['DJANGO_SETTINGS_MODULE'] = 'twitghost.settings'
module_path = path.abspath(path.join(path.dirname(__file__), '..'))
sys.path.append(module_path)
from twitghost.server.models import Tweet
from twitghost import settings


def main(arv):
  tweet = Tweet.next_tweet()
  if not tweet:
    logging.debug("Nothing to tweet")
    return
  else:
    logging.debug("Will send tweet: \"%s\"" % tweet.tweet.encode('utf-8'))
  api = twitter.Api(username=settings.TWITTER_USERNAME,
      password=settings.TWITTER_PASSWORD)
  try:
    status = api.PostUpdate(tweet.tweet)
    tweet.processed = True
    tweet.save()
    logging.debug("Tweet sent")
  except Exception, e:
    logging.error("Couldn't tweet: %s" % e.msg)
    tweet.error_message = str(e)
    tweet.processed = True
    tweet.save()
    sys.exit(1)

if "__main__" == __name__:
  main(sys.argv)

