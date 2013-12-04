(function($){

  $.ajax({
    method: 'GET',
    dataType: 'jsonp',
    url: '/api/comments/'
  }).done(function(data){

    // dummy colors
    var colours = {};
    colours['-6'] = { bg: '#871d10', color: '#fff'};
    colours['-5'] = { bg: '#b53929', color: '#fff'};
    colours['-4'] = { bg: '#c7542f', color: '#fff'};
    colours['-3'] = { bg: '#ca7631', color: '#fff'};
    colours['-2'] = { bg: '#daa538', color: '#fff'};
    colours['-1'] = { bg: '#e7c358', color: '#555'};
    colours['0'] = { bg: '#ffffff', color: '#666'};
    colours['1'] = { bg: '#e8f19f', color: '#555'};
    colours['2'] = { bg: '#c6d746', color: '#666'};
    colours['3'] = { bg: '#84a51f', color: '#ccc'};
    colours['4'] = { bg: '#3d7212', color: '#fff'};
    colours['5'] = { bg: '#1c3f06', color: '#fff'};
    colours['6'] = { bg: '#102403', color: '#fff'};

    $('.comments li').each(function() {
      var sentiment = $(this).data('sentiment');
      var bar = $(this).find('.sentiment-num');
      $(bar).css('color', colours[sentiment].color);
      $(bar).css('background-color', colours[sentiment].bg);
    });

  });

})(jQuery);