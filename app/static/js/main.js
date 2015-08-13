require([
  'jquery',
  'bootstrap',
  'backbone',
  'js/views/app',
  'js/views/inputArea',
  'js/views/resultArea',
  'js/models/document'
], function($, Bootstrap, Backbone, AppView, InputAreaView, ResultAreaView, Document) {
  'use strict';

  // Backbone.history.start();

  // initialize the application view
  var doc = new Document();

  var inputAreaView = new InputAreaView({model: doc});
  var resultAreaView = new ResultAreaView({model: doc});

  var appView = new AppView();
  appView.addSubviews([inputAreaView, resultAreaView]);

  $('body').append(appView.el);

});
