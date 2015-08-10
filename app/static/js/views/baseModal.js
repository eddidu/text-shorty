define([
    'jquery',
    'underscore',
    'backbone',
    'text!templates/baseModal.html'
], function($, _, Backbone, baseModalHtml) {  
    
'use strict';

var BaseModalView = Backbone.View.extend({

    className: 'modal fade',
    template: _.template(baseModalHtml),

    events: {
        'click .close': function(event) {
            event.preventDefault();
            this.trigger('cancel');
        },
        'click .cancel': function(event) {
            event.preventDefault();
            this.trigger('cancel');
        },
        'click .ok': function(event) {
            event.preventDefault();
            this.trigger('ok');
        },
        'keypress': function(event) {
           if(event.which == 13) {
            event.preventDefault();
            this.trigger('ok');
           } 
        }        
    },

    initialize: function(options) {
        var defaults = {
            title: 'Dialog',
            content: '',
            okText: 'Okay',
            cancelText: 'Close'            
        };

        this.options = _.extend(defaults, options);
    },

    render: function() {
        var $el = this.$el;
        var options = this.options;
        var content = options.content;

        $el.html(this.template(options));

        var $content = this.$content = $el.find('.modal-body')

        // insert body content if it's a view
        if(content && content.$el) {
            content.render();
            $el.find('.modal-body').html(content.$el);
        }

        this.isRendered = true;

        return this;
    },    

    open: function() {
        if(!this.isRendered) this.render();

        var self = this;
        var $el = this.$el;

        $el.modal();

        /*
        $el.one('shown.bs.modal', function() {
            self.trigger('shown');
        });
        */

        self.on('ok', function() {
            self.close();
        });

        self.on('cancel', function() {
            self.close();
        });
    },

    close: function() {

        var self = this;
        var $el = this.$el;

        $el.one('hidden.bs.modal', function onHidden(event) {
            self.remove();
            /*
            self.trigger('hidden');
            */
        });

        $el.modal('hide');
    }
});

    return BaseModalView;

});
