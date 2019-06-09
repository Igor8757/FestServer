angular.
module('newsFeed').
component('newsFeed', {
  // Note: The URL is relative to our `index.html` file
  templateUrl: 'app/news-feed/news-feed.template.html',
  controller: function newsFeedController($http) {
    var self = this;
    $http.get('/data?_collection=news').then(function(response) {
        self.list = response.data;
    });
  }
});