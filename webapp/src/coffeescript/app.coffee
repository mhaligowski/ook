define [
    'jQuery'
    'Underscore'
    'Backbone'
    'router'
    'views/main_view'
    'views/navbar/navbar_view'
    ], ($, _, Backbone, Router, MainView, NavbarView) ->
    initialize: ->
        # initialize bootstrap and shit
        $(".dropdown-toggle").dropdown()

        # initialize the history
        Router.initialize()
        
        # now, to the main views
        new MainView
        new NavbarView
