from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Parametro

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    

    def get_queryset(self):
        """Return the last five published questions."""
        #return Question.objects.order_by('-pub_date')[:5]
        print(Parametro.objects.all())
        return Parametro.objects.all()[:1]
