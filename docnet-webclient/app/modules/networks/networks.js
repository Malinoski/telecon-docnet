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
	
	console.log("NetworksCtrl start ...");
	
	$http.defaults.headers.common.Authorization = 'Authorization: Token ' + $rootScope.globals.currentUser.token;
	$scope.networks = null;

	$scope.init = function(){
		$scope.getNetworks();
	}
    
	$scope.logout = function(){
		AuthenticationService.ClearCredentials();
	}
	
    $scope.getNetworks = function(){
    	
		console.log("NetworksCtrl createNetwork ...");
	
		$http.get(
			$rootScope.webServerBaseUrl+'/networks/'										
		).then(function successCallback(response) {
			
			console.log("NetworksCtrl getNetworks success!");
			console.log(response);
			$scope.networks = response.data.results		
			
		}, function errorCallback(response) {
			
			console.log("NetworksCtrl getNetworks failed!");
			console.log(response);			
			
		}).finally(function() {
			// If needed
		});		
	}
    
    $scope.createNetwork = function($cidr, $title, $description, $enabled){
    	
    		console.log("NetworksCtrl createNetwork ...");
    		console.log($http.defaults.headers.common.Authorization);
    		
    		$http.post(
    			$rootScope.webServerBaseUrl+'/networks/', 
    	    		{
    				cidr: $cidr,
    				title: $title,
    				description: $description,
    				enabled: $enabled
    	    		},
    	    		$rootScope.postConfig
    	    ).then(function successCallback(response) {
    			
    			console.log("NetworksCtrl createNetwork success!");
    			console.log(response);
    			$scope.getNetworks();
    			bootbox.alert("Network created!");		
    			
    		}, function errorCallback(response) {
    			
    			console.log("NetworksCtrl createNetwork failed!");
    			console.log(response);
    			
    			var createNetworkResponseMessage = "";    			
    			if(response.status==401){
    				createNetworkResponseMessage = "Unauthorized!"
    			}else{
    				createNetworkResponseMessage = "Failed to create the network!" 
    			}
    			bootbox.alert(createNetworkResponseMessage);
    			
    		}).finally(function() {
    			$('#createNetworkModal').modal('hide');
    		});	
    		
    }
    
}]);