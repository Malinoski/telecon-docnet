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
            		$location.path('/networks');
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
.factory("AuthenticationService", function($http, $cookieStore, $rootScope, $timeout, $location) {

    //  Function defined for when the user login is initiate
    var Login = function (username, password, callback) {
    	
    		var loginResponse = { 
    			success: false,
    			token: null    			
    		};
    		
    		$http.post(
    			$rootScope.webServerBaseUrl+'/api-token-auth/', 
    			{
    				username: username,
    				password: password
    			}	
    		).then(function successCallback(response) {
    			
    			console.log("AuthenticationService Login success!");
    			// console.log(response);
    			
    			loginResponse.success = true;
    			loginResponse.token = response.data.token;
    			callback(loginResponse);
    			
    		}, function errorCallback(response) {
    			
    			console.log("AuthenticationService Login failed!");
    			console.log(response);
    			
    			if(response.status === 400){
    				loginResponse.message = 'Username or password is incorrect, try "admin" and "admin" =)';
    			} else {
    				loginResponse.message = 'Some problem occurred in REST Web Server =(';
    			} 		
    			
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
        
        $rootScope.tokenHeaderConfig = {
        		headers: {
        			'Authorization': 'Token '+$rootScope.globals.currentUser.token
        		}
        };

        $http.defaults.headers.common['Authorization'] = 'Basic ' + authdata; 
        $cookieStore.put('globals', $rootScope.globals);
    };

    //  Clears the cookie and the state for the application to recognise a logged out state
    var ClearCredentials = function () {
    	
    		console.log("AuthenticationService ClearCredentials ...");
    		
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

