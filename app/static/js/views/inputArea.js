define([
  'jquery', 'backbone',
  'text!templates/inputArea.html'
], function($, Backbone, InputAreaHtml) {  

  'use strict';

  var InputAreaView = Backbone.View.extend({

    className: 'row',
    template: _.template(InputAreaHtml),

    events: {

      'click button': 'submit'

    },

    initialize: function() {

    },

    render: function() {

      var $el = this.$el;
      $el.html(this.template());

    },

    submit: function(event) {
      var $el = this.$el;

      var textInput = $el.find('textarea').val();
      var option = $el.find('input[name="option"]').val();

      this.model.save({text: textInput, option: option});

    }

  });

  return InputAreaView;
});
