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
	
	$scope.addresses = null;
	$scope.networks = null;
	$scope.ipNote = "For example: if CIDR networks is 192.168.0.0/24, the values can be between 192.168.0.0 to 192.168.0.255";
	
	$scope.init = function(){
		$scope.getAddresses();
	}
    
	$scope.logout = function(){
		AuthenticationService.ClearCredentials();
	}
	
	/** REST request */
    $scope.getAddresses = function(){
    		
    		console.log("AddressesCtrl getAddresses () ...");
    	
    		console.log("AddressesCtrl getAddresses - get networks ...");
    		/* Get networks - this will be used to create an adress (to make a relationship)*/
    		$http.get(
    			$rootScope.webServerBaseUrl+'/networks/'										
    		).then(function successCallback(response) {
    			
    			console.log("AddressesCtrl getAddresses - get networks success!");
    			console.log(response);
    			$scope.networks = response.data.results		
    			
    		}, function errorCallback(response) {
    			
    			console.log("AddressesCtrl getAddresses - get networks failed!");
    			console.log(response);			
    			
    		}).finally(function() {
    			// If needed
    		});		
    	
    		console.log("AddressesCtrl getAddresses - get addresses ...");	
		$http.get(
			$rootScope.webServerBaseUrl+'/addresses/'										
		).then(function successCallback(response) {
			
			console.log("AddressesCtrl getAddresses - get addresses success!");
			console.log(response);
			$scope.addresses = response.data.results		
			
		}, function errorCallback(response) {
			
			console.log("AddressesCtrl getAddresses - get addresses failed!");
			console.log(response);			
			
		}).finally(function() {
			// If needed
		});		
	}
    
    $scope.createAddress = function($ip, $title, $description, $networkId){
    		console.log("AddressesCtrl createAddress ("+ $ip+", "+$title+", "+ $description+", "+ $networkId + ") ...");
    		
    		$http.post(
    			$rootScope.webServerBaseUrl+'/addresses/', 
    	    		{
    				ip: $ip,
    				title: $title,
    				description: $description,
    				network: $networkId
    	    		},
    	    		$rootScope.globals.tokenHeaderConfig
    	    ).then(function successCallback(response) {
    			
    			console.log("AddressesCtrl createAddress success!");
    			console.log(response);
    			$scope.getAddresses();
    			bootbox.alert("Address created!");    			
    			
    		}, function errorCallback(response) {
    			
    			console.log("AddressesCtrl createAddress failed!");
    			console.log(response);
    			
    			if(response.status==401){ // Unauthorized, but why?
    				bootbox.alert("Unauthorized!");
    			}else{
    				bootbox.alert("Failed to create the address!" );    				
    			}
    			
    		}).finally(function() {
    			$('#createAddressModal').modal('hide');    			
    		});	
    }
    
    $scope.loadUpdateAddressModal = function ($address){
    		console.log("AddressesCtrl loadUpdateAddressModal ...");
    }
    
    $scope.deleteAddress = function ($address){
    		console.log("AddressesCtrl deleteAddress ...");
    		
    		bootbox.confirm("Are you sure to delete?", function(result){
    			if(result){
    				
    				$http.delete(
    					$address.url,
    		    			$rootScope.globals.tokenHeaderConfig
    		    	    ).then(function successCallback(response) {
    		    			
    		    			console.log("AddressesCtrl deleteAddress success!");
    		    			console.log(response);
    		    			$scope.getAddresses();
    		    			bootbox.alert("Address removed!");		
    		    			
    		    		}, function errorCallback(response) {
    		    			
    		    			console.log("AddressesCtrl deleteAddress failed!");
    		    			console.log(response);
    		    			
    		    			if(response.status==401){
    		    				bootbox.alert("Unauthorized!");    		    				
    		    			}else{
    		    				bootbox.alert("Failed to remove the address!");
    		    			}    		    			
    		    			
    		    		}).finally(function() {
    		    			// If need to
    		    		});	
    			}
    		});    		
    		
    }
    
}]);