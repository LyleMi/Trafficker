app.controller("ipController", ["$scope", "$rootScope", "$state", "HttpService",
    function($scope, $rootScope, $state, HttpService) {
        $scope.data = {
            Ether: {
                mac_dst: 'ff:ff:ff:ff:ff:ff',
                mac_src: '00:00:00:00:00:00',
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
            }
        };

        $scope.send_ip = function() {
            HttpService.post('ip', $scope.data, function() {}, function() {});
            console.log('this is send ip');
        }

    }
]);