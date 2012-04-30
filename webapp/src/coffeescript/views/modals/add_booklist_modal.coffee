define [ 'jQuery', 'Underscore', 'Backbone', 'models/booklist' ], ($, _, Backbone, Booklist) ->
    AddBooklistModalView = Backbone.View.extend
        el : $("#add-booklist-modal")
        
        initialize: (options) ->
            @booklists = options.booklist
        
        events:
            'click #add-booklist-modal-add-button' : "addBooklist"
        
        addBooklist : (event) ->
            # change the button to loading (bootstrap trick)
            $("button").button 'loading'
            
            # create the booklist
            b = new Booklist
                name: $('input[name="name"]').val()
            
            # try to save the booklist
            b.save null, 
                beforeSend: (xhr) ->
                    xhr.setRequestHeader "Authorization", "ApiKey " + $.cookie("api-id") + ":" + $.cookie("api-key")
                success: (model, response) =>
                    @clearStatus()
                    @toggleSuccess()
                    
                    console.log model
                    console.log response
                    # add to the booklists
                    @booklists.add model
                error: (model, response) =>
                    @clearStatus()
                    @toggleError()

        clearStatus: ->
            $("#add-booklist-modal-input").removeClass "error success"
            $("#add-booklist-modal-success").hide()
            $("#add-booklist-modal-error").hide()
            
            $("#add-booklist-modal-add-button").button 'reset'
        toggleError: (msg) ->
            $("#add-booklist-modal-input").addClass "error"
            $("#add-booklist-modal-error").show()
            
        toggleSuccess: (msg) ->
            $("#add-booklist-modal-input").addClass "success"
            $("#add-booklist-modal-success").show()

        reset: ->
            $("#add-booklist-modal form input").val ''

