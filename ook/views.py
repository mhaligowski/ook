from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core import serializers
from api.handlers import BooklistResource

from books.models import Booklist

@login_required
def home_view(request):
    br = BooklistResource()
    booklists = br.get_object_list(request)
    
    br_list = []
    for booklist in booklists:    
        br_bundle = br.build_bundle(obj=booklist, request = request)
        br_bundle = br.full_dehydrate(br_bundle)
        br_list.append(br_bundle)
        
    
    return render_to_response('home_base.html',
                              { 'initial_data': br.serialize(request, br_list, 'application/json') },
                              context_instance = RequestContext(request)
                              )