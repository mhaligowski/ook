namespace "Ook.Mainmenu", (exports) ->

    ###
    Handler for clicking the Save button
    ###
    exports.modal_add_button = ->
        $(this).button 'loading'

        formData = {}
        
        for elem in $("#add-booklist-modal form input").serializeArray()
            do (elem) ->
                formData[elem.name] = elem.value
        
        formData["owner"] = eval $.cookie "api-user-url"
        
        # send the form
        $.ajax
            url: "/api/v1/booklist/" # url
            data: JSON.stringify formData
            type: "POST"
            contentType: "application/json"
            dataType: 'json'
            processData: false
            headers:
                "Authorization": sprintf "ApiKey %s:%s", $.cookie("api-id"), $.cookie("api-key")
            success: (data) ->
                # switch the classes
                $("#add-booklist-modal-input").removeClass "error"
                $("#add-booklist-modal-input").addClass "success"

                $("#add-booklist-modal-success").show()
                $("#add-booklist-modal-error").hide()
                
                # clear the data
                $("#add-booklist-modal form input").val ''

                # clear the dropdown list
                $("#navbar-books > ul > li.divider").before templates.navbar_booklist.render "booklists": [ data ]
                
                # reset the button
                $("#add-booklist-modal-add-button").button 'reset'
            error: -> # what if there is an error creating new booklist?
                $("#add-booklist-modal-input").addClass "error"
            
                $("#add-booklist-modal-success").hide()
                $("#add-booklist-modal-error").show()
    
                # reset the button
                $("#add-booklist-modal-add-button").button 'reset'

    exports.modal_hidden = ->
        ###
        Reset the modal
        ###
        # clear the button
        $("#add-booklist-modal-add-button").button 'reset'
        
        # clear the style
        $("#add-booklist-modal-input").removeClass 'success', 'error'
    
        # hide the texts
        $("#add-booklist-modal .help-block").hide()

    exports.go_to_booklist_view = (booklist_id, booklist_name) ->
        Ook.Booklists.init_view booklist_id, booklist_name
    
    exports.init = ->
        $("#add-booklist-modal-add-button").click ->
            exports.modal_add_button()
        
        $("#add-booklist-modal").on 'hidden', ->
            exports.modal_hidden()
        
        # init modals
        $('#add-booklist-modal').modal show:false
        $('#confirmation-modal').modal show:false

        $(".navbar-booklist a").click ->
            d = $(this).parent().data()
            exports.go_to_booklist_view d.booklistId, d.booklistName