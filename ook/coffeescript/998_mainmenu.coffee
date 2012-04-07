namespace "Ook.Mainmenu", (exports) ->

    ###
    Handler for clicking the Save button
    ###
    exports.modal_add_button = ->
        $(this).button 'loading'
        
        # get the values of the form
        values = {}
        
        for field in $ "#add-booklist-modal form input"
            do (field) ->
                values[$(field).attr "name"] = $(field).val()
        
        # send the form
        $.post(
            "/api/booklists/" # url
            values
            (data) ->
                # switch the classes
                $("#add-booklist-modal-input").removeClass "error"
                $("#add-booklist-modal-input").addClass "success"

                $("#add-booklist-modal-success").show()
                $("#add-booklist-modal-error").hide()
                
                # clear the data
                $("#add-booklist-modal form input").val ''

                # clear the dropdown list
                $(".navbar-booklist").remove()
                
                $("#navbar-books > ul > li.nav-header:first").after templates.navbar_booklist.render({ "booklists": data })
                
                # reset the button
                $("#add-booklist-modal-add-button").button 'reset'
                
        ).error -> # what if there is an error creating new booklist?
            $("#add-booklist-modal-input").addClass "error"
            
            $("#add-booklist-modal-success").hide()
            $("#add-booklist-modal-error").show()

            # reset the button
            $("#add-booklist-modal-add-button").button 'reset'

    exports.model_hidden = ->
        ###
        Reset the modal
        ###
        # clear the button
        $("#add-booklist-modal-add-button").button 'reset'
        
        # clear the style
        $("#add-booklist-modal-input").removeClass 'success', 'error'
    
        # hide the texts
        $("#add-booklist-modal .help-block").hide()

    
    exports.init = ->
        $("#add-booklist-modal-add-button").click ->
            exports.modal_add_button()
        
        $("#add-booklist-modal").on 'hidden', ->
            exports.model_hidden()
        
        # init modals
        $('#add-booklist-modal').modal show:false
