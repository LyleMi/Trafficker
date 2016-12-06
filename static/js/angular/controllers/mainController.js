app.controller("mainController", ["$scope", "$rootScope", "$state", "HttpService",
    function($scope, $rootScope, $state, HttpService) {
        $scope.data = {
            ARP: {
                arpop: 0,
                sendermac: 0,
                senderip: 0,
                targetmac: 0,
                targetip: 0,
            },
            ICMP: {
                type: 0,
                code: 0,
                checksum: 0,
                unused: 0,
                next_hop_mtu: 0,
            },
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
            UDP: {
                sport: 233,
                dport: 233,
                payload: '',
            },
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