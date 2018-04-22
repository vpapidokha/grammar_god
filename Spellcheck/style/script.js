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
                if(data.checkedText=='True') {
                    $('#pngIncorrect').hide();
                    $('#textIncorrect').hide();
                    $('#pngCorrect').show('slow');
                    $('#textCorrect').show('slow');
                    console.log('Show image that correct');
                } else {
                    $('#pngCorrect').hide();
                    $('#textCorrect').hide();
                    $('#pngIncorrect').show('slow');
                    $('#textIncorrect').show('slow');
                    console.log('Show image that correct');
                }
                /*$('#areaForOutput').text(data.checkedText);*/
                if (data.added == 'true') {
                    $(".doSwap").load("main.html .queries");
                    var myCase="";
                    console.log(data.textId);

                    if (data.textChecked == "True" ) {
                        myCase = '<div class="modalCorrectText">' + data.inputedText + '</div>' +
                            '<div class="checkOutput"><img class="modalpngOutput" src="style\\Pictures\\happyFace.png" width="100" height="100"></div>'
                            '<div class="modaltextOutput"> Correct!</div>'
                    } else {
                        myCase = '<div class="modalIncorrectText">' + data.inputedText + '</div>' +
                            '<div class="checkOutput"><img class="modalpngOutput" src="style\\Pictures\\cryingFace.png" width="100" height="100"></div>'
                            '<div class="modaltextOutput">We detected a typo here!</div>';
                    }
                    var url="";
                    if (data.language == "English") {
                        url = "style\\Pictures\\usa.png";
                    } else {
                        url = "style\\Pictures\\usa.png";
                    }
                    console.log(myCase);
                    $('.queries').append('<button type="button" id="'+data.textId+'"class="btn btn-success tagButton" data-toggle="modal"' +
                        'data-target="#Modal'+data.textId+'" data-placement="bottom" title="'+data.checkedText+'">' +
                        data.inputedText+' </button>'+
                        '<div class="modal fade" id="Modal'+data.textId+'" tabindex="-1" role="dialog" aria-labelledby="ModalLabel" aria-hidden="true">'+
                        '<div class="modal-dialog modal-dialog-centered" role="document">'+
                        ' <div class="modal-content">'+
                        ' <div class="modal-header">'+
                        '<span>'+
                        '<div class="myModalTitle modal-title" id="exampleModalLabel">Language: '+data.language+' '+
                        '<img class="flag" src='+url+' width="35" height="35">'+'</div>'+
                        '<button type="button" class="close myClose" aria-label="Close" data-dismiss="modal">'+
                        '<span aria-hidden="true">&times;</span>'+
                        '</button>'+
                        '</span>'+
                        '</div>'+
                        '<div class="modal-body">'+
                        myCase+
                        '</div>'+
                        '<div class="modal-footer">'+
                        '<button type="button" class="btn btn-primary myCloseButton" data-dismiss="modal">Close</button>'+
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


