from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import BooklistHandler
from piston.authentication import OAuthAuthentication

# auth = OAuthAuthentication()
# booklist_handler = Resource(BooklistHandler, auth)

booklist_handler = Resource(BooklistHandler)

urlpatterns = patterns('',
   url(r'booklist/(?P<booklist_id>[^/]+)/', booklist_handler),
   url(r'booklists/', booklist_handler),
)