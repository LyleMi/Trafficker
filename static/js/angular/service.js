var host = "http://localhost:8888/";

app.factory("HttpService", function($http) {

	return {
		get: function(path, params, successCallBack, failureCallBack) {
			params = params || {};

			$http({
				method: 'GET',
				url: host + path,
				params: params,
				headers: {
					'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
				}
			}).then(function(response) {
				successCallBack(response);
			}, function(error) {
				failureCallBack(error);
			});
		},
		post: function(path, params, successCallBack, failureCallBack) {
			params = params || {};

			$http({
				method: 'POST',
				url: host + path,
				data: $.param(params),
				headers: {
					'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
				}
			}).then(function(response) {
				successCallBack(response);
			}, function(error) {
				failureCallBack(error);
			});
		},
	}

});

app.factory("GlobalFunctions", function($rootScope, HttpService) {
	return {
		deepCopy: function(source) {
			if (source instanceof Array) {
				var result = [];
				for (var key in source)
					result.push(typeof source[key] === 'object' ? this.deepCopy(source[key]) : source[key]);
			} else {
				var result = {};
				for (var key in source)
					result[key] = typeof source[key] === 'object' ? this.deepCopy(source[key]) : source[key];
			}
			return result;
		},
	}

});