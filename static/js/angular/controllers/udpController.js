app.controller("udpController", ["$scope", "$rootScope", "$state", "HttpService",
    function($scope, $rootScope, $state, HttpService) {
        $scope.data = {
            UDP: {
                sport: 233,
                dport: 233,
                payload: '',
            },
        }
    }
]);