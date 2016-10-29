app.controller("BeginController", ["$scope", "$rootScope", "$state", "HttpService", function($scope, $rootScope, $state, HttpService) {
    $scope.nextStep = function() {
        $state.go("step1");
    };

}]);