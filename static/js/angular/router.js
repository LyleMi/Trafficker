app.config(["$stateProvider", "$urlRouterProvider", function($stateProvider, $urlRouterProvider) {

	$urlRouterProvider.otherwise("/ip");

	$stateProvider
		.state("http", {
			url: "/http",
			templateUrl: "static/templates/http.html",
			controller: "httpController"
		})
		.state("ip", {
			url: "/ip",
			templateUrl: "static/templates/ip.html",
			controller: "ipController"
		})
		.state("tcp", {
			url: "/tcp",
			templateUrl: "static/templates/tcp.html",
			controller: "tcpController"
		})
		.state("udp", {
			url: "/udp",
			templateUrl: "static/templates/udp.html",
			controller: "udpController"
		})
		.state("arp", {
			url: "/arp",
			templateUrl: "static/templates/arp.html",
			controller: "udpController"
		})
		.state("icmp", {
			url: "/icmp",
			templateUrl: "static/templates/icmp.html",
			controller: "udpController"
		})
		.state("pcap", {
			url: "/pcap",
			templateUrl: "static/templates/pcap.html",
			controller: "udpController"
		});

}]);