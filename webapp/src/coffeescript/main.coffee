require.config
    paths :
        jQuery: 'lib/jquery/jquery'
        Underscore: 'lib/underscore/underscore'
        Backbone: 'lib/backbone/backbone'
        
require [
    'app'
    
    #external libraries
    'lib/require/order!lib/jquery/jquery.min',
    'lib/require/order!lib/bootstrap/bootstrap.min'
    'lib/require/order!lib/underscore/underscore.min',
    'lib/require/order!lib/jquery/jquery.cookie'
    'lib/require/order!lib/backbone/backbone.min',
    'lib/require/order!lib/backbone/backbone-tastypie',
    'lib/require/order!lib/backbone/backbone-relational',
], (App) ->
    App.initialize()