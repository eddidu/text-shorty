'use strict';

require.config({
    paths: {
        'jquery': '../public/jquery/dist/jquery',
        'underscore': '../public/underscore/underscore',
        'backbone': '../public/backbone/backbone',
        'text': '../public/requirejs-text/text',
        'bootstrap': '../public/bootstrap/dist/js/bootstrap.min',
    },
    shim: {
        underscore: {
            exports: '_'
        },
        backbone: {
            exports: 'Backbone',
            deps: ['jquery', 'underscore']
        },
        bootstrap: {
            deps: ['jquery']
        },
    }
    //deps: ['jquery', 'underscore', 'backbone', 'text', 'bootstrap']
});

require([
    'backbone',
    'views/app',
    'bootstrap'
], function(Backbone, AppView) {
    // Backbone.history.start();

    // initialize the application view
    new AppView();
});
