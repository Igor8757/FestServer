angular.
module('aboutFeed').
component('aboutFeed', {
  // Note: The URL is relative to our `index.html` file
  templateUrl: 'app/about-feed/about-feed.template.html',
  controller: function aboutFeedController($http) {
    var self = this;
    $http.get('/data?_collection=about').then(function(response) {
        self.list = response.data;
    });
    $http.get('/data?_collection=sponsors').then(function(response) {
      self.slist = response.data;
  });
  }
});