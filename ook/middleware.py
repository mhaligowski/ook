import string
from django.core.urlresolvers import reverse

class SessionVariablesMiddleware(object):
    def process_response(self, request, response):

        if hasattr(request, "user") and request.user.is_authenticated():
            cookie_value = reverse("api_dispatch_detail",
                                    kwargs={"api_name":"v1",
                                            "resource_name":"auth/user",
                                            "pk":request.user.id})
            
            response.set_cookie(key = "api-user-url",
                                value = cookie_value,
                                httponly = False)
        else:
            response.delete_cookie("api-user-url")
        
        return response