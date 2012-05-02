define [
    'jQuery'
    'Underscore'
    'Backbone'
    'models/booklist'
    ], ($, _, Backbone, Booklist) ->
        PagePaginator = Backbone.View.extend
            initialize: (options) ->
                console.log options
            
        BooklistView = Backbone.View.extend
            el: $ "#booklist-view"
        
            initialize: ->
                @title = @.$ "#booklist-title"
                
            setBooklist: (booklist, clbk) ->
                @booklist = booklist
                
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