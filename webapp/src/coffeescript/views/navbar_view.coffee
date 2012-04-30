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
			initialize : =>
				# initialize the booklist_item. do nothing yet.
				console.log "BooklistItemView.initialize"
			render : =>
				($ @el).html @template @model.toJSON()
				@
			
		BooklistsSubmenuView = Backbone.View.extend 
			tagName : 'li'
			id : 'navbar-books'
			initialize : (options) =>
				console.log "BooklistSubmenuView.initialize"
				$(".dropdown-toggle").dropdown()
				
				# initialize the items
				@booklist = options.booklist
				
				for item in $ "li.navbar-booklist"
					do (item) =>
						booklistItem = new BooklistItemView $ item
						@booklist.push booklistItem.model
				
			render : =>
				# 1. clear all booklist items
				$("navbar-booklist").remove()
				
				# 2. for each elem in items render
				#    and add to list
				for item in @items
					do (item) =>
						($ @).append item.render().el
				@

		NavbarView = Backbone.View.extend
			tagName : 'div'
			id : 'navbar-view'
			
			initialize : (options) =>
				console.log "NavbarView.initialize"
				
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