define ['Underscore', 'Backbone'], (_, Backbone) ->
    Backbone.Model.extend
        defaults:
            id    : -1
            name  : "unknown"
            owner : null