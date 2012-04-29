define ['Underscore', 'Backbone'], (_, Backbone) ->
    Backbone.Model.extend
        defaults:
            id        : -1
            title     : "untitled"
            author    : "unknown"
            booklist  : "unknown"