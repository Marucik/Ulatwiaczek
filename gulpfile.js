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
    .pipe(gulp.dest('ulatwiaczek/static/css'))
    .pipe(cssmin())
    .pipe(rename({suffix: '.min'}))
    .pipe(gulp.dest('ulatwiaczek/static/css'));
});
gulp.task('bootstrap-v4-dev', function () {
  return gulp.src('./sources/style/bootstrap-v4-dev/scss/bootstrap.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(postcss([ autoprefixer() ]))
    .pipe(cssbeautify({
      indent: '  ',
      openbrace: 'end-of-line',
      autosemicolon: true
    }))
    .pipe(gulp.dest('ulatwiaczek/static/css'))
    .pipe(cssmin())
    .pipe(rename({suffix: '.min'}))
    .pipe(gulp.dest('ulatwiaczek/static/css'));
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
    .pipe(gulp.dest('ulatwiaczek/static/css'))
    .pipe(cssmin())
    .pipe(rename({suffix: '.min'}))
    .pipe(gulp.dest('ulatwiaczek/static/css'));
});
gulp.task('sass:user', function () {
  return gulp.src('sources/style/user.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(postcss([ autoprefixer() ]))
    .pipe(cssbeautify({
      indent: '  ',
      openbrace: 'end-of-line',
      autosemicolon: true
    }))
    .pipe(gulp.dest('ulatwiaczek/static/css'))
    .pipe(cssmin())
    .pipe(rename({suffix: '.min'}))
    .pipe(gulp.dest('ulatwiaczek/static/css'));
});
gulp.task('sass:watch', function () {
  gulp.watch('sources/style/*.scss',['sass', 'sass:user']);
  gulp.watch('./node_modules/bootstrap-v4-dev/scss/**/*',['bootstrap-v4-dev']);
});

gulp.task('fonts', function() {
  return gulp.src('node_modules/font-awesome/fonts/*')
  .pipe(gulp.dest('main/static/fonts'))
});

gulp.task('css:compile', ['sass', 'sass:user', 'font-awesome', 'bootstrap-v4-dev'], function () {
  console.log("Kompiluje pliki scss.");
});
