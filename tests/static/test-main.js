var allTestFiles = [];
var TEST_REGEXP = /(-spec|-test)\.js$/i;

Object.keys(window.__karma__.files).forEach(function(file) {
  if (TEST_REGEXP.test(file)) {
    normalizedTestModule = file.replace(/^\/base\//, '../../').replace(/\.js$/, '');
    allTestFiles.push(normalizedTestModule);
  }
});

require.config({
  baseUrl: '/base/app/static',

  paths: {
    'jquery': 'public/jquery/dist/jquery',
    'underscore': 'public/underscore/underscore',
    'backbone': 'public/backbone/backbone',
    'text': 'public/requirejs-text/text',
    'bootstrap': 'public/bootstrap/dist/js/bootstrap.min',

    'squire': '../../node_modules/squirejs/src/squire'
  },

  shim: {
    underscore: {
      exports: '_'
    },
    backbone: {
      exports: 'Backbone',
      deps: ['jquery', 'underscore']
    },
    bootstrap: {
      deps: ['jquery']
    }
  },

  deps: allTestFiles,

  callback: window.__karma__.start
});
