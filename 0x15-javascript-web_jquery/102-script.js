$(document).ready(function() {
  $('input#btn_translate').click(function() {
    // get the language code for translation
    var langCode = $('input#language_code').val()
    // construct the API URL
    var url = 'https://hellosalut.stefanbohacek.dev/?lang=' + langCode
    $.get(url, function(response, textStatus){
      $('div#hello').text(response.hello);
    });    
  });
});
