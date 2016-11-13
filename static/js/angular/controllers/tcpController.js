app.controller("tcpController", ["$scope", "$rootScope", "$state", "HttpService",
    function($scope, $rootScope, $state, HttpService) {
        $scope.data = {
            TCP: {
                sport: 2333,
                dport: 30,
                seq: 10,
                ack: 0,
                offset: 5,
                reserved: 0,
                urg: 0,
                ack: 0,
                psh: 0,
                rst: 0,
                syn: 1,
                fin: 0,
                window: 53270,
                chksum: 0,
                urgp: 0,
                payload: 0,
                options: '',
            },
        }
    }
]);