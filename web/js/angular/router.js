app.config(["$stateProvider", "$urlRouterProvider", function($stateProvider, $urlRouterProvider) {

	$urlRouterProvider.otherwise("/http");

	$stateProvider
		.state("http", {
			url: "/http",
			templateUrl: "templates/http.html",
			controller: "httpController"
		})
		.state("ip", {
			url: "/ip",
			templateUrl: "templates/ip.html",
			controller: "ipController"
		})
		.state("tcp", {
			url: "/tcp",
			templateUrl: "templates/tcp.html",
			controller: "tcpController"
		})
		.state("udp", {
			url: "/udp",
			templateUrl: "templates/udp.html",
			controller: "udpController"
		});

}]);