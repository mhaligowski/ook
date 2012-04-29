define [ "jQuery", "Underscore", "Backbone"], ($, _, Backbone, Session) ->
  AppRouter = Backbone.Router.extend(
    routes:
      "booklist/:booklistId": "showBooklist"
      "users": "showUsers"
      "*actions": "defaultAction"

    showBooklist: (booklistId) ->
      console.log "showBooklist", booklistId

    showUsers: ->
      console.log "showUsers"

    defaultAction: (actions) ->
      console.log "No route:", actions
  )
  
  initialize: ->
    app_router = new AppRouter
    Backbone.history.start()
