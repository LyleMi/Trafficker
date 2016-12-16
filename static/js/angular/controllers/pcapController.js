app.controller("pcapController", ["$scope", "$rootScope", "$state", "HttpService",
    function($scope, $rootScope, $state, HttpService) {

        $scope.data = {
            pcaps : [],
        }

        $scope.getpcaps = function() {
            HttpService.get('pcap', {},
                function(response) {
                    $scope.data.pcaps = response.data;
                    // console.log(response);
                },
                function() {});
        }

        $scope.getpcaps();

        $scope.choosepcap = function () {
            $("#pcap").click();
        }
    }
]);