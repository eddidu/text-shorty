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
    },

    validate: function(attrs) {
      if( attrs.option === 'summary' && attrs.text.length < 500 ) {
        return 'The document must have more than 500 characters to summarize';
      }
      if( attrs.option === 'keywords' && attrs.text.length < 40) {
        return 'The document must have more than 40 characters to extract keywords';
      }
    }

  });

  return Document;

});