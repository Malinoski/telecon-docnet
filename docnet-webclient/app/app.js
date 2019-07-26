'use strict';

// Declare app level module which depends on views, and core components
angular.module('myApp', [
  'ngRoute',
  'myApp.view1',
  'myApp.view2',
  'myApp.login',
  'myApp.version'
])
.controller('MainCtrl', [ '$rootScope', function($rootScope) {	
	$rootScope.token = null;	
}])
.config(['$locationProvider', '$routeProvider', '$httpProvider', function($locationProvider, $routeProvider, $httpProvider) {
	
	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	$locationProvider.hashPrefix('!');
	$routeProvider.otherwise({redirectTo: '/view1'});
	

	
}]);
