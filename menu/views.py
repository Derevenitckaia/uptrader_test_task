from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from typing import Iterable
from itertools import chain
# Create your views here.


def show_item(request, item_id):

    context = {

    }

    return render(request, 'index.html', context)




