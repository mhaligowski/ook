define [
	'jQuery'
	'Underscore'
	'Backbone'
	'models/booklist'
	], ($, _, Backbone, Booklist) ->
		BooklistItemView = Backbone.View.extend
		    tagName    : 'li'
		    className  : 'navbar-booklist'
		    template   : _.template('<a href="#booklist/<%= id %>"><%= name %></a>')
		    initialize : ->
			# initialize the booklist_item. do nothing yet.
                        console.log "BooklistItemView.initialize"
		    render     : ->
                        ($ @el).html @template @model.toJSON()
                        @
                                
                BooklistsSubmenuView = Backbone.View.extend
                    el: $("#navbar-books")
                    initialize: ->
                        console.log "BooklistSubmenuView.initialize"

                        # initialize booklists
			for item in @$ ".navbar-booklist"
                            do (item) ->
                                new BooklistItemView
                        
		NavbarView = Backbone.View.extend
		    el: $("#navbar-view")
		    initialize: ->
                        console.log "NavbarView.initialize"
                        
                        # initialize submenu item
                        @booklistsItem = new BooklistsSubmenuView
                                
		    clearBooks: ->
                        # this is shortcut for this.$(query)
                        console.log "clearBooks"

                output =
                    mainView             : NavbarView
                    booklistsSubmenuView : BooklistsSubmenuView
                    booklistItemView     : BooklistItemView

                output