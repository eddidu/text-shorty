define([
  'jquery', 'backbone',
  'js/models/document'
], function($, Backbone, Document) {

  describe('document models', function () {

  	beforeEach(function() {
  	  this.model = new Document();
  	});

  	afterEach(function() {

  	});

  	describe('when synced', function() {

  	  it('should set the request url depending on the option value', function () {

  	    var stub = new sinon.stub($, 'ajax');
            this.model.save({option: 'suburl'});
        
            stub.should.have.been.calledOnce;
            stub.getCall(0).args[0].url.should.contain('suburl');

	  });

  	});

    describe('when validate', function() {

      describe('when option is set to "summary"', function() {

        it('should throw an error when text.length < 500', function() {
          var error = this.model.validate({text: 'some texts with length less than 500', option: 'summary'});
          
          error.should.contain('500');
        });

      });

      describe('when option is set to "keywords"', function() {

        it('should throw an error when text.length < 40', function() {
          var error = this.model.validate({text: 'some texts with length less than 40', option: 'keywords'});
          
          error.should.contain('40');
        });

      });

    });

  });

});
