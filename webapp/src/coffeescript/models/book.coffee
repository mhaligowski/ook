define ['Underscore', 'Backbone'], (_, Backbone) ->
    Backbone.RelationalModel.extend
        defaults:
            id        : -1
            title     : "untitled"
            author    : "unknown"
            booklist  : "unknown"