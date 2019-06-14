angular.module('totalPrice', [])
    .component('totalPrice', {
        template: '<div class="container" ng-controller="totalPriceController">' + 
                            '<h3>Number of Tickets</h3>' +
                            '<input type="number" id="tickets" name="quantity" min="1" placeholder="1" ng-change="newTotal(ticketsNum)" ng-model="ticketsNum">' +            
                        '<hr><p>Total<span class="price" style="color:black" ><b name="price" >{{total}}$</b></span></p>' +
                    '</div>',
    })
    .controller('totalPriceController', ['$scope', function ($scope) {
        $scope.newTotal = function (ticketsNum) {
            console.log(ticketsNum);
            $scope.total = 35 * ticketsNum
        }
    }]);