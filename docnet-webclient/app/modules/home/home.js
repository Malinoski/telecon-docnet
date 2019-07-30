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
	
	$scope.networks = null;
	
	$scope.init = function(){
		$scope.getNetworksToken();
	}
    
	$scope.logout = function(){
		AuthenticationService.ClearCredentials();
    }
    
    console.log($rootScope);
    
    /* Example using username and pass
    $scope.getNetworks = function(){
    		$http({
			method: 'GET', 
			url: $rootScope.webServerBaseUrl+'/networks/',
			data:{
				username: $rootScope.globals.username,
				password: $rootScope.globals.password
			}						
		}).then(function successCallback(response) {
			
			console.log(response);
			$scope.networks = response.data.results;
			
		}, function errorCallback(response) {
			
			console.log(response);			
			
		}).finally(function() {
			// If needed
		});		
    }
    */
    
    $scope.getNetworks = function(){
		$http({
		method: 'GET', 
		url: $rootScope.webServerBaseUrl+'/networks/',
		data:{
			token: $rootScope.globals.currentUser
		}						
	}).then(function successCallback(response) {
		
		console.log(response);
		$scope.networks = response.data.results		
		
	}, function errorCallback(response) {
		
		console.log(response);			
		
	}).finally(function() {
		// If needed
	});		
}
    
}]);