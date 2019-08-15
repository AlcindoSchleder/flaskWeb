$(document).ready(function() {
    $('#formZipCode').submit(function(e) {
        let zipCode = $('#zip_code').val(); 
        let url = $('#formZipCode').attr('action') + '/' + zipCode; 
        $('#msgData').html('Mensagem: CEP digitado: ' + zipCode + ' para a ação: ' + url);
        $.ajax({
            type: "GET",
            url: url,
            // data: '',
            success: function(data) {
                console.log(data);  // display the returned data in the console.
                if (data.status == 200) {
                    $('#msgData').html('Mensagem: cep ' + data.data + '/Localidade aprovado!');
                } else {
                    $('#msgData').html('Mensagem:' + data.errors[0]);
                }
            },
            error: function(e) {
                console.log(data);
                $('#msgData').html('Mensagem:' + data.errors[0]);
            }
        });
        e.preventDefault(); // block the traditional submission of the form.
    });
    // Inject our CSRF token into our AJAX request.
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", "{{ form.csrf_token._value() }}")
            }
        }
    })
});
