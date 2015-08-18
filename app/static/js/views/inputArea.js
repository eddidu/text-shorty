define([
  'jquery', 'backbone',
  'text!templates/inputArea.html',
  'js/views/modal'
], function($, Backbone, InputAreaHtml, ModalView) {  

  'use strict';

  var InputAreaView = Backbone.View.extend({

    className: 'row',
    template: _.template(InputAreaHtml),

    events: {
      'click button': 'submit'
    },

    initialize: function() {
      this.listenTo(this.model, 'invalid', function(model, error) {
        this.showError(error);
      });      
    },

    render: function() {
      var $el = this.$el;

      $el.html(this.template());

      $el.find('input[name="option"][value="summary"]').prop('checked', true);
    },

    submit: function(event) {
      var $el = this.$el;

      var textInput = $el.find('textarea').val();
      var option = $el.find('input[name="option"]:checked').val();
      var data = {text: textInput, option: option};

      this.model.save(data);
    },

    showError: function(msg) {
      var modalView = new ModalView();

      modalView.setTitle('Error');
      modalView.setContent(msg);

      modalView.open();
    }

  });

  return InputAreaView;
});
