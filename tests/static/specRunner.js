require.config({
  baseUrl: '../../app/static',
  paths: {
    'jquery': 'public/jquery/dist/jquery',
    'underscore': 'public/underscore/underscore',
    'backbone': 'public/backbone/backbone',
    'text': 'public/requirejs-text/text',
    'bootstrap': 'public/bootstrap/dist/js/bootstrap.min',

    'mocha': '../../node_modules/mocha/mocha',
    'chai': '../../node_modules/chai/chai',
    'chaiJquery': '../../node_modules/chai-jquery/chai-jquery',
    'sinon': '../../node_modules/sinon/lib/sinon',
    'sinonChai': '../../node_modules/sinon-chai/lib/sinon-chai',
    'squire': '../../node_modules/squirejs/src/squire'
  },
  shim: {
    mocha: {
      exports: 'mocha'   
    },
    chaiJquery: {
      deps: ['jquery', 'chai']
    },
    sinonChai: {
      deps: ['chai', 'sinon']
    }
  }
});

require([
  'jquery',
  'mocha',
  'chai',
  'chaiJquery',
  'sinon',
  'sinonChai',
  'squire'
], function($, mocha, Chai, ChaiJquery, Sinon, SinonChai, Squire) {
  // Backbone.history.start();
  Chai.config.includeStack = true;
  var should = Chai.should();
  Chai.use(SinonChai);
  Chai.use(ChaiJquery);

  mocha.setup('bdd');

  /*
  require(['../../tests/static/views/app-tests'], function() {
    mocha.run();
  });
  require(['../../tests/static/views/inputArea-tests'], function() {
    mocha.run();
  });
  require(['../../tests/static/views/resultArea-tests'], function() {
    mocha.run();
  });  
*/

  require(['../../tests/static/models/document-tests'], function() {
    mocha.run();
  });

});
