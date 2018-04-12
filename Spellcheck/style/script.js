$(document).ready(function(){
    $('[data-toggle="modal"]').tooltip();
    var form = $('#checkText');

    function checkText(inputedText, language){
        var data = {};
        data.inputedText = inputedText;
        data.language=language;
        var csrf_token = $('#checkText [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        var url = form.attr("action");
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log("OK");

                if (data.checkedText){
                    $('#areaForOutput').text(data.checkedText);
                }

            },
            error: function(){
                console.log("error")
            }
        })

    }

    form.on('submit', function(e){
        e.preventDefault();
        var inputedText = $("#areaForInput").val();
        var language=$("#FormControlSelect").val();

        checkText(inputedText, language)

    });


});


