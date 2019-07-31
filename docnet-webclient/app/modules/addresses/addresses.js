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
	$scope.ipNote = "For example: if CIDR networks is 192.168.0.0/24, the values can be between 192.168.0.0 to 192.168.0.255";
	
	$scope.init = function(){
		$scope.getAddresses();
	}
    
	$scope.logout = function(){
		AuthenticationService.ClearCredentials();
	}
	
	/** REST request */
    $scope.getAddresses = function(){
    	
		console.log("AddressesCtrl getAddresses ...");
	
		$http.get(
			$rootScope.webServerBaseUrl+'/addresses/'										
		).then(function successCallback(response) {
			
			console.log("AddressesCtrl getAddresses success!");
			console.log(response);
			$scope.addresses = response.data.results		
			
		}, function errorCallback(response) {
			
			console.log("AddressesCtrl getAddresses failed!");
			console.log(response);			
			
		}).finally(function() {
			// If needed
		});		
	}
    
    $scope.createAddress = function($inputIp, $inputTitle, $inputDescription, $network){
    		console.log("AddressesCtrl createAddress ("+ $inputIp+", "+$inputTitle+", "+ $inputDescription+", "+ $network + ") ...");
    		console.log("TODO");
    }
    
}]);