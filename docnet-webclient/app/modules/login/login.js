'use strict';

angular.module('myApp.login', ['ngRoute'])
.config(['$routeProvider', function($routeProvider) {
	
	$routeProvider.when('/login', {
		templateUrl: 'modules/login/login.html',
		controller: 'LoginCtrl'
	});
	
}])
.controller('LoginCtrl', [ '$rootScope', '$scope', '$http', '$location', 'AuthenticationService', function($rootScope, $scope, $http, $location, AuthenticationService) {
	
	AuthenticationService.ClearCredentials();
	
	$scope.login = function (username, password) {
		
		$scope.dataLoading = true;
        AuthenticationService.Login(username, password, function(response) {
            if(response.success) {
                // AuthenticationService.SetCredentials(username, password);
            		AuthenticationService.SetCredentials(username, response.token);
            		$location.path('/');
            } else {
                $scope.error = response.message;
                $scope.dataLoading = false;
            }
        });
    };
    
    $rootScope.logout = function(){
		AuthenticationService.ClearCredentials();
	}
	
}])
.factory("AuthenticationService", function($http, $cookieStore, $rootScope, $timeout) {

    //  Function defined for when the user login is initiate
    var Login = function (username, password, callback) {
    	
    		var loginResponse = { 
    			success: false,
    			token: null    			
    		};
    		
    		$http({
			method: 'POST', 
			url: $rootScope.webServerBaseUrl+'/api-token-auth/',
			data:{
				username: username,
				password: password
			}						
		}).then(function successCallback(response) {
			
			loginResponse.success = true;
			loginResponse.token = response.data.token;
			callback(loginResponse);
			
		}, function errorCallback(response) {
			
			loginResponse.message = 'Username or password is incorrect, try "admin" and "admin" =)';
			callback(loginResponse);
			
		}).finally(function() {
			// If needed
		});		
        
    };

    //  Sets the cookie and the state to logged in
    var SetCredentials = function (username, token) {
        var authdata = username + ':' + token;
        $rootScope.globals = {
            currentUser: {
                username: username,
                authdata: authdata,
                token:token
            }
        };

        $http.defaults.headers.common['Authorization'] = 'Basic ' + authdata; 
        $cookieStore.put('globals', $rootScope.globals);
    };

    //  Clears the cookie and the state for the application to recognise a logged out state
    var ClearCredentials = function () {
        $rootScope.globals = {};
        $cookieStore.remove('globals');
        $http.defaults.headers.common.Authorization = 'Basic ';
    };

	return {
		Login: Login,
		SetCredentials: SetCredentials,
		ClearCredentials: ClearCredentials
	};

})
.run(function($rootScope, $location, $cookieStore, $http) {
	// keep user logged in after page refresh
	$rootScope.globals = $cookieStore.get('globals') || {};
	if ($rootScope.globals.currentUser) {
		$http.defaults.headers.common['Authorization'] = 'Basic ' + $rootScope.globals.currentUser.authdata; 
	}
    
	$rootScope.$on('$locationChangeStart', function (event, next, current) {
		// redirect to login page if not logged in
		if ($location.path() !== '/login' && !$rootScope.globals.currentUser) {
			$location.path('/login');
		}
	});
});

