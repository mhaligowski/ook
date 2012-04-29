define [
	'jQuery'
	'Underscore'
	'Backbone'
	'views/navbar/booklist_item_view'
	'models/booklist'
	], ($, _, Backbone, BooklistItemView, Booklist) ->
		NavbarView = Backbone.View.extend
			el: $("#navbar-view")
	    
			initialize: ->
				for item in @$ ".navbar-booklist"
					do (item) ->
						new BooklistItemView 
							el: $ item
							
				# experiment - try creating new booklist model
				b = new Booklist
					id: 7
					name: "testBooklist"
				
				bv = new BooklistItemView
					model: b
					
				console.log bv.render()

			clearBooks: ->
				# this is shortcut for this.$(query)
