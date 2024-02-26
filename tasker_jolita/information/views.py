from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
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

@login_required
def information_like(request: HttpRequest, pk: int) -> HttpResponse:
    information = get_object_or_404(models.Information, pk=pk)
    like = models.InformationLike.objects.filter(information=information, user=request.user).first()
    if not like:
        models.InformationLike.objects.create(information=information, user=request.user)
    else:
        like.delete()
    if request.GET.get('next'):
        return redirect(request.GET.get('next'))
    return redirect('information_list')