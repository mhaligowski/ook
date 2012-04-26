define [ "zepto", "Underscore", "Backbone"], ($, _, Backbone, Session) ->
  AppRouter = Backbone.Router.extend(
    routes:
      "projects": "showProjects"
      "users": "showUsers"
      "*actions": "defaultAction"

    showProjects: ->
      console.log "showProject"

    showUsers: ->
      console.log "showUsers"

    defaultAction: (actions) ->
      console.log "No route:", actions
  )
  
  initialize: ->
    app_router = new AppRouter
    Backbone.history.start()
