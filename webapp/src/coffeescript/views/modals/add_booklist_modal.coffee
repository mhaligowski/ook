define [
    'jQuery'
    'Underscore'
    'Backbone'
    ], ($, _, Backbone) ->
    AddBooklistModalView = Backbone.View.extend
        el : $("#add-booklist-modal")
        initialize: ->
            console.log "AddBooklistModalView"
        events:
            'click #add-booklist-modal-add-button' : "addBooklist"
        addBooklist : (event) ->
            console.log "addBooklist"