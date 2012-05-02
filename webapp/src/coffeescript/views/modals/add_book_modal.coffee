define [ 'jQuery', 'Underscore', 'Backbone'], ($, _, Backbone) ->
    AddBookModalView = Backbone.View.extend
        el : $ "#add-book-modal"
        
        initialize: ->
            # initialize the sign
            $("#add-book-modal-help").popover()

        events:
            "click button": "submit"
            
        submit: ->
            console.log "submitted!"
            false
            
    new AddBookModalView
        