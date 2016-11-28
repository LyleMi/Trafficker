app.controller("ipController", ["$scope", "$rootScope", "$state", "HttpService",
    function($scope, $rootScope, $state, HttpService) {
        $scope.data = {
            mac: {
                dst: 'ff:ff:ff:ff:ff:ff',
                src: '00:00:00:00:00:00',
                type: 0x0800
            },
            IP: {
                version: 4, // 4 bits
                ihl: 20, // head length 4 bits
                tos: 0, // tyoe of service 8 bits
                id: 512, // total len 16 bits
                flags: 0, // 3 bits
                offset: 0, // 3 bits
                ttl: 64, // 8 bits
                proto: 6, // 8 bits
                checksum: 0, // 16 bits
                src: '127.0.0.1', // 32 bits
                dst: '127.0.0.1', // 32 bits
                options: 0,
                payload: '',
            },
            result: ''
        };

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