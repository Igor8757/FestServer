# The data for your website

data = {
  "news": [
    {
      "title": "News 1",
      "content": """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
          Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
    },
    {
      "title": "News 2",
      "content": """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
          Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
    },
    {
      "title": "News 3",
      "content": """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
          Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
    },
    {
      "title": "News 4",
      "content": """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
          Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
    },
    {
      "title": "News 5",
      "content": """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
          Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
    },
    {
      "title": "News 6",
      "content": """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
          Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
    },
    {
      "title": "News 7",
      "content": """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
          Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
    },
    {
      "title": "News 8",
      "content": """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
          Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
    }
  ],
  "about": [
    {
      "content": """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
      Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
      Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""",
      "youtubeURL": "https://www.youtube.com/embed/jbixaaxeKt0"
    }
  ],
  "sponsors": [
    {
      "name": "Sponsor Name 1",
      "imageURL": "/shared/images/sponsor.jpg"
    },
    {
      "name": "Sponsor Name 2",
      "imageURL": "/shared/images/sponsor.jpg"
    },
    {
      "name": "Sponsor Name 3",
      "imageURL": "/shared/images/sponsor.jpg"
    },
    {
      "name": "Sponsor Name 4",
      "imageURL": "/shared/images/sponsor.jpg"
    },
    {
      "name": "Sponsor Name 5",
      "imageURL": "/shared/images/sponsor.jpg"
    },
    {
      "name": "Sponsor Name 6",
      "imageURL": "/shared/images/sponsor.jpg"
    }
  ],
  "bands": [
        {
          "name": "Band Name 1",
          "imageURL": "/shared/images/band.jpg"
        },
        {
          "name": "Band Name 2",
          "imageURL": "/shared/images/band.jpg"
        },
        {
          "name": "Band Name 3",
          "imageURL": "/shared/images/band.jpg"
        },
        {
          "name": "Band Name 4",
          "imageURL": "/shared/images/band.jpg"
        },
        {
          "name": "Band Name 5",
          "imageURL": "/shared/images/band.jpg"
        },
        {
          "name": "Band Name 6",
          "imageURL": "/shared/images/band.jpg"
        },
        {
          "name": "Band Name 7",
          "imageURL": "/shared/images/band.jpg"
        },
        {
          "name": "Band Name 8",
          "imageURL": "/shared/images/band.jpg"
        },
        {
          "name": "Band Name 9",
          "imageURL": "/shared/images/band.jpg"
        }
      ]
}


def get_data(params):
    index = int(params.pop('_index', 0))
    length = int(params.pop('_length', 0))
    collection = params.pop('_collection')

    filtered_data = list(filter(lambda element: set(params.items()).issubset(set(element.items())),
                           data[collection]))

    return filtered_data[index:index + length] if length > 0 else filtered_data[index:]
