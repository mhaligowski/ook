from tastypie.validation import Validation
from django.core.urlresolvers import resolve

class BookValidation(Validation):
    def is_valid(self, bundle, request=None):
        return getattr(self, 'validate_%s' % request.method.lower())(bundle, request)
                
    def validate_post(self, bundle, request):
        # first, resolve the url from the request
        url_data = resolve(request.path).kwargs
        
        # if given by booklist-relative url, then validate the booklist
        if 'parent_resource_name' in url_data and url_data['parent_resource_name'] == u'booklist':
            # get the booklist id from the url
            booklist_id = url_data['parent_pk']
            
            # get the booklist in the post payload
            payload_url_data = resolve(bundle.data["booklist"]).kwargs
            
            if url_data['parent_resource_name'] == payload_url_data['resource_name'] \
                and url_data['parent_pk'] == payload_url_data['pk']:
                return {}
            else:
                return {
                    'booklist' : 'Given booklists do not match'
                }
    
        
        # in case there is nothing to validate    
        return {}
        
    def validate_get(self, bundle, request=None):
        """
        Make sure that if the request is relational, the parent booklist is also the child's booklist
        """
        print "i'm here"
        return {}
        
    def validate_delete(self, bundle, request=None):
        return {}
        
    def validate_put(self, bundle, request=None):
        return {}
