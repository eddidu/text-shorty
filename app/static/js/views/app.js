define([
    'jquery',
  	'backbone',
    'models/document',
    'views/document',
    'views/baseModal'
], function($, Backbone, Document, DocumentView, BaseModalView) {  
    
    'use strict';

    var AppView = Backbone.View.extend({

        el: '.container',

      	events: {
      		  'click #btn-summerize': 'summarize',
            'click p.lead a': 'showDetail'
      	},      	

      	initialize: function() {
        		this.$input = this.$('#document');

            var documentView = new DocumentView({model: Document});
            documentView.render();

            return this;
      	},

      	summarize: function(event) {

            var attrs = {
                text: this.$input.val().trim()
            };

            Document.save(attrs);

            return this;
      	},

        showDetail: function(event) {

            var ModalContent = Backbone.View.extend({
                render: function() {
                    var content = [
                      'This summarization tool is based on the <a href=#>Lexrank</a> algorithm',
                      'which uses statistical aproach to pick sentences that best represent the given document.',
                      'This algorithm relies heavily on how the document is tokenized, to sentences and to words.',
                      'NLTK package is used for the tokenization, but still need sophiscated tokenization steps to improve accuracy.', 
                      '<br><br>For contribution, check the <a href=#>git repository</a>'                    
                    ].join(' ');
                    this.$el.html(content);
                }
            });

            var detailModal = new BaseModalView({
                title: 'About Text Shorty',
                content: new ModalContent()
            });
            detailModal.open();
        }
    });

    return AppView;
});
