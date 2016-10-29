app.controller("Step3Controller", ["$scope", "$rootScope", "$state", "$timeout", "GlobalFunctions", "HttpService", function($scope, $rootScope, $state, $timeout, GlobalFunctions, HttpService) {

	$scope.Info = function() {

		HttpService.get("user/info", {}, function(response) {

			if(response.data.data) {
                alert('step3 run');
				$rootScope.submitInfo = response.data.data;
				$("#spaceSelectBtn").text($rootScope.submitInfo.project.space);
				$rootScope.submitInfo.project.resume = $rootScope.submitInfo.project.resume ? $rootScope.submitInfo.project.resume : {};
				$rootScope.submitInfo.project.BP = $rootScope.submitInfo.project.BP ? $rootScope.submitInfo.project.BP : {};
				$rootScope.submitInfo.project.ppt = $rootScope.submitInfo.project.ppt ? $rootScope.submitInfo.project.ppt : {};
			}

		}, function(error) {

		});

	}

	$scope.Info();

	$scope.data = {
		spaces: ["开放空位", "40平方米以下", "40-100平方米", "100-200平方米", "200平方米以上"],
	};
	$scope.nextStep = function(valid) {
		
		if(!valid){
			alert("请按要求补充未填栏目");
			return;
		}
		
		if($rootScope.submitInfo.project.space.length === 0){
			alert("请选择场地需求。");
			return;
		};
		
		if(!$rootScope.submitInfo.project.resume.fname){
			alert("请上传负责人或主创团队简历。");
			return;
		};
		
		if(!$rootScope.submitInfo.project.BP.fname){
			alert("请上传项目BP。");
			return;
		};
		
		if(!$rootScope.submitInfo.project.ppt.fname){
			alert("请上传项目PPT。");
			return;
		};
		
		$rootScope.submitInfo.project.complete = 'C';

		HttpService.post("user/info", $rootScope.submitInfo, function(response) {
			$state.go("succeed");
		}, function(error) {

		});
		
	};

	$scope.goBack = function() {
		$state.go("step2");
	};

	$scope.selectSpace = function(space, index) {
		$("#spaceSelectBtn").text(space);
		$rootScope.submitInfo.project.space = space;
	};

	$scope.sendEmail = function() {

	};

	GlobalFunctions.initQiNiuElement("resumeFileBtn", "resumeFileContainer", 'resume', function(file) {

	}, function(file) {

	}, function(file, info) {
		// console.log(file);
		// console.log(file.id);
		HttpService.post("file/callback", {
			fid: JSON.parse(info).key,
			fname: file.name,
			fsize: file.size,
			type: 'resume'
		}, function(response) {}, function(error) {

		});
		$timeout(function() {
			$rootScope.submitInfo.project.resume.fname = file.name;
		}, 0);
	}, function(err) {

	});

	GlobalFunctions.initQiNiuElement("BPFileBtn", "BPFileContainer", 'BP', function(file) {

	}, function(file) {

	}, function(file, info) {
		HttpService.post("file/callback", {
			fid: JSON.parse(info).key,
			fname: file.name,
			fsize: file.size,
			type: 'BP'
		}, function(response) {}, function(error) {

		});
		$timeout(function() {
			$rootScope.submitInfo.project.BP.fname = file.name;
		}, 0);
	}, function(err) {

	});

	GlobalFunctions.initQiNiuElement("pptFileBtn", "pptFileContainer", 'ppt', function(file) {

	}, function(file) {

	}, function(file, info) {
		HttpService.post("file/callback", {
			fid: JSON.parse(info).key,
			fname: file.name,
			fsize: file.size,
			type: 'ppt'
		}, function(response) {}, function(error) {

		});
		$timeout(function() {
			$rootScope.submitInfo.project.ppt.fname = file.name;
		}, 0);
	}, function(err) {

	});

}]);
