from django.http import HttpResponse

def home(request):
  return HttpResponse('')

import sentiment_analysis
from sentiment_analysis import Splitter, POSTagger, DictionaryTagger, sentiment_score
from dictionaries.models import Positive, Negative, Incrementer, Decrementer, Inverter
from pprint import pprint

def sentiment(text):

  positive = {}
  negative = {}
  inc = {}
  dec = {}
  inv = {}

  for e in list(Positive.objects.all()):
    positive[str(e.label)] = ['positive']

  for e in list(Negative.objects.all()):
    negative[str(e.label)] = ['negative']

  for e in list(Incrementer.objects.all()):
    inc[str(e.label)] = ['inc']

  for e in list(Decrementer.objects.all()):
    dec[str(e.label)] = ['dec']

  for e in list(Inverter.objects.all()):
    inv[str(e.label)] = ['inv']

  splitter = Splitter()
  postagger = POSTagger()
  dicttagger = DictionaryTagger([positive, negative, inc, dec, inv])
  splitted_sentences = splitter.split(text)
  pos_tagged_sentences = postagger.pos_tag(splitted_sentences)
  dict_tagged_sentences = dicttagger.tag(pos_tagged_sentences)
  score = sentiment_score(dict_tagged_sentences)

  return score

import json
from comments.models import Comment

def comments(request):
  comments = []
  objects = list(Comment.objects.all())
  for obj in objects:
    user = {'name': obj.user.name, 'avatar': obj.user.avatar}
    comments.append({'pub_date': str(obj.pub_date), 'user': user, 'comments': obj.comment, 'sentiment': sentiment(obj.comment)})

  if 'callback' in request.REQUEST:
    data = json.dumps(comments)
    data = '%s(%s);' % (request.REQUEST['callback'], data)
    return HttpResponse(data, 'text/javascript')
  else:
    return HttpResponse(json.dumps(comments), 'application/json')

