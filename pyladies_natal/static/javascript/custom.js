$(document).ready(function() {
  $('.rating').rating();

  $('.ui.dropdown').dropdown();

  $('.ui.checkbox').checkbox();

  $('.remove-serie').click(function () {
    var url = '/series/' + $(this).attr('data-serie') + '/delete/';
    $('.basic.modal form').attr('action', url);

    $('.basic.modal').modal('show');
  });

  $('.rating').click(function () {
    var serie_id = $(this).attr('data-serie'),
        rating = $(this).find('.active').length,
        url = '/series/' + serie_id + '/rating/' + rating + '/';

    $.ajax({url: url, type: 'GET'});
  });
});
