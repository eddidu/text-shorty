define([
    'underscore',
    'backbone',
    'models/document',
    'text!../../templates/document.html',
    'views/baseModal'        
], function(_, Backbone, Document, documentHtml, BaseModalView) {  
    
'use strict';

var DocumentView = Backbone.View.extend({

    el: '#summary',
    template: _.template(documentHtml),

    initialize: function() {
        this.listenTo(this.model, 'change', this.render);
        this.listenTo(this.model, 'invalid', function(model, error) {

            var ModalContent = Backbone.View.extend({
                render: function() {
                    this.$el.html(error);
                }
            });

            var warningModal = new BaseModalView({
                title: 'Warning',
                content: new ModalContent()
            });
            warningModal.open(); 

        });
    },

    render: function() {

        var doc = this.model.toJSON();
        this.$el.html(this.template(doc));

        return this;
    }

});

    return DocumentView;

});
