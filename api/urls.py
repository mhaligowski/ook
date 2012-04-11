from django.conf.urls.defaults import *
from tastypie.api import Api
import handlers

v1_api = Api(api_name = 'v1')
v1_api.register(handlers.BooklistResource())
v1_api.register(handlers.BookResource())
v1_api.register(handlers.UserResource())

urlpatterns = patterns('',
                       (r'/', include(v1_api.urls)),
                       )