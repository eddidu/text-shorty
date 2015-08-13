define([
  'jquery', 'bootstrap', 'backbone',
  'js/views/inputArea'
], function($, Bootstrap, Backbone, InputAreaView) {
  
  describe('inputArea views', function() {

    // setup
    beforeEach(function() {

      this.model = new Backbone.Model();
      this.view = new InputAreaView({model: this.model});
      this.view.render();

    });

    afterEach(function() {

      // clear up
      $('.modal').modal('hide');
      $('.modal').remove();      

      this.view.remove();

    });

    //tests
    describe('when rendered', function() {

      it('should have text input area', function() {

        var $textarea = this.view.$el.find('textarea');

        $textarea.length.should.be.equal(1);

      });

      it('should have raido buttons to select the type of text reduction method', function() {

        var $radio = this.view.$el.find('input:radio');

        // radio options: summary, keywords
        $radio.length.should.be.equal(2);

      });

      it('should set "summary" as a default option', function() {

        var $option = this.view.$el.find('input[name="option"]');

        $option.should.have.value('summary')      

      });

      it('should have a submit button', function() {

        var $btn = this.view.$el.find('button:button');

        $btn.length.should.be.equal(1);

      });

    });

    describe('when submit button is clicked', function() {

      it('should save the data through model', function() {
        var $el = this.view.$el;

        $el.find('textarea').val('some texts');
        $el.find('input[name="option"]').val('keywords');

        var stub = new sinon.stub(this.model, 'save');

        $el.find('button:button').click();

        stub.should.have.been.calledOnce;
        stub.should.have.been.calledWith({text: 'some texts', option: 'keywords'});
      });

      it('should show error modal when validation fails', function(done) {
        var $el = this.view.$el;

        this.model.trigger('invalid', this.model, 'error msg');

        setTimeout(function() {
          $('.modal').should.be.visible;
          $('.modal-body').should.have.text('error msg');

          done();
        }, 300);

      });

    });

  });

});
