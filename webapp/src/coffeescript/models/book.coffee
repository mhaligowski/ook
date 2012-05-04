define ['Underscore', 'Backbone'], (_, Backbone) ->
    Backbone.RelationalModel.extend
        defaults:
            title     : "untitled"
            author    : "unknown"
