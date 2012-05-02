define [
    'jQuery'
    'Underscore'
    'Backbone'
    'views/main/booklist_view'
    ], ($, _, Backbone, BooklistView) ->
        MainView = Backbone.View.extend
            el: $ "#main-container"

            initialize: ->
                @views =
                    booklists: BooklistView

            showBooklist: (booklistId) ->
                booklist = @booklists.get booklistId

                @views.booklists.setBooklist @booklists.get(booklistId), =>
                    @views.booklists.render()
                    @views.booklists.show()
                    
            setBooklists: (booklists) ->
                @booklists = booklists
                
        return new MainView