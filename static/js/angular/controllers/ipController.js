app.controller("ipController", ["$scope", "$rootScope", "$state", "HttpService",
    function($scope, $rootScope, $state, HttpService) {
        $scope.data = {
            mac: {
                dst: 'ff:ff:ff:ff:ff:ff',
                src: '00:00:00:00:00:00',
                type: 36864
            },
            IP: {
                version: '',
                ihl: '',
                tos: '',
                len: '',
                flags: '',
                flag: '',
                ttl: '',
                proto: '',
                chksum: '',
                src: '',
                dst: '',
                options: '',
            },
            result: ''
        };

        $scope.send_ip = function() {
            HttpService.post('ip',
                {
                    'mac' : JSON.stringify($scope.data.mac),
                    'ip' : JSON.stringify($scope.data.ip)
                },
                function(response) {
                    $scope.data.result = JSON.stringify(response.data);
                },
                function() {});
        }

    }
]);