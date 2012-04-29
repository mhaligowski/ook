from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

from books.models import Booklist

@login_required
def home_view(request):
    return render_to_response('home_base.html', context_instance = RequestContext(request))