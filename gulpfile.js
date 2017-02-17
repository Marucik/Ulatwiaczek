'use strict';
var gulp = require('gulp'),
   sass = require('gulp-sass'),
   rename = require('gulp-rename'),
   cssbeautify = require('gulp-cssbeautify'),
   cssmin = require('gulp-cssmin'),
   postcss = require('gulp-postcss'),
   autoprefixer = require('autoprefixer');

gulp.task('sass', function () {
   return gulp.src('sources/style/main.scss')
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
gulp.task('font-awesome', function () {
   return gulp.src('sources/style/font-awesome.scss')
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
gulp.task('sass:login', function () {
   return gulp.src('sources/style/login.scss')
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
   gulp.watch('sources/style/*.scss',['sass', 'sass:login']);
   gulp.watch('node_modules/bootstrap-sass/assets/stylesheets/**/*.scss',['bootstrap-sass']);
});

gulp.task('fonts', function() {
    return gulp.src('node_modules/font-awesome/fonts/*')
    .pipe(gulp.dest('main/static/fonts'))
});

gulp.task('compile_css', ['sass', 'sass:login', 'font-awesome'], function () {
    console.log("Kompiluje pliki scss.");
});
