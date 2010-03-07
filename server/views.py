import logging
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Tweet
from twitghost import settings

@login_required
def list(request):
  scheduled = Tweet.objects.filter(processed=False).order_by('-created_on')
  processed = Tweet.objects.filter(processed=True).order_by('-created_on')
  return render_to_response('list.html', dict(scheduled=scheduled,
      processed=processed))

def schedule(request):
  if request.POST.get('auth') != settings.TWITGHOST_AUTH_KEY:
    logging.error("Unauthorized access")
    return HttpResponse('forbidden', status=403)
  new_tweet = Tweet(tweet=request.POST['tweet'],
      username=settings.TWITTER_USERNAME)
  new_tweet.save()
  return HttpResponse('ok', mimetype="text/xml")

