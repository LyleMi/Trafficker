app.controller("arpController", ["$scope", "$rootScope", "$state", "HttpService",
    function($scope, $rootScope, $state, HttpService) {
        $scope.data = {
            ARP: {
                arpop: 0,
                sendermac: 0,
                senderip: 0,
                targetmac: 0,
                targetip: 0,
            },
        };

        // console.log('arp');

        $scope.send_arp = function() {
            HttpService.post('arp', {
                    'arp': JSON.stringify($scope.data.ARP),
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