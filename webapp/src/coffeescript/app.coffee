define [
    'jQuery'
    'Underscore'
    'Backbone'
    'router'
    'views/main_view'
    'views/navbar_view'
    ], ($, _, Backbone, Router, MainView, NavbarView) ->
    initialize: ->
        # initialize the history
        Router.initialize()
        
        # now, to the main views
        new NavbarView
        new MainView
        
