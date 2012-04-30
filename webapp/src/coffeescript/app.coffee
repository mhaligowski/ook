define [
    'jQuery'
    'Underscore'
    'Backbone'
    'router'
    'views/main_view'
    'views/navbar_view'
    'collections/booklist_list'
    ], ($, _, Backbone, Router, MainView, NavbarView, BooklistCollection) ->
    initialize: ->
        console.log "initialize"
        
        # initialize the history
        Router.initialize()

        # initialize collections
        b = new BooklistCollection
        
        # now, to the main views
        new NavbarView
            el: $ "#navbar-view"
            booklist: b
            
        new MainView
            el: $ "#main-view"
            booklist: b
        
