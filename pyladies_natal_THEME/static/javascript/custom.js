$(document).ready(function() {
  $('.ui.rating').rating();

  $('.ui.dropdown').dropdown();

  $('.ui.checkbox').checkbox();

  // $('.remove-serie').click(function () {
  //   $('.basic.modal').modal('show');

  //   var url = '/series/' + $(this).attr('data-serie') + '/delete';
  //   $('.basic.modal form').attr('action', url);
  // });

  // $('.rating').click(function () {
  //   var rating_block = $(this).parents('.rating'),
  //       serie_id = $(this).attr('data-serie'),
  //       rating = $(this).find('.active').length;

  //   $.ajax({
  //       url: '/series/' + serie_id + '/rating/' + rating,
  //       type: 'POST'
  //   });
  // });
});