define([
  'squire', 'sinon', 
  'underscore', 'jquery', 'backbone',
  'js/models/document'
], function(Squire, Sinon, _, $, Backbone, Document) {

  describe('document models', function () {

  	beforeEach(function() {

  	  this.model = new Document();

  	});

  	afterEach(function() {

  	});

  	describe('when synced', function() {

  	  it('should set the request url depending on the option value', function () {

  	  	var stub = Sinon.stub($, 'ajax');

	    this.model.save({option: 'suburl'});

	    stub.should.have.been.calledOnce;
	    stub.getCall(0).args[0].url.should.contain('suburl');

	  });

  	});

  });

});