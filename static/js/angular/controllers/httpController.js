app.controller("httpController", ["$scope", "$rootScope", "$state", "HttpService",
    function($scope, $rootScope, $state, HttpService) {
        
        $scope.sendRequest = function() {

            $.ajax({
                url: $('#url').val(),
                type: $("input[name='method']:checked").val(),
                data: $('#params').val(),
                //dataType:'JSONP',
                success: function(response) {
                    $('#text_result').val(response);
                    $('#html_result').html(response);
                    $('#json_result').html('<pre>' + jsonFormat(response) + '</pre>');
                },
                error: function(response) {
                    $('#text_result').val(JSON.stringify(response));
                    $('#html_result').html(JSON.stringify(response));

                },
            });

        }

        $scope.jsonFormat = function(json, options) {

            var reg = null,
                formatted = '',
                pad = 0,
                PADDING = '    ';

            options = options || {};
            options.newlineAfterColonIfBeforeBraceOrBracket = (options.newlineAfterColonIfBeforeBraceOrBracket === true) ? true : false;
            options.spaceAfterColon = (options.spaceAfterColon === false) ? false : true;

            if (typeof json !== 'string') {
                json = JSON.stringify(json);
            } else {
                json = JSON.parse(json);
                json = JSON.stringify(json);
            }

            reg = /([\{\}])/g;
            json = json.replace(reg, '\r\n$1\r\n');

            reg = /([\[\]])/g;
            json = json.replace(reg, '\r\n$1\r\n');

            reg = /(\,)/g;
            json = json.replace(reg, '$1\r\n');

            reg = /(\r\n\r\n)/g;
            json = json.replace(reg, '\r\n');

            reg = /\r\n\,/g;
            json = json.replace(reg, ',');

            if (!options.newlineAfterColonIfBeforeBraceOrBracket) {
                reg = /\:\r\n\{/g;
                json = json.replace(reg, ':{');
                reg = /\:\r\n\[/g;
                json = json.replace(reg, ':[');
            }
            if (options.spaceAfterColon) {
                reg = /\:/g;
                json = json.replace(reg, ': ');
            }

            $.each(json.split('\r\n'), function(index, node) {
                var i = 0,
                    indent = 0,
                    padding = '';

                if (node.match(/\{$/) || node.match(/\[$/)) {
                    indent = 1;
                } else if (node.match(/\}/) || node.match(/\]/)) {
                    if (pad !== 0) {
                        pad -= 1;
                    }
                } else {
                    indent = 0;
                }

                for (i = 0; i < pad; i++) {
                    padding += PADDING;
                }

                formatted += padding + node + '\r\n';
                pad += indent;
            });

            return formatted;
        }

        $scope.ClearResponse = function() {
            $('#text_result').val('');
            $('#html_result').html('');
            $('#json_result').html('');
        }
    }
]);