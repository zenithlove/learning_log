from django.shortcuts import render
from learning_logs.models import Topic
from .form import TopicForm
from .form import EntryForm
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,r"learning_logs\index.html")
    
@login_required    
def showtopics(request):
    #topics=Topic.objects.all()
    topics = Topic.objects.filter(owner=request.user).order_by('-add_time')
    for topic in topics:
        print(topic.id,topic)
    context = {'topics':topics}
    return render(request,r"learning_logs\topics.html",context)    
@login_required     
def showentry(request,topicindex):
    print("topicindex",topicindex)
    topic = Topic.objects.get(id=topicindex)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-time_added')
    context = {"topic":topic,"entries":entries}
    
    topic2 = Topic.objects.filter(id=topicindex)
    print("topic2",topic2)
    print("topicvvv",topic)
    return render(request,r"learning_logs\topic.html",context)    
    
@login_required     
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            print("********************addr is********************************** :\n",reverse('learning_logs:showtopics'),request.POST['text'])
            return HttpResponseRedirect(reverse('learning_logs:showtopics'))
            
    context = {'form':form}
    return render(request,r'learning_logs\new_topic.html',context)

@login_required 
def new_entry(request,topic_id):
    print("******************************************************")
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry= form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:showentry',args=[topic_id]))
    context = {'topic':topic,'form':form}
    return render(request,r'learning_logs\new_entry.html',context)

    


    