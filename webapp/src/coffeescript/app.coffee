define [
    'jQuery'
    'Underscore'
    'Backbone'
    'router'
    'views/main_view'
    'views/navbar_view'
    ], ($, _, Backbone, Router, MainView, Navbar) ->
    initialize: ->
        # initialize bootstrap and shit
        $(".dropdown-toggle").dropdown()

        # initialize the history
        Router.initialize()
        
        # now, to the main views
        navBarMainView = Navbar.mainView
        new navBarMainView
        new MainView
        
