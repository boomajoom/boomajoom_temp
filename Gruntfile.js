'use strict';

module.exports = function(grunt) {

    // configuration
  grunt.initConfig({

    jshint: {
      options: {
        jshintrc: '.jshintrc',
        ignores: ['static/components/**/*.js']
      },
      files: {
        src: ['client/**/*.js', 'static/js/*.js']
      },
      gruntfile: {
        src: 'Gruntfile.js'
      }
    },

    watch: {
      lint: {
        files: '<%= jshint.files.src %>',
        tasks: 'jshint'
      }
    }
  });


  // plugins
  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // tasks
  grunt.registerTask('default', ['watch']);

};