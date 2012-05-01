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
			initialize : (options) ->
				$(".dropdown-toggle").dropdown()

				@booklists = options.booklists

				@booklists.fetch
					beforeSend: (xhr) ->
						xhr.setRequestHeader "Authorization", "ApiKey " + $.cookie("api-id") + ":" + $.cookie("api-key")
					success: =>
						@render()
				
				# when a booklist is added, addItem
				@booklists.bind 'add', @addItem, @
				
			render : ->
				# 1. clear all booklist items
				$("li.navbar-booklist").remove()

				# 2. find the divider - items will be added BEFORE
				elem = @.$el.find "ul.dropdown-menu > li.divider"
				
				# 3. for each elem in items render
				#    and add to list
				@booklists.each (item) =>
					blv = new BooklistItemView
						model: item
					
					elem.before blv.render().el

				@
				
			addItem : (item) ->
				@render()

		NavbarView = Backbone.View.extend
			tagName : 'div'
			id : 'navbar-view'
			
			initialize : (options) =>
				# initialize booklist collection
				@booklists = options.booklist
				
				# initialize submenu item
				@booklistsItem = new BooklistsSubmenuView
					el: $ "#navbar-books"
					booklists: @booklists
				
				# initialize modal
				new AddBooklistModal
					el: $ "#add-booklist-modal"
					booklists: @booklists
					
		NavbarView