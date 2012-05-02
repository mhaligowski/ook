define [
    'jQuery'
    'Underscore'
    'Backbone'
    'models/booklist'
    'views/modals/add_book_modal'
    ], ($, _, Backbone, Booklist, AddBookModal) ->
        PagePaginator = Backbone.View.extend
            initialize: (options) ->
                console.log options
            
        BooklistView = Backbone.View.extend
            el: $ "#booklist-view"
        
            initialize: ->
                # make title element
                @title = @.$ "#booklist-title"
                
                #initialize modal
                
                
            setBooklist: (booklist, clbk) ->
                @booklist = booklist
                
                # issue booklist to modal
                
                if clbk
                    clbk()
                
            render: ->
                console.log "render"
                if @booklist
                    @title.html @booklist.get "name"
                @
                
            show: ->
                @.$el.show()
        
        new BooklistView