define [ 'jQuery', 'Underscore', 'Backbone', 'models/booklist' ], ($, _, Backbone, Booklist) ->
    AddBooklistModalView = Backbone.View.extend
        el : $("#add-booklist-modal")
        
        initialize: (options) =>
            console.log "AddBooklistModalView.initialize"
            @booklist = options.booklist
        
        events:
            'click #add-booklist-modal-add-button' : "addBooklist"
        
        addBooklist : (event) =>
            console.log "addBooklist"
        
            b = new Booklist
                id : 1000
                name: "newTitle"
            
            @booklist.add b
