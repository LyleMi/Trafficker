app.controller("tcpController", ["$scope", "$rootScope", "$state", "HttpService",
    function($scope, $rootScope, $state, HttpService) {
        $scope.data = {
            TCP: {
                sport: '',
                dport: '',
                seq: '',
                ack: '',
                dataofs: '',
                reserved: '',
                flags: '',
                window: '',
                chksum: '',
                urgptr: '',
                options: '',
            },
        }
    }
]);