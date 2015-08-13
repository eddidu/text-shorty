define([
  'jquery', 'bootstrap', 'backbone',
  'js/views/modal'
], function($, Bootstrap, Backbone, ModalView) {

  describe('modal views', function() {

  	beforeEach(function() {
  	  this.view = new ModalView();
  	});

  	afterEach(function() {
  	  var view = this.view;
  	  view.$el.modal('hide');
  	  this.view.$el.one('hidden.bs.modal', function onHidden(event) {
        view.remove();
      });
  	});
  
    describe('when initialized', function() {
      
      it('should take "title" string as an input and show it when rendered', function() {
      	var view = this.view;

		view.setTitle('What up yo').render();

		view.$el.find('.modal-title').should.have.text('What up yo');
      });

      it('should take "content" html as an input and show it when rendered', function() {
      	var view = this.view;

      	view.setContent('some <b>contents</b> to be shown').render();

      	view.$el.find('.modal-body').should.have.html('some <b>contents</b> to be shown');
      });

    });

    describe('when rendered', function() {

      it('should be visible when opened', function(done) {
      	var view = this.view;
      	
      	view.open();
      	setTimeout(function() {
          view.$el.should.be.visible;
          done();
      	}, 300);
      });

      it('should be hidden when closed', function(done) {
      	var view = this.view;
      	
      	view.open();
      	view.close();
      	setTimeout(function() {
          view.$el.should.be.hidden;
          done();
      	}, 300);
      });

    });

  });

});
