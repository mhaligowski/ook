define(
    ['lib/require/order!lib/backbone/backbone.min'],
    function(){
        _.noConflict();
        $.noConflict();
        return Backbone.noConflict();
    }
);