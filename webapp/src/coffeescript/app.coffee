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
        # initialize collections
        b = new BooklistCollection 
        
        # now, to the main views
        NavbarView.setBooklists b
        MainView.setBooklists b
                    
        # set the booklist data (now, as the events are binded)
        b.add initial_booklist_data

        # initialize the history
        Router.initialize()
        
        # setInterval
        setInterval ->
                b.fetch 
                    beforeSend: (xhr) ->
                        xhr.setRequestHeader "Authorization", "ApiKey " + $.cookie("api-id") + ":" + $.cookie("api-key")
                    add: true
            , 5 * 60 * 1000 #every two minutes