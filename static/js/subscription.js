$(document).ready(function () {
    $('#subscribe').submit(function (event) {
        event.preventDefault()
        form = $("#subscribe")

        $.ajax({
            'url': '/ajax/subscription/',
            'type': 'POST',
            'data': form.serialize(),
            'dataType': 'json',
            'success': function (data) {
                alert(data['success'])
            },
        })
        $('#id_name').val('')
        $("#id_email").val('')
    })

})
