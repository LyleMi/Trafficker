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
		})
		.state("tcp", {
			url: "/tcp",
			templateUrl: "static/templates/tcp.html",
		})
		.state("udp", {
			url: "/udp",
			templateUrl: "static/templates/udp.html",
		})
		.state("arp", {
			url: "/arp",
			templateUrl: "static/templates/arp.html",
		})
		.state("icmp", {
			url: "/icmp",
			templateUrl: "static/templates/icmp.html",
		})
		.state("pcap", {
			url: "/pcap",
			templateUrl: "static/templates/pcap.html",
			controller: "pcapController"
		});
		// .state("hex", {
		// 	url: "/hex",
		// 	templateUrl: "static/templates/hex.html",
		// 	controller: "mainController"
		// });

}]);