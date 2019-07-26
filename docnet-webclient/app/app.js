'use strict';

// Declare app level module which depends on views, and core components
angular.module('myApp', [
  'ngRoute',
  'myApp.view1',
  'myApp.view2',
  'myApp.login',
  'myApp.version'
])
.config(['$locationProvider', '$routeProvider', '$httpProvider', function($locationProvider, $routeProvider) {
	
	$locationProvider.hashPrefix('!');
	$routeProvider.otherwise({redirectTo: '/login'});
	
}])
.controller('MainCtrl', [ '$rootScope', function($rootScope) {	
	$rootScope.token = null;	
}])
