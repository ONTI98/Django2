
  $.ajaxSetup({
    headers: {
      'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content') // for Laravel, Django, etc.
    }
  });

  $(document).ready(function () {
    $('#myButton').click(function () {
      $.ajax({
        url: 'https://jsonplaceholder.typicode.com/posts', // replace with your endpoint
        method: 'GET',
        success: function (response) {
          console.log('Success:', response);
        },
        error: function (xhr) {
          console.error('Error:', xhr);
        }
      });
    });
  });

