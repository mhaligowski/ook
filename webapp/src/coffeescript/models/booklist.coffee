define ['jQuery', 'Underscore', 'Backbone'], ($, _, Backbone) ->
    Backbone.RelationalModel.extend
        defaults:
            name  : "unknown"
            owner : $.cookie("api-user-url").replace(/["']/g,"")
        url: ->
            '/api/v1/booklist/'
