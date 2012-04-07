init = ->
    # init dropdowns
    $('.dropdown-toggle').dropdown()
    
    # init buttons
    $('.btn').button()
    
$ ->
    init()
    Ook.Mainmenu.init()
    Ook.Booklists.init()