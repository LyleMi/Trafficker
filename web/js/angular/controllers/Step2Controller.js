app.controller("Step2Controller", ["$scope", "$rootScope", "$state", "HttpService", function($scope, $rootScope, $state, HttpService) {

	$scope.Info = function() {

		HttpService.get("user/info", {}, function(response) {

			if (response.data.data) {
                alert('step2 run');
				$rootScope.submitInfo = response.data.data;
			}

		}, function(error) {

		});

	}

	$scope.Info();

	$scope.data = {
		currentMemberId: 0,
		selectedDate: new Date(),
		placeholders: {
			introduction: "着眼于特定的市场、竞争、经营、运作、管理、财务等策略方案，清楚描述公司的创业机会，500字以内，详细创业计划大纲可以另附",
			innovation: "（1000字以内）",
			difficulties: "（1000字以内）",
			expect: "每3个月为一个阶段（1000字以内）",
			feasibility: "包括自身及成员具备的知识条件、实践经历、已有的项目基础等（1000字以内）",
			structure: "包括团队成员分工、目前股权比例、未来期权计划等说明（1000字以内）",
			schedule: "包括市场调研、方案设计、企业实践、撰写创业计划、项目鉴定、其他等环节的时间安排 至少按6个月规划（1000字以内）"
		},

	};

	$scope.nextStep = function(valid) {
		if(!valid){
			alert("请按要求补充未填栏目");
			return;
		}
		
		HttpService.post("user/info", $rootScope.submitInfo, function(response) {
			$state.go("step3");
		}, function(error) {
			
		});

	};

	$scope.goBack = function() {
		$state.go("step1");
	};

}]);
