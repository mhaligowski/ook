define [
	'jQuery'
	'Underscore'
	'Backbone'
	'models/booklist'
	'collections/booklist_list'
	'views/modals/add_booklist_modal'
	], ($, _, Backbone, Booklist, BooklistCollection, AddBooklistModal) ->
		BooklistItemView = Backbone.View.extend
			tagName : 'li'
			className : 'navbar-booklist'
			template : _.template '<a href="#booklist/<%= id %>"><%= name %></a>'
			render : ->
				($ @el).html @template @model.toJSON()
				@
			
		BooklistsSubmenuView = Backbone.View.extend 
			tagName : 'li'
			id : 'navbar-books'
			el: $ "#navbar-books"
			initialize : ->
				$(".dropdown-toggle").dropdown()
				@render()
				
			render : ->
				# 1. clear all booklist items
				$("li.navbar-booklist").remove()

				# 2. find the divider - items will be added BEFORE
				elem = @.$el.find "ul.dropdown-menu > li.divider"
				
				# 3. for each elem in items render
				#    and add to list
				if @booklists
					@booklists.each (item) ->
						blv = new BooklistItemView
							model: item
						
						elem.before blv.render().el

				@
			setBooklists: (booklists) ->
				@booklists = booklists
				@booklists.bind "add", @render, @
				
		NavbarView = Backbone.View.extend
			tagName : 'div'
			id : 'navbar-view'
			el: $ "#navbar-view"

			initialize : (options) ->
				# initialize submenu item
				@booklistsItem = new BooklistsSubmenuView
					
				# initialize modal
				new AddBooklistModal
					el: $ "#add-booklist-modal"
					
			setBooklists: (booklists) ->
				@booklists = booklists
				@booklistsItem.setBooklists booklists
				
				
		new NavbarView