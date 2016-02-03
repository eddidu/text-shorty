// Karma configuration
// Generated on Wed Aug 12 2015 22:39:53 GMT+0900 (KST)

module.exports = function(config) {
  config.set({

    basePath: '../..',

    frameworks: ['mocha', 'requirejs', 'chai-jquery', 'jquery-2.1.0', 'chai-sinon'],

    files: [
      'tests/static/test-main.js',
      {pattern: 'node_modules/squirejs/**/*.js', included: false},
      {pattern: 'tests/static/**/*.js', included: false},
      {pattern: 'app/static/js/**/*.js', included: false},
      {pattern: 'app/static/templates/*.html', included: false},
      {pattern: 'app/static/public/**/*.*', included: false}
    ],

    exclude: [
      'app/static/js/main.js',
      'app/static/js/config.js'
    ],

    reporters: ['mocha'],

    client: {
      mocha: {
        reporter: 'html', // change Karma's debug.html to the mocha web reporter
        ui: 'bdd'
      }
    },

    // possible values: config.LOG_DISABLE || config.LOG_ERROR || config.LOG_WARN || config.LOG_INFO || config.LOG_DEBUG
    //logLevel: config.LOG_INFO,

    browsers: ['Chrome'],
 
    singleRun: true
  })
}
