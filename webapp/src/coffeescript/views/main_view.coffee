define [
    'jQuery'
    'Underscore'
    'Backbone'
    ], ($, _, Backbone) ->
        MainView = Backbone.View.extend
            el: $("#main-view")

            initialize: ->
                console.log "initialize MainView"
