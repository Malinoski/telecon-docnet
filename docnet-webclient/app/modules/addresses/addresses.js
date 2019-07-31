'use strict';

angular.module('myApp.addresses', ['ngRoute'])
.config(['$routeProvider', function($routeProvider) {
	
	$routeProvider
	.when('/addresses', {
		templateUrl: 'modules/addresses/addresses.html',
		controller: 'AddressesCtrl'
	});
	
}])
.controller('AddressesCtrl', ['$rootScope', '$scope', '$http', '$location', '$cookieStore', 'AuthenticationService', function($rootScope, $scope, $http, $location, $cookieStore, AuthenticationService) {
	
	console.log("AddressesCtrl start ...");
	
	$scope.init = function(){
		
	}
    
	$scope.logout = function(){
		AuthenticationService.ClearCredentials();
	}
    
}]);