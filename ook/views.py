from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

from ook.utils import render_template
from books.models import Booklist

@login_required
def home_view(request):
    # get booklists for the user
    booklists = list(Booklist.objects.filter(owner = request.user))
    
    # render the mustache template
    booklists_html = render_template('navbar_booklist.mustache', { "booklists": booklists})
    print booklists_html
    
    return render_to_response('home_base.html',
                              { "booklists_html": booklists_html, },
                              context_instance = RequestContext(request))