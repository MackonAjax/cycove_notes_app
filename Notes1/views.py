from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Note
from django.urls import reverse
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'notes1/index.html'
    context_object_name = 'notes'

    def get_queryset(self) -> QuerySet[Any]:
        return Note.objects.all().values()[::-1]


class DetailView(generic.DetailView):
    model = Note
    template_name = 'notes1/detail.html'

"""
def index(request):
    notes = Note.objects.all().values()[::-1]
    return render(request, 'notes1/index.html', {'notes':notes})

"""
def add(request):
    try:
        title = request.POST['title']
        detail = request.POST['detail_text']
    except:
        return render(request, 'notes1/add.html')
    else:
        note = Note(title=title, detail=detail)
        note.save()
        return HttpResponseRedirect(reverse('notes1:index'))
    

def detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'notes1/detail.html', {'note':note})

def delete(request, note_id):
    note = Note.objects.get(pk=note_id)
    note.delete()
    return HttpResponseRedirect(reverse('notes1:index'))