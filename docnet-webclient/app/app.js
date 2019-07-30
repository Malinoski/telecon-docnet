'use strict';

// Declare app level module which depends on views, and core components
angular.module('myApp', [
  'ngRoute',
  'ngCookies',
  'myApp.view1',
  'myApp.view2',
  'myApp.login',
  'myApp.home',
  'myApp.version'
])
.config(['$locationProvider', '$routeProvider', '$httpProvider', function($locationProvider, $routeProvider, $httpProvider) {
	
	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	
	
	
	$routeProvider
	.when('/login', {
		controller : 'LoginController',
		templateUrl : 'modules/login/login.html',
		hideMenus : true,
		controller: 'LoginCtrl'
	})
	.when('/', {
		controller : 'HomeCtrl',
		templateUrl : 'modules/home/home.html'
	})
	.otherwise({
		redirectTo : '/login'
	});	
	
}])
.run(function($rootScope) {
	$rootScope.webServerBaseUrl = 'http://127.0.0.1:8001/';
});
