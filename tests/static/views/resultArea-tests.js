define([
  'squire', 'sinon', 
  'underscore', 'jquery', 'backbone',
  'js/views/resultArea'
], function(Squire, Sinon, _, $, Backbone, ResultAreaView) {

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

	  	  $el.should.contain('an option');
	  	  $el.should.contain('yo1');
	  	  $el.should.contain('yo2');
	  	  $el.should.not.contain('some texts');

	  	});

	  });

	});

});