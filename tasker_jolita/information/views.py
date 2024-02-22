from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import gettext_lazy as _
from . import models

def information_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'information/information_list.html', {
        'information_list': models.Information.objects.all(),
    })
   
def information_detail(request: HttpRequest, pk:int) -> HttpResponse:
    return render(request, 'information/information_detail.html', {
        'information': get_object_or_404(models.Information, pk=pk),
    })    
