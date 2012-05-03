define ['Underscore', 'Backbone', 'models/book'], (_, Backbone, Book) ->
    Backbone.Collection.extend
        model : Book
        url: ->
            '/api/v1/booklist/'