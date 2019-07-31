'use strict';

angular.module('myApp.networks', ['ngRoute'])
.config(['$routeProvider', function($routeProvider) {
	
	$routeProvider
	.when('/networks', {
		templateUrl: 'modules/networks/networks.html',
		controller: 'NetworksCtrl'
	});
	
}])
.controller('NetworksCtrl', ['$rootScope', '$scope', '$http', '$location', '$cookieStore', 'AuthenticationService', function($rootScope, $scope, $http, $location, $cookieStore, AuthenticationService) {
	
	console.log("NetworksCtrl start ...");
	
	$http.defaults.headers.common.Authorization = 'Authorization: Token ' + $rootScope.globals.currentUser.token;
	$scope.networks = null;
	$scope.networkToUpdate = null;
	$scope.disableSendUpdateNetworkForm = true;
	$scope.cidrNote = "Classless Inter-Domain Routing (i.e.: 192.168.0.0/24, 192.168.0.0/22, 2002:C0A8::/48, etc.)";
	
	$scope.init = function(){
		$scope.getNetworks();
	}
    
	$scope.logout = function(){
		AuthenticationService.ClearCredentials();
	}
	
	/** REST request */
    $scope.getNetworks = function(){
    	
		console.log("NetworksCtrl getNetworks ...");
	
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
    
    /** REST request */
    $scope.createNetwork = function($cidr, $title, $description, $enabled){
    	
    		console.log("NetworksCtrl createNetwork ("+$cidr+", "+$title+", "+$description+", "+$enabled+") ...");
    		
    		$http.post(
    			$rootScope.webServerBaseUrl+'/networks/', 
    	    		{
    				cidr: $cidr,
    				title: $title,
    				description: $description,
    				enabled: $enabled
    	    		},
    	    		$rootScope.globals.tokenHeaderConfig
    	    ).then(function successCallback(response) {
    			
    			console.log("NetworksCtrl createNetwork success!");
    			
    			console.log(response);
    			$scope.getNetworks();
    			bootbox.alert("Network created!");		
    			
    		}, function errorCallback(response) {
    			
    			console.log("NetworksCtrl createNetwork failed!");
    			console.log(response);
    			
    			if(response.status==401){ 
    				bootbox.alert("Unauthorized!");
    			}else{
    				bootbox.alert("Failed to create the network!" );    				
    			}
    			
    		}).finally(function() {
    			$('#createNetworkModal').modal('hide');
    		});	
    		
    }
    
    /** Used to fill the modal for update network */ 
    $scope.loadUpdateNetworkModal = function(network){
    		$scope.updateNetworkForm.$setPristine()
    		
    		/**
    		The code below CANT be used, because it will create a reference, not a copy. If the user alter the fields (imput), it will update the principal object.
    		$scope.networkToUpdate = network;
    			
    		The proper way is to make a copy:
    		$scope.networkToUpdate = angular.copy(network);
    		*/ 
    		$scope.networkToUpdate = angular.copy(network);
    }
    
    /** REST request */
    $scope.updateNetwork = function($networkToUpdate){
    		console.log("NetworksCtrl updateNetwork ... ");
    		console.log($networkToUpdate);
    		
		$http.put(
			// $rootScope.webServerBaseUrl+'/networks/'+$networkToUpdate.id+'/',
			$networkToUpdate.url,
	    		{
				cidr: $networkToUpdate.cidr,
				title: $networkToUpdate.title,
				description: $networkToUpdate.description,
				enabled: $networkToUpdate.enabled
	    		},
	    		$rootScope.globals.tokenHeaderConfig
	    ).then(function successCallback(response) {
			
			console.log("NetworksCtrl updateNetwork success!");
			console.log(response);
			$scope.getNetworks();
			bootbox.alert("Network updated!");		
			
		}, function errorCallback(response) {
			
			console.log("NetworksCtrl updateNetwork failed!");
			console.log(response);
			
			if(response.status==401){ // Unauthorized, but why?
				bootbox.alert("Unauthorized!");
			}else{
				bootbox.alert("Failed to update the network!" );    				
			}
			
		}).finally(function() {
			$('#updateNetworkModal').modal('hide');
		});	
		
    }
    
    /** REST request */
    $scope.deleteNetwork = function($network){
    		console.log("NetworksCtrl deleteNetwork("+$network.id+") ...");
    		
    		bootbox.confirm("Are you sure to delete?", function(result){
    			if(result){
    				
    				$http.delete(
    		    			// $rootScope.webServerBaseUrl+'/networks/'+$networkId+'/',
    					$network.url,
    		    			$rootScope.globals.tokenHeaderConfig
    		    	    ).then(function successCallback(response) {
    		    			
    		    			console.log("NetworksCtrl deleteNetwork success!");
    		    			console.log(response);
    		    			$scope.getNetworks();
    		    			bootbox.alert("Network removed!");		
    		    			
    		    		}, function errorCallback(response) {
    		    			
    		    			console.log("NetworksCtrl deleteNetwork failed!");
    		    			console.log(response);
    		    			
    		    			if(response.status==401){
    		    				bootbox.alert("Unauthorized!");
    		    				
    		    			}else{
    		    				bootbox.alert("Failed to remove the network!");
    		    			}    		    			
    		    			
    		    		}).finally(function() {
    		    			// If need to
    		    		});	
    			}
    		});    		
    }
    
    $scope.networkDetail = function($network){
    		console.log("NetworksCtrl networkDetail ... ");    		
    		$location.path('/addresses/'+$network.id);		
    }
    
}]);