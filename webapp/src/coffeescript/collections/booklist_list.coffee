define ['Underscore', 'Backbone', 'models/booklist'], (_, Backbone, Booklist) ->
    Backbone.Collection.extend
        model : Booklist
        
        initialize: ->
            console.log "initialize::BooklistCollection"