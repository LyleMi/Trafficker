app.controller("TestController", ["$scope", "$rootScope", "$state", "HttpService", function($scope, $rootScope, $state, HttpService) {
    $rootScope.submitInfo = {
        project: {
            name: "123",
            field: "2134",
            numbers: "123",
            introduction: "124",
            innovation: "123",
            difficulties: "124",
            expect: "123",
            feasibility: "123",
            structure: "124",
            schedule: "123",
            space: "123",
            guidance: "asdf",
            investment: "sf",
            policy: "asd",
            others: "",
            resume: "",
            BP: "",
            ppt: "",
            //status:"D"
        },
        members: [{
                order: 1,
                name: "12xzc3",
                birth: "123",
                school: "12asd3",
                major: "1asd23",
                phone: "12zcxsad3",
                email: "123",
                resume: "123"
            }, {
                order: 2,
                name: "123",
                birth: "aasdsd",
                school: "23asd1",
                major: "12asd3",
                phone: "1zxc23",
                email: "123",
                resume: "123"
            },

        ],
    };


    $scope.test = function() {
        HttpService.post("/user/info", ($rootScope.submitInfo), function(response) {
            console.log(response);
        }, function(error) {

        });
    };

}]);