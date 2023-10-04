$(document).ready(function () {
  $('input#btn_translate').click(function () {
    translate();
  });

  $('input#language_code').keyup(function (event) {
    if (event.keyCode === 13) {
      // Enter key
      translate();
    }
  });

  function translate () {
    // get the language code for translation
    var langCode = $('input#language_code').val();
    // construct the API URL
    var url = 'https://hellosalut.stefanbohacek.dev/?lang=' + langCode;
    $.get(url, function (response, textStatus) {
      $('div#hello').text(response.hello);
    });
  }
});
