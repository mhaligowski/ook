define [
	'jQuery'
	'Underscore'
	'Backbone'
	'models/booklist'
	], ($, _, Backbone, Booklist) ->
		BooklistItemView = Backbone.View.extend
		    tagName    : 'li'
		    className  : 'navbar-booklist'
		    template   : _.template '<a href="#booklist/<%= id %>"><%= name %></a>'
		    initialize : ->
			# initialize the booklist_item. do nothing yet.
                        console.log "BooklistItemView.initialize"
		    render     : =>
                        ($ @el).html @template @model.toJSON()
                        @
                                
                BooklistsSubmenuView = Backbone.View.extend 
                    tagName    : 'li'
                    id         : 'navbar-books'
                    initialize : ->
                        console.log "BooklistSubmenuView.initialize"
                        $(".dropdown-toggle").dropdown()
                        
                        # initialize the items
                        @items = []
                            
                        for item in $ "li.navbar-booklist"
                            do (item) =>
                                booklistItem = new BooklistItemView $ item
                                @items.push booklistItem
                    
                    render      : =>
                        # 1. clear all booklist items
                        $("navbar-booklist").remove()
                        
                        # 2. for each elem in items render
                        #    and add to list
                        for item in @items
                            do (item) =>
                                ($ @).append item.render().el
                                
                        @

		NavbarView = Backbone.View.extend
                    tagName    : 'div'
                    id         : 'navbar-view'

                    initialize : ->
                        console.log "NavbarView.initialize"
                        # initialize submenu item
                        @booklistsItem = new BooklistsSubmenuView $ "#navbar-books"

                NavbarView