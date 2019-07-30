'use strict';

angular.module('myApp.home', ['ngRoute'])
.config(['$routeProvider', function($routeProvider) {
	
	$routeProvider
	.when('/home', {
		templateUrl: 'modules/home/home.html',
		controller: 'HomeCtrl'
	});
	
}])
.controller('HomeCtrl', ['$rootScope', '$scope', '$http', 'AuthenticationService', function($rootScope, $scope, $http, AuthenticationService) {
	
	console.log("Start HomeCtrl ...");
	
	$scope.logout = function(){
		AuthenticationService.ClearCredentials();
	}
	
}]);