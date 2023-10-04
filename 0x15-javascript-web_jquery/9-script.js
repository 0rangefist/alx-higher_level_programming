$(document).ready(function() {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(response, textStatus){
    $('div#hello').text(response.hello);
  });
});
