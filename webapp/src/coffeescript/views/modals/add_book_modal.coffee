define [ 'jQuery', 'Underscore', 'Backbone'], ($, _, Backbone) ->
    AddBookModalView = Backbone.View.extend
        el : $ "#add-book-modal"
        
        initialize: ->
            # initialize the sign
            $("#add-book-modal-help").popover()

        events:
            "click button": "submit"
            
        submit: ->
            # get the data
            data = {}
            for item in @.$("form").serializeArray()
                do (item) ->
                    data[item.name] = item.value

            # it's a form not to be sent
            false
            
        setBooklist: (booklist) ->
            @booklist = booklist
            
    new AddBookModalView
        