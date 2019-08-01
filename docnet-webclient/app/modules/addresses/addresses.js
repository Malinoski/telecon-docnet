'use strict';

angular.module('myApp.addresses', ['ngRoute'])
.config(['$routeProvider', function($routeProvider) {
	
	$routeProvider
	.when('/addresses/:networkId', {
		templateUrl: 'modules/addresses/addresses.html',
		controller: 'AddressesCtrl'
	});
	
}])
.controller('AddressesCtrl', ['$rootScope', '$scope', '$http', '$location', '$cookieStore', 'AuthenticationService', '$routeParams', function($rootScope, $scope, $http, $location, $cookieStore, AuthenticationService, $routeParams) {
	
	console.log("AddressesCtrl start (Route params: "+$routeParams.networkId+ ")...");	
	
	$scope.addresses = null;
	$scope.networks = null;
	$scope.network = null;
	$scope.networkId = $routeParams.networkId;
	$scope.ipNote = "For example: if CIDR networks is 192.168.0.0/24, the values can be between 192.168.0.0 to 192.168.0.255";
	
	$scope.init = function(){
		console.log("AddressesCtrl init ...");
		$scope.getAddressesFromNetwork();	
		$scope.getNetworkDetails();
	}
    
	$scope.logout = function(){
		AuthenticationService.ClearCredentials();
	}
	
	/** REST request */
    $scope.getNetworkDetails = function(){
    		
    		console.log("AddressesCtrl getAddressNetwork ...");
    	
    		$http.get(
			$rootScope.webServerBaseUrl+'/networks/' + $scope.networkId + '/'	,
			$rootScope.globals.tokenHeaderConfig
		).then(function successCallback(response) {
			
			console.log("AddressesCtrl getAddressNetwork success!");
			console.log(response);
			$scope.network = response.data		
			
		}, function errorCallback(response) {
			
			console.log("AddressesCtrl getAddressNetwork failed!");
			console.log(response);			
			
		}).finally(function() {
			// If needed
		});		
	}
	
	
	/** REST request */
    $scope.getAddressesFromNetwork = function(){
    		
    		console.log("AddressesCtrl getAddressesFromNetwork (networkId="+$scope.networkId+")...");
    	
    		/** Get addresses */
    		$http.get(
			$rootScope.webServerBaseUrl+'/addresses/?networkId=' + $scope.networkId,
			$rootScope.globals.tokenHeaderConfig
		).then(function successCallback(response) {
			
			console.log("AddressesCtrl getAddressesFromNetwork success!");
			console.log(response);
			$scope.addresses = response.data.results		
			
		}, function errorCallback(response) {
			
			console.log("AddressesCtrl getAddressesFromNetwork failed!");
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
    			$scope.getAddressesFromNetwork();
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
    		$scope.createAddressForm.$setPristine();
    		
    		/**
    		The code below CANT be used, because it will create a reference, not a copy. If the user alter the fields (input), it will update the principal object.
    		$scope.addressToUpdate = $address;    			
    		The proper way is to make a copy:
    		$scope.addressToUpdate = angular.copy($address);
    		*/ 
    		$scope.addressToUpdate = angular.copy($address);
    }
    
    /** REST request */
    $scope.updateAddress = function($addressToUpdate){
    	
    		console.log("AddressesCtrl updateAddress ...");
    		
		$http.put(
			$addressToUpdate.url,
	    		{
				ip: $addressToUpdate.ip,
				title: $addressToUpdate.title,
				description: $addressToUpdate.description,
				network: $addressToUpdate.network				
	    		},
	    		$rootScope.globals.tokenHeaderConfig
	    ).then(function successCallback(response) {
			
			console.log("AddressesCtrl updateAddress success!");
			console.log(response);
			$scope.getAddressesFromNetwork();
			bootbox.alert("Address updated!");		
			
		}, function errorCallback(response) {
			
			console.log("AddressesCtrl updateAddress failed!");
			console.log(response);
			
			if(response.status==401){ // Unauthorized, but why?
				bootbox.alert("Unauthorized!");
			}else{
				bootbox.alert("Failed to update the address!" );    				
			}
			
		}).finally(function() {
			$('#updateAddressModal').modal('hide');
		});	
		
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
    		    			$scope.getAddressesFromNetwork();
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