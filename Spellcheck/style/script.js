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
                console.log(data.checkedText);
                console.log(typeof data.checkedText);
                $('#areaForOutput').text(data.checkedText);
                if (data.added == 'true') {
                    $(".doSwap").load("main.html .queries");

                    console.log(data.textId);
                    $('.queries').append('<button type="button" id="'+data.textId+'"class="btn btn-success tagButton" data-toggle="modal"' +
                        'data-target="#Modal'+data.textId+'" data-placement="bottom" title="'+data.checkedText+'">' +
                        data.inputedText+' </button>'+
                        '<div class="modal fade" id="Modal'+data.textId+'" tabindex="-1" role="dialog" aria-labelledby="ModalLabel" aria-hidden="true">'+
                        '<div class="modal-dialog modal-dialog-centered" role="document">'+
                           ' <div class="modal-content">'+
                               ' <div class="modal-header">'+
                       '<span>'+
                            '<h4 class="modal-title" id="exampleModalLabel">Language: '+data.language+'</h4>'+
                            '<button type="button" class="close" aria-label="Close" data-dismiss="modal">'+
                                       '<span aria-hidden="true">&times;</span>'+
                           '</button>'+
                        '</span>'+
                                '</div>'+
                                '<div class="modal-body">'+
                                    'User name: '+data.userName+'<p>'+
                                    'Inputed text: '+data.inputedText+
                                '</div>'+
                               '<div class="modal-footer">'+
                                    '<button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>'+
                                '</div>'+
                           '</div>'+
                        '</div>'+
                    '</div>'


                    );
                    console.log("fine");
                    $('[data-toggle="modal"]').tooltip();

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


