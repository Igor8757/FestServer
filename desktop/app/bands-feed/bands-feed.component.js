angular.
module('bandsFeed').
component('bandsFeed', {
  // Note: The URL is relative to our `index.html` file
  templateUrl: 'app/bands-feed/bands-feed.template.html',
  controller: function bandsFeedController($http) {
    var self = this;
    $http.get('/data?_collection=bands').then(function(response) {
        self.list = response.data;
    });
  }
});