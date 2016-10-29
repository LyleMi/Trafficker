app.config(["$stateProvider", "$urlRouterProvider", function($stateProvider, $urlRouterProvider) {

	$urlRouterProvider.otherwise("/begin");

	$stateProvider
		.state("step1", {
			url: "/step1",
			templateUrl: "templates/join-step1.html",
			controller: "Step1Controller"

		})
		.state("step2", {
			url: "/step2",
			templateUrl: "templates/join-step2.html",
			controller: "Step2Controller"
		})
		.state("step3", {
			url: "/step3",
			templateUrl: "templates/join-step3.html",
			controller: "Step3Controller"
		})
		.state("succeed", {
			url: "/succeed",
			templateUrl: "templates/join-succeed.html"
		})
		.state("begin", {
			url: "/begin",
			templateUrl: "templates/join-begin.html",
			controller: "BeginController"
		})
		.state("test", {
			url: "/test",
			templateUrl: "templates/test.html",
			controller: "TestController"
		});

}]);