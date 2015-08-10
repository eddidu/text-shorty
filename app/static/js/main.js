'use strict';

require.config({
  baseUrl: 'static',
  paths: {
    'jquery': 'public/jquery/dist/jquery',
    'underscore': 'public/underscore/underscore',
    'backbone': 'public/backbone/backbone',
    'text': 'public/requirejs-text/text',
    'bootstrap': 'public/bootstrap/dist/js/bootstrap.min',
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
  'bootstrap',
  'jquery',
  'backbone',
  'js/views/app',
  'js/views/inputArea',
  'js/views/resultArea',
  'js/models/document'
], function(Bootstrap, $, Backbone, AppView, InputAreaView, ResultAreaView, Document) {
  // Backbone.history.start();

  // initialize the application view
  var doc = new Document();

  var inputAreaView = new InputAreaView({model: doc});
  var resultAreaView = new ResultAreaView({model: doc});

  var appView = new AppView();
  appView.addSubviews([inputAreaView, resultAreaView]);

  $('body').append(appView.el);

});
