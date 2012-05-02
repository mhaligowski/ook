define [ "jQuery",
        "Underscore",
        "Backbone",
        "views/main_view"], ($, _, Backbone, MainView) ->
  AppRouter = Backbone.Router.extend(
    routes:
      "booklist/:booklistId": "showBooklist"
      "*actions": "defaultAction"

    showBooklist: (booklistId) ->
      MainView.showBooklist booklistId
    
    defaultAction: (actions) ->
      console.log "No route:", actions
  )
  
  initialize: ->
    app_router = new AppRouter
    Backbone.history.start()
