from piston.handler import BaseHandler
from books.models import Booklist



class BooklistHandler(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'POST', 'DELETE')
    model = Booklist
    exclude = ('owner',)
    
    def read(self, request, booklist_id = None):
        """Returns a single booklist if booklist_id is given, else returns a subset"""
        
        base = Booklist.objects
        
        if booklist_id:
            return base.get(pk = booklist_id)
        else:
            return base.filter(owner = request.user)

            
    def create(self, request):
        """ Creates new booklist """
        if request.POST and request.POST["booklist_name"]:
            b = Booklist.objects.create(name = request.POST["booklist_name"], owner = request.user)
            return list(Booklist.objects.filter(owner = request.user))
    
    def update(self, request):
        pass
    
    def delete(self, request):
        pass
    