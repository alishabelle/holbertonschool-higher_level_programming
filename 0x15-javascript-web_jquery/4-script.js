$('DIV#toggle_header').click(function () {
  if ($('HEADER').hasClass('red')) {
    $('HEADER').addClass('green');
    $('HEADER').removeClass('red');
    $('HEADER').css('green', '#00FF00');
  } else {
    $('HEADER').removeClass('green');
    $('HEADER').addClass('red');
    $('HEADER').css('red', '#FF0000');
  }
});
