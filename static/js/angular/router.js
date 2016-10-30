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
		});

}]);