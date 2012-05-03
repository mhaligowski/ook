define ['jQuery', 'Underscore', 'Backbone', 'models/book', 'collections/book_list'], ($, _, Backbone, Book, BookCollection) ->
    Backbone.RelationalModel.extend
        relations: [
            {
                type: Backbone.HasMany
                key: 'books'
                relatedModel: Book
                collectionType: BookCollection
                reverseRelation: {
                    key: 'booklist'
                }
            }
        ]
        defaults:
            name  : "unknown"
            owner : $.cookie("api-user-url").replace(/["']/g,"")
        url: ->
            '/api/v1/booklist/'
