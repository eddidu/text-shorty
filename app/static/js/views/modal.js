define([
    'bootstrap', 
    'jquery', 'underscore', 'backbone',
    'text!templates/modal.html'
], function(Bootstrap, $, _, Backbone, ModalHtml) {  

  'use strict';

  var BaseModalView = Backbone.View.extend({
    
    className: 'modal fade',
    template: _.template(ModalHtml),

    events: {
      'click .close': function(event) {
        event.preventDefault();
        this.trigger('close');
      },
      'click .cancel': function(event) {
        event.preventDefault();
        this.trigger('close');
      },
      'keypress': function(event) {
        if(event.which == 13) {
          event.preventDefault();
          this.trigger('close');
        } 
      }        
    },

    initialize: function() {
      this.options = {
        title: 'Dialog',
        content: '',
        cancelText: 'Close'            
      };
    },

    render: function() {
      var $el = this.$el;
      var options = this.options;
      var content = options.content;

      $el.html(this.template(options));

      this.isRendered = true;
    },

    isShown: function() {
      return $('.modal').data('bs.modal').isShown;
    },

    setTitle: function(title) {
      this.options.title = title;

      if( this.isRendered ) {
        throw 'modal has already been rendered';
      }

      return this;

    }, 

    setContent: function(content) {
      this.options.content = content;

      if( this.isRendered ) {
        throw 'modal has already been rendered';
      }      

      return this;
    },

    open: function() {
      if(!this.isRendered) this.render();

      var self = this;
      var $el = this.$el;

      $el.modal();

      self.on('close', function() {
        self.close();
      });

      self.trigger('shown');

    },

    close: function() {
      var self = this;
      var $el = this.$el;

      $el.one('hidden.bs.modal', function onHidden(event) {
        self.remove();
      });

      $el.modal('hide');

      self.trigger('hidden');
    }
  });
  return BaseModalView;

});
