'use strict';

require.config({
  baseUrl: 'static',
  paths: {
    'jquery': 'public/jquery/dist/jquery',
    'underscore': 'public/underscore/underscore',
    'backbone': 'public/backbone/backbone',
    'text': 'public/requirejs-text/text',
    'bootstrap': 'public/bootstrap/dist/js/bootstrap.min'
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
    },
  deps: ['js/main']
  //deps: ['jquery', 'underscore', 'backbone', 'text', 'bootstrap']
});
