define [
    'zepto'
    'Underscore'
    'Backbone'
    'router'
    ], ($, _, Backbone, Router) ->
    initialize: ->
        Router.initialize()
        
        # initialize bootstrap dropdown menus
