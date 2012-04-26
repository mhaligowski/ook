require.config
    paths :
        zepto: 'lib/zepto/zepto'
        Underscore: 'lib/underscore/underscore'
        Backbone: 'lib/backbone/backbone'

require [
    'app'
    
    #external libraries
    'lib/require/order!lib/zepto/zepto.min',
    'lib/require/order!lib/underscore/underscore.min',
    'lib/require/order!lib/backbone/backbone.min',
], (App) ->
    App.initialize()