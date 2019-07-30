'use strict';

angular.module('myApp.networks', ['ngRoute'])
.config(['$routeProvider', function($routeProvider) {
	
	$routeProvider
	.when('/networks', {
		templateUrl: 'modules/networks/networks.html',
		controller: 'NetworksCtrl'
	});
	
}])
.controller('NetworksCtrl', ['$rootScope', '$scope', '$http', 'AuthenticationService', function($rootScope, $scope, $http, AuthenticationService) {
	
	$scope.networks = null;

	$scope.init = function(){
		$scope.getNetworks();
	}
    
	$scope.logout = function(){
		AuthenticationService.ClearCredentials();
	}
	
    console.log("NetworksCtrl start ...");
    
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
    	
    		console.log("NetworksCtrl createNetwork ...");
    	
		$http({
			method: 'GET', 
			url: $rootScope.webServerBaseUrl+'/networks/',
			data:{
				token: $rootScope.globals.currentUser.token
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
    
    $scope.createNetwork = function(){
    		console.log("NetworksCtrl createNetwork ...");
    		$('#createNetworkModal').modal('hide');
    }
    
}]);