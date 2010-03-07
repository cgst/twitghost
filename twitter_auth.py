#!/usr/bin/env python
import tweepy

import settings


if __name__ == "__main__":
  auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY,
      settings.TWITTER_CONSUMER_SECRET)
  print "Authorization URL: %s" % auth.get_authorization_url()
  pin = raw_input('Verification pin number from twitter.com: ').strip()
  token = auth.get_access_token(verifier=pin)
  print 'Access token:'
  print '  Key: %s' % token.key
  print '  Secret: %s' % token.secret

