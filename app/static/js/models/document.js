define([
    'jquery', 
    'backbone'
], function($, Backbone) {

    var Document = Backbone.Model.extend({

        initialize: function() {

        },

        url: function() {
            return '/text-shorty/api/summarizer';
        },        

        defaults: {
            text: '',
            summary: []
        },

        validate: function(attrs) {
            if(attrs.text.length < 500) {
                return ['The document you requested to summerize is either too short or contains no texts.',
                'Be sure to provide a document with <b>more than 500</b> characters.'
                ].join(' ');
            }
        },

        parse : function(resp, xhr) {
            return {
                summary: resp['summary']
            };
        }        

        /*
        // Gets called automatically by Backbone when the set and/or save methods are called (Add your own logic)
        validate: function(attrs) {

        }
        */

    });

    return new Document();

}

);