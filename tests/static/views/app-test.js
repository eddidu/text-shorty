define([
  'jquery', 'backbone',
  'js/views/app'
], function($, Backbone, AppView) {
  
  describe('appView views', function() {

    // setup
  	beforeEach(function() {

  		this.view = new AppView();

  	});

  	afterEach(function() {

      this.view.remove();

  	});

  	//tests
  	describe('when initialized', function() {

  	  it('should show app title', function() {  

  	  	var $el = this.view.$el;

  	  	$el.find('.app-title').text().trim().length.should.be.above(0);  	  	  	  	

  	  });

  	  it('should show app description', function() {

  	  	var $el = this.view.$el;

  	  	$el.find('.app-description').text().trim().length.should.be.above(0);

  	  });

  	  it('should be able to take subviews and render them', function() {

  	  	var $el = this.view.$el;

  	  	// sample subviews
  	  	var view1 = Backbone.View.extend({
  	  	  className: 'view1',
  	  	  render: function() {
  	  	  	this.$el.html('this is view1');
  	  	  }
  	  	});
  	  	var view2 = Backbone.View.extend({
  	  	  className: 'view2',
  	  	  render: function() {
  	  	  	this.$el.html('this is view2');
  	  	  }
  	  	});

  	  	this.view.addSubviews([new view1, new view2]);

  	  	$el.find('.view1').should.have.text('this is view1');
  	  	$el.find('.view2').should.have.text('this is view2');

  	  });

  	});

  });

});
