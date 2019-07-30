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
    	    		$rootScope.tokenHeaderConfig
    	    ).then(function successCallback(response) {
    			
    			console.log("NetworksCtrl createNetwork success!");
    			console.log(response);
    			$scope.getNetworks();
    			bootbox.alert("Network created!");		
    			
    		}, function errorCallback(response) {
    			
    			console.log("NetworksCtrl createNetwork failed!");
    			console.log(response);
    			
    			var responseMessage = "";    			
    			if(response.status==401){
    				responseMessage = "Unauthorized!"
    			}else{
    				responseMessage = "Failed to create the network!" 
    			}
    			bootbox.alert(responseMessage);
    			
    		}).finally(function() {
    			$('#createNetworkModal').modal('hide');
    		});	
    		
    }
    
    $scope.deleteNetwork = function($networkId){
    		console.log("NetworksCtrl deleteNetwork("+$networkId+") ...");
    		
    		bootbox.confirm("Are you sure to delete the network?", function(result){
    			if(result){
    				
    				$http.delete(
    		    			$rootScope.webServerBaseUrl+'/networks/'+$networkId+'/',
    		    	    		$rootScope.tokenHeaderConfig
    		    	    ).then(function successCallback(response) {
    		    			
    		    			console.log("NetworksCtrl deleteNetwork success!");
    		    			console.log(response);
    		    			$scope.getNetworks();
    		    			bootbox.alert("Network removed!");		
    		    			
    		    		}, function errorCallback(response) {
    		    			
    		    			console.log("NetworksCtrl deleteNetwork failed!");
    		    			console.log(response);
    		    			
    		    			var responseMessage = "";    			
    		    			if(response.status==401){
    		    				responseMessage = "Unauthorized!"
    		    			}else{
    		    				responseMessage = "Failed to remove the network!" 
    		    			}
    		    			bootbox.alert(responseMessage);
    		    			
    		    		}).finally(function() {
    		    			// If needed
    		    		});	
    			}
    		});	
    		
    		
    }
}]);