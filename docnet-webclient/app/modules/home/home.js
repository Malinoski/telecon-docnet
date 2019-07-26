'use strict';

angular.module('myApp.home', ['ngRoute'])
.config(['$routeProvider', function($routeProvider) {
	
	$routeProvider
	.when('/home', {
		templateUrl: 'modules/home/home.html',
		controller: 'HomeCtrl'
	});
	
}])
.controller('HomeCtrl', ['$rootScope', '$scope', 'AuthenticationService', function($rootScope, $scope, AuthenticationService) {
	
    $scope.logout = function(){
		AuthenticationService.ClearCredentials();
    }
    
}]);