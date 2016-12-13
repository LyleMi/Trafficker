app.controller("mainController", ["$scope", "$rootScope", "$state", "HttpService",
    function($scope, $rootScope, $state, HttpService) {
        $scope.data = {
            ARP: {
                arpop: 1,
                sendermac: '00:0c:29:86:1c:1b',
                senderip: '192.168.33.254',
                targetmac: '00:00:00:00:00:00',
                targetip: '202.120.2.101',
            },
            ICMP: {
                type: 8,
                code: 0,
                checksum: 0,
                ident: 3864,
                seq: 1,
                payload: 'abcdefghijklm',
            },
            MAC: {
                dst: 'FF:FF:FF:FF:FF:FF',
                src: '00:0c:29:86:1c:1b',
                type: 0x0800
            },
            IP: {
                version: 4, // 4 bits
                ihl: 5, // head length 4 bits
                tos: 0, // tyoe of service 8 bits
                id: 29849, // total len 16 bits
                flags: 2, // 3 bits
                offset: 0, // 3 bits
                ttl: 64, // 8 bits
                proto: 6, // 8 bits
                checksum: 0, // 16 bits
                src: '192.168.33.254', // 32 bits
                dst: '192.168.33.11', // 32 bits
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
                payload: '',
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