$(document).ready(function() {
    $('.fav_button_on, .fav_button_del').click(function(e) {
        e.preventDefault()
        var form = $(this).closest('form')
        var url = form.attr('action')
        $.ajax({
            url: url,
            type: 'POST',
            data: form.serialize(),
            success: function(response) {
                // Обновляем только кнопку, если запрос успешен
                var button = form.find('button')
                button.replaceWith(response.button_html)
            },
            error: function(xhr, status, error) {
                // Обрабатываем ошибку, если что-то пошло не так
                console.log(error)
            }
        })
    })
  })