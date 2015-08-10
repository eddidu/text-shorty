define([
  'jquery', 
  'backbone'
], function($, Backbone) {

  var Document = Backbone.Model.extend({

    defaults: {
      text: '',
      option: '',
      result: []
    },

    url: function() {
      return 'api/' + this.attributes.option
    }

  });

  return Document;

});