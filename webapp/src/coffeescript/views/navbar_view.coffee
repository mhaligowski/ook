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
				
				# initialize the items
				@booklists = options.booklist
				
				_.each $("li.navbar-booklist"), (item) =>
					booklistItem = new BooklistItemView $ item
					@booklists.push booklistItem.model
						
				# when a booklist is added, addItem
				@booklists.bind 'add', @addItem, @
				
			render : ->
				# 1. clear all booklist items
				$("li.navbar-booklist").remove()
				
				# 2. for each elem in items render
				#    and add to list
				@booklists.each (item) ->
					console.log item
					blv = new BooklistItemView
						model: item
					($ @).append blv.render().el
				@
				
			addItem : (item) ->
				@render()

		NavbarView = Backbone.View.extend
			tagName : 'div'
			id : 'navbar-view'
			
			initialize : (options) =>
				# initialize booklist collection
				@booklist = options.booklist
				
				# initialize submenu item
				@booklistsItem = new BooklistsSubmenuView
					el: $ "#navbar-books"
					booklist: @booklist
				
				# initialize modal
				new AddBooklistModal
					el: $ "#add-booklist-modal"
					booklist: @booklist
					
		NavbarView