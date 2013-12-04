from django.http import HttpResponse
from django.shortcuts import render
from timesthermometer.comments.models import Comment
from timesthermometer.api.views import sentiment

def home(request):
  comments = []
  objects = list(Comment.objects.all())
  for obj in objects:
    user = {'name': obj.user.name, 'avatar': obj.user.avatar}
    comments.append({'pub_date': str(obj.pub_date), 'user': user, 'body': obj.comment, 'sentiment': sentiment(obj.comment)})
  context = { 'comment_list': comments }
  return render(request, 'comments/index.html', context)
