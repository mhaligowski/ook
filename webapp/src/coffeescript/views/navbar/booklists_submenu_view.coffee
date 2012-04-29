define [
    'jQuery'
    'Underscore'
    'Backbone'
    ], ($, _, Backbone) ->
	BooklistsMenuItemView = Backbone.View.extend
	    el: $("#navbar-books")
	    initialize: ->
		alert "dupa"