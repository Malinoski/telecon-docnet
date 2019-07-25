'use strict';

angular.module('myApp.login', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/login', {
    templateUrl: 'modules/login/login.html',
    controller: 'LoginCtrl'
  });
}])

.controller('LoginCtrl', [ '$scope', '$http', function($scope, $http) {
	
	$scope.username = null;
	$scope.password = null;
	
	$scope.login = function(){
		
		$scope.response = null;
		
		$http({
			method: 'POST', 
			url: 'http://127.0.0.1:8001/api-token-auth/',
			data:{
				username: $scope.username,
				password: $scope.password
			}						
		}).then(function successCallback(response) {
			console.log(response);
			$scope.response = response;
		}, function errorCallback(response) {
			console.log(response);
			$scope.response = response;
		});		
	}
}]);