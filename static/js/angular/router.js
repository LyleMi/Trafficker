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
			controller: "mainController"
		})
		.state("tcp", {
			url: "/tcp",
			templateUrl: "static/templates/tcp.html",
			controller: "mainController"
		})
		.state("udp", {
			url: "/udp",
			templateUrl: "static/templates/udp.html",
			controller: "mainController"
		})
		.state("arp", {
			url: "/arp",
			templateUrl: "static/templates/arp.html",
			controller: "mainController"
		})
		.state("icmp", {
			url: "/icmp",
			templateUrl: "static/templates/icmp.html",
			controller: "mainController"
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