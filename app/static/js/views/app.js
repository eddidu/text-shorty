define([
  'jquery', 'underscore', 'backbone', 
  'text!templates/app.html',
  'js/views/modal'
], function($, _, Backbone, AppHtml, ModalView) {  
  'use strict';

  var AppView = Backbone.View.extend({
    className: 'container',
    template: _.template(AppHtml),

    events: {

    },

    initialize: function() {
      this.subviews = [];
      this.render();

    },

    render: function() {
      var $el = this.$el;

      $el.html(this.template());

    },

    addSubview: function(view) {
      var $el = this.$el;

      if(!!view && view.$el) {
        view.render();
        $el.append(view.el);
      }

    },

    addSubviews: function(views) {
      var self = this;

      _.each(views, function(view) {
        self.addSubview(view);
      });

    }

  });

  return AppView;

});
