app.controller("icmpController", ["$scope", "$rootScope", "$state", "HttpService",
    function($scope, $rootScope, $state, HttpService) {
        $scope.data = {

        }


        $scope.send_ip = function() {
            HttpService.post('ip', {
                    'mac': JSON.stringify($scope.data.mac),
                    'ip': JSON.stringify($scope.data.IP)
                },
                function(response) {
                    console.log(response);
                    // $scope.data.result = JSON.stringify(response.data);
                },
                function() {});
        }
    }
]);