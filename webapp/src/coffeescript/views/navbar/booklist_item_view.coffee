define [
	'jQuery'
	'Underscore'
	'Backbone'
	], ($, _, Backbone) ->
		BooklistItemView = Backbone.View.extend
			tagName    : 'li'
			className  : 'navbar-booklist'
			template   : _.template('<a href="#booklist/<%= id %>"><%= name %></a>')
			initialize : ->
				# initialize the booklist_item. do nothing yet.
			render     : ->
				($ @el).html @template @model.toJSON()
				@