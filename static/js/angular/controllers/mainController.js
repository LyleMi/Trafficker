app.controller("mainController", ["$scope", "$rootScope", "$state", "HttpService",
    function($scope, $rootScope, $state, HttpService) {
        $scope.data = {
            ARP: {
                arpop: 1,
                sendermac: 'FF:FF:FF:FF:FF:FF',
                senderip: '127.0.0.1',
                targetmac: '00:00:00:00:00:00',
                targetip: '192.168.1.1',
            },
            ICMP: {
                type: 0,
                code: 8,
                checksum: 0,
                ident: 0,
                seq: 0,
                payload: 'abcdefghijklm',
            },
            MAC: {
                dst: 'FF:FF:FF:FF:FF:FF',
                src: 'FF:FF:FF:FF:FF:FF',
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
                srcp: 23333,
                dstp: 19992,
                payload: 'AABBCCDD',
            },
            TCP: {
                srcp: 2333,
                dstp: 30333,
                seqnumber: 10,
                acknumber: 0,
                offset: 8,
                reserved: 0,
                urg: 0,
                ack: 0,
                psh: 0,
                rst: 0,
                syn: 1,
                fin: 0,
                window: 53270,
                checksum: 0,
                urgp: 0,
                payload: 0,
                options: '',
            },
        };

        // console.log('arp');

        $scope.cu = function() {
            console.log($state.current.name);
            switch($state.current.name)
            {
                case "ip":
                    $scope.send_ip();
                    break;
                case "arp":
                    $scope.send_arp();
                    break;
                case "icmp":
                    $scope.send_icmp();
                    break;
                case "tcp":
                    $scope.send_tcp();
                    break;
                case "udp":
                    $scope.send_udp();
                    break;
                default:
                    break;
            }


        }

        $scope.send_arp = function() {
            HttpService.post('arp', {
                    'arp': JSON.stringify($scope.data.ARP),
                    'mac': JSON.stringify($scope.data.MAC)
                },
                function(response) {
                    console.log(response);
                    // $scope.data.result = JSON.stringify(response.data);
                },
                function(err) { console.log(err)});
        }

        $scope.send_ip = function() {
            HttpService.post('ip', {
                    'mac': JSON.stringify($scope.data.MAC),
                    'ip': JSON.stringify($scope.data.IP)
                },
                function(response) {
                    console.log(response);
                    // $scope.data.result = JSON.stringify(response.data);
                },
                function() {});
        }

        $scope.send_udp = function() {
            HttpService.post('udp', {
                    'mac': JSON.stringify($scope.data.MAC),
                    'ip': JSON.stringify($scope.data.IP),
                    'udp': JSON.stringify($scope.data.UDP)
                },
                function(response) {
                    console.log(response);
                    // $scope.data.result = JSON.stringify(response.data);
                },
                function() {});
        }

        $scope.send_tcp = function() {
            HttpService.post('tcp', {
                    'mac': JSON.stringify($scope.data.MAC),
                    'ip': JSON.stringify($scope.data.IP),
                    'tcp': JSON.stringify($scope.data.TCP)
                },
                function(response) {
                    console.log(response);
                    // $scope.data.result = JSON.stringify(response.data);
                },
                function() {});
        }

        $scope.send_icmp = function() {
            HttpService.post('icmp', {
                    'mac': JSON.stringify($scope.data.MAC),
                    'ip': JSON.stringify($scope.data.IP),
                    'icmp': JSON.stringify($scope.data.ICMP)
                },
                function(response) {
                    console.log(response);
                    // $scope.data.result = JSON.stringify(response.data);
                },
                function() {});
        }
    }
]);