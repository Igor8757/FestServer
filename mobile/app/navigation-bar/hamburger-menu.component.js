angular.module('hamburgerMenu', [])
    .component('hamburgerMenu', {
        template: 
        '<div ng-controller="hamburgerController">' +
            '<input type="image" src="../images/hamburger.png" class="hamburger-menu-button" ng-click="ShowHide()"/>' + 
            '<div class="hamburger-menu-content" ng-hide="IsInvisible">' +
                '<ul class="menu-list">' +
                    '<a class="menu-item" href="index.html">Home</a>' +
                    '<a class="menu-item" href="about.html">About</a>'+
                    '<a class="menu-item" href="bands.html">Bands</a>'+
                    '<a class="menu-item" href="tickets.html">Tickets</a>'+
                    '<a class="menu-item" href="https://www.facebook.com/SquattingSlavs/">'+
                        '<img src="/shared/images/facebook.png"' +
                        'style="max-height: 45px; max-width: 45px;"></a>' +
                '</ul>' +
            '</div>' +
        '</div>'
    })
    .controller('hamburgerController',['$scope', function($scope){
    $scope.IsInvisible = true;

    $scope.ShowHide = function(){
        console.log($scope.IsInvisible)
        $scope.IsInvisible = !($scope.IsInvisible);
    }
    }]);
    