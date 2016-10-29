app.controller("Step1Controller", ["$scope", "$rootScope", "$state", "$timeout", "HttpService", function($scope, $rootScope, $state, $timeout, HttpService) {

	$scope.Info = function() {

		HttpService.get("user/info", {}, function(response) {

			if (response.data.data) {
alert('step1 run');
				$rootScope.submitInfo = response.data.data;
				$("#fieldSelectBtn").text($rootScope.submitInfo.project.field);
			}

			if (!$rootScope.submitInfo.members) {
				$rootScope.submitInfo.members = [{
					order: 0,
					name: "",
					birth: "",
					school: "",
					major: "",
					phone: "",
					email: "",
					resume: ""
				}, {
					order: 1,
					name: "",
					birth: "",
					school: "",
					major: "",
					phone: "",
					email: "",
					resume: ""
				}, ]
			} else {
				if ($rootScope.submitInfo.members.length == 1) {
					$rootScope.submitInfo.members.push({
						order: 1,
						name: "",
						birth: "",
						school: "",
						major: "",
						phone: "",
						email: "",
						resume: ""
					});
				}
			}



		}, function(error) {

		});

	}

	$scope.Info();

	$scope.data = {
		selectedDate: new Date(),
		fields: ["电子信息技术", "生物与新医药技术", "航空航天技术", "新材料技术", "高技术服务业", "新能源及节能技术", "资源与环境技术", "高新技术改造传统产业", "其他（请输入技术领域）"],
		showFieldInput: false,
	};

	$rootScope.$watch("submitInfo.members.length", function(newValue, oldValue) {
		$timeout(function() {
			$(".nb-input-datepicker").datepicker({
				language: "zh-CN",
				autoclose: true,
				format: "yyyy-mm-dd",
				startView: 2,
				todayHighlight: true,
				orientation: "bottom",
				container: ".container"
			});

		}, 0);
	});

	$scope.selectField = function(field, index) {
		if (index === $scope.data.fields.length - 1) {
			$rootScope.submitInfo.project.field = "";
			$scope.data.showFieldInput = true;
			$timeout(function() {
				$("#fieldInput").focus();

			}, 0);

		} else {
			if ($scope.data.showFieldInput) {
				$scope.data.showFieldInput = false;
			};

			$("#fieldSelectBtn").text(field);
			$rootScope.submitInfo.project.field = field;
		};

	};

	$scope.memberInfoRequired = function(index) {
		if (index !== 1 || index === 1 && $rootScope.submitInfo.members.length > 2) {
			return true;
		};

		return false;
	};

	$scope.addNewMember = function() {
		var memberInfo = {
			id: $rootScope.submitInfo.members.length,
			name: "",
			birth: "",
			school: "",
			major: "",
			phone: "",
			email: "",
			resume: ""
		};

		$rootScope.submitInfo.members.push(memberInfo);
	};

	$scope.removeMember = function(index) {
		$rootScope.submitInfo.members.splice(index, 1);
		HttpService.delete("user/member" + "?order=" + index, {}, function(response) {

		}, function(error) {

		});

	};

	$scope.nextStep = function(valid) {
		if(!valid){
			alert("请按要求补充未填栏目");
			return;
		}

		if ($rootScope.submitInfo.project.field.length === 0) {
			alert("请选择国家重点支持高新技术领域。");
			return;
		};

		var pFlag = true;
		var regP = /^1[3|4|5|7|8]\d{9}$/;
		// for (var index in $rootScope.submitInfo.members) {
		// 	var temp = $rootScope.submitInfo.members[index];
		// 	if (temp.phone.length > 0 && !regP.test(temp.phone)) {
		// 		pFlag = false;
		// 		break;
		// 	};
		// };

		if (!pFlag) {
			alert("输入的手机号码格式不正确");
			return;
		}

		//		if($rootScope.submitInfo.members.length === 2) {
		//			var allDone = true;
		//
		//			for(var key in $rootScope.submitInfo.members[1]) {
		//				var temp = $rootScope.submitInfo.members[1][key];
		//				if(temp.length === 0) {
		//					allDone = false;
		//					break;
		//				};
		//			};
		//
		//			if(!allDone) {
		//				$rootScope.submitInfo.members.splice(1, 1);
		//			};
		//		};

		HttpService.post("user/info", $rootScope.submitInfo, function(response) {
			$state.go("step2");

		}, function(error) {

		});

	};
	

}]);
