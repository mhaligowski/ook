from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import BooklistHandler, BookHandler
from piston.authentication import OAuthAuthentication

# auth = OAuthAuthentication()
# booklist_handler = Resource(BooklistHandler, auth)

booklist_handler = Resource(BooklistHandler)
book_handler = Resource(BookHandler)

urlpatterns = patterns('',
   url(r'booklists/', booklist_handler),
   url(r'booklist/(?P<booklist_id>[^/]+)/$', booklist_handler),
   url(r'booklist/(?P<booklist_id>[^/]+)/books', book_handler),
   
)