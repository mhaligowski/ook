define ['Underscore', 'Backbone', 'models/booklist'], (_, Backbone, Booklist) ->
    Backbone.Collection.extend
        model : Booklist
        url: ->
            '/api/v1/booklist/'