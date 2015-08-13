define([
  'jquery', 'backbone',
  'js/views/resultArea'
], function($, Backbone, ResultAreaView) {

	describe('resultArea views', function() {

	  // setup
	  beforeEach(function() {

	  	var Model = Backbone.Model.extend({
	  	  defaults: {
	  	  	text: '',
	  	  	option: '',
	  	  	result: ''
	  	  }
	  	});
	  	this.model = new Model();
	  	this.view = new ResultAreaView({model: this.model});

      });

      afterEach(function() {

      	this.view.remove();

      });

	  describe('when initialized', function() {

	  	it('should update the view when the model has changed', function () {

	  	  this.model.set({text: 'some texts', result: ['yo1', 'yo2'], option: 'an option'});

	  	  var $el = this.view.$el;

                  //TODO: chai-jquery contains not working properly...causing obj.indexOf not a function error
                  $el.is(':contains("yo1")').should.be.true;
                  $el.is(':contains("yo2")').should.be.true;
                  $el.is(':contains("some texts")').should.be.false;

	  	});

	  });

	});

});
