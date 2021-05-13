# coding=utf-8
from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    """Strona główna plikacji Dziennik Awarii."""
    return render(request, 'learning_2/index.html')


@login_required
def topics(request):
    """Wyświetlenie wszystkich tematów"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render (request, 'learning_2/topics.html', context)

@login_required
def topic(request, topic_id):
    """Wyświetla pojedynczy temat i wszystkie powiązane z nim wpisy."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic,  'entries': entries}
    return render (request, 'learning_2/topic.html', context)

@login_required
def new_topic(request):
    """Dodaj nowy temat."""
    if request.method != 'POST':
        #Nie przekazano żadnych danych, należy utworzyć pusty formularz.
        form = TopicForm()
    else:
        #Przekazano dane za pomocą żądania POST, należy je przetworzyć
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_2:topics')

    context = {'form': form}
    return render(request, 'learning_2/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Dodanie nowego wposu dla określonego tematu"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #Nie przekazano żadnych danych, należy utworzyć pusty formularz.
        form = EntryForm()
    else:
        #Przekazano dane za pomocą żądania POST, należy je przetworzyć
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_2:topic', topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_2/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edycja istniejącego wpisu."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        #Żądanie początkowe, wypełnienie formularza aktualną treścią wpisu
        form = EntryForm(instance = entry)

    else:
        #Przekazano dane za pomocą żądania POST, należy je przetworzyć
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_2:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_2/edit_entry.html', context)

