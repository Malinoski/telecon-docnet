'use strict';

// Declare app level module which depends on views, and core components
angular.module('myApp', [
  'ngRoute',
  'ngCookies',
  'myApp.login',
  'myApp.home',
  'myApp.networks',
  'myApp.addresses',
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
	.when('/networks', {
		controller : 'NetworksCtrl',
		templateUrl : 'modules/networks/networks.html'
	})
	.when('/addresses', {
		controller : 'AddressesCtrl',
		templateUrl : 'modules/addresses/addresses.html'
	})
	.otherwise({
		redirectTo : '/login'
	});	
	
}])
.run(function($rootScope) {
	 $rootScope.webServerBaseUrl = 'http://127.0.0.1:8001';	 
});
