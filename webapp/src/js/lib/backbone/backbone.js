define(
    ['lib/require/order!lib/backbone/backbone.min'],
    function(){
        _.noConflict();
        return Backbone.noConflict();
    }
);