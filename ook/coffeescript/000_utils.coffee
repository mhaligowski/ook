###
Define some useful CScript functions
    
Author: Mateusz Haligowski <mhaligowski@googlemail.com>
Date started: 07-04-2012
###

namespace = (target, name, block) ->
  [target, name, block] = [(if typeof exports isnt 'undefined' then exports else window), arguments...] if arguments.length < 3
  top    = target
  target = target[item] or= {} for item in name.split '.'
  block target, top

###
confirmation box
###

confirm = (message, action) ->
    # some shortcuts
    confirmation_box = $("#confirmation-modal")
    modal_body = confirmation_box.find(".modal-body")
    yes_button = confirmation_box.find(".btn-success")
    no_button = confirmation_box.find(".btn-danger")
    
    # append the message    
    modal_body.empty().append(message)
    
    # handle the no button
    no_button.on "click", (event) ->
        # hide the modal
        confirmation_box.modal 'hide'
        
        # remove the handler
        no_button.off 'click'
        
        # do not do the link
        false
        
    # handle the yes button
    yes_button.on "click", (event) ->
        # do the action!
        action()
        
        # remove the handlers
        yes_button.off 'click'
        
        # hide the dialog
        confirmation_box.modal 'hide'
        
        # do not do the link
        false

    # show
    $("#confirmation-modal").modal 'show'
    
    
    