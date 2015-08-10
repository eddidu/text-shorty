define([
  'jquery', 'backbone',
  'text!templates/resultArea.html'
], function($, Backbone, ResultAreaHtml) {  

  'use strict';

  var ResultAreaView = Backbone.View.extend({

    className: 'row',
    template: _.template(ResultAreaHtml),

    initialize: function() {

      this.listenTo(this.model, 'change', function() {
        this.render();
      });

    },

    render: function() {

      var $el = this.$el;
      $el.html(this.template(this.model.toJSON()));

    }

  });

  return ResultAreaView;
});
