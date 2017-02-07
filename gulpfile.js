'use strict';
var gulp = require('gulp'),
   sass = require('gulp-sass'),
   rename = require('gulp-rename'),
   cssbeautify = require('gulp-cssbeautify'),
   cssmin = require('gulp-cssmin'),
   postcss = require('gulp-postcss'),
   autoprefixer = require('autoprefixer');
   
gulp.task('sass', function () {
   return gulp.src('sources/style/*.scss')
         .pipe(sass().on('error', sass.logError))
         .pipe(postcss([ autoprefixer() ]))
		   .pipe(cssbeautify({
            indent: '  ',
            openbrace: 'end-of-line',
            autosemicolon: true
          }))
         .pipe(gulp.dest('main/static/css'))
         .pipe(cssmin())
         .pipe(rename({suffix: '.min'}))
         .pipe(gulp.dest('main/static/css'));
});
gulp.task('bootstrap-sass', function () {
   return gulp.src('node_modules/bootstrap-sass/assets/stylesheets/**/*.scss')
         .pipe(sass().on('error', sass.logError))
         .pipe(postcss([ autoprefixer() ]))
         .pipe(cssbeautify({
            indent: '  ',
            openbrace: 'end-of-line',
            autosemicolon: true
          }))
         .pipe(gulp.dest('main/static/css'))
         .pipe(cssmin())
         .pipe(rename({suffix: '.min'}))
         .pipe(gulp.dest('main/static/css'));
});


gulp.task('sass:watch', function () {
   gulp.watch('sources/style/*.scss',['sass']);
   gulp.watch('node_modules/bootstrap-sass/assets/stylesheets/**/*.scss',['bootstrap-sass']);
});