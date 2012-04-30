define [
    'jQuery'
    'Underscore'
    'Backbone'
    'router'
    'views/main_view'
    'views/navbar_view'
    'views/modals/add_booklist_modal'
    ], ($, _, Backbone, Router, MainView, NavbarView, AddBooklistModal) ->
    initialize: ->
        # initialize the history
        Router.initialize()
        
        # now, to the main views
        new NavbarView $ "#navbar-view"
        new MainView $ "#main-view"
        
        # initialize modals 
        new AddBooklistModal $ "#add-booklist-modal"