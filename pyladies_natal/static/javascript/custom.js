$(document).ready(function() {
  $('.ui.rating').rating();

  $('.ui.dropdown').dropdown();

  $('.ui.checkbox').checkbox();

  $('.remove-serie').click(function () {
    $('.basic.modal').modal('show')
  });
});