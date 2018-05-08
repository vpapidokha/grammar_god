$(document).ready(function(){
    $('[data-toggle="modal"]').tooltip();
    $('[data-toggle="icon"]').tooltip();
    $(function () {
                $('#datetimepicker1').datetimepicker();
            });

    var form = $('#checkText');
    var formDelete=$('#deleteForm');

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
                console.log(data.mycurrentUser);
                var date = new Date(data.dateTimeCreated)

                if(data.checkedText=='True') {
                    $('#pngIncorrect').hide();
                    $('#textIncorrect').hide();
                    $('#ourSuggest').hide();
                    $('#pngCorrect').show('slow');

                    $('#textCorrect').show('slow');
                    console.log('Show image that correct');
                } else {
                    $('#pngCorrect').hide();
                    $('#textCorrect').hide();
                    $('#pngIncorrect').show('slow');
                    $('#textIncorrect').show('slow');
                    console.log('Show image that Incorrect');
                    $('#ourSuggest').show('slow');

                    $('#ourSuggest').empty().append('<button type="button" id="suggest" class="btn btn-warning btn-lg" data-toggle="modal"' +
                        'data-target="#ModalSuggest" data-placement="top" title="Click to open list of suggestions">Maybe, you meant this</button>'+
                        '<div class="modal fade" id="ModalSuggest" tabindex="-1" role="dialog" aria-labelledby="ModalLabel" aria-hidden="true">'+
                        '<div class="modal-dialog modal-dialog-centered" role="document">'+
                        ' <div class="modal-content">'+
                        ' <div class="modal-header">'+
                        '<span>'+
                        '<div class="suggestTitleInModal modal-title" id="exampleModalLabel">We assumed that you meant one of this '+
                        '<img class="flag" src="style\\Pictures\\thinking.png" width="40" height="40">'+'</div>'+
                        '<button type="button" class="close myClose" aria-label="Close" data-dismiss="modal">'+
                        '<span aria-hidden="true">&times;</span>'+
                        '</button>'+
                        '</span>'+
                        '</div>'+
                        '<div class="suggestModalList modal-body">'+
                        data.suggest+
                        '</div>'+
                        '</div>'+
                        '</div>'+
                        '</div>');
                    console.log(data.suggest);


                }
                /*$('#areaForOutput').text(data.checkedText);*/
                if (data.added == 'true') {
                    $(".doSwap").load("main.html .queries");
                    var myCase="";
                    var mySupposeBlock="";
                    console.log(data.textId);

                    if (data.textChecked == "True" ) {
                        myCase = '<div class="modalCorrectText">' + data.inputedText + '</div>' +
                            '<div class="checkOutput"><img class="modalpngOutput" src="style\\Pictures\\happyFace.png" width="100" height="100"></div>'+
                            '<div class="modaltextOutput"> Correct!</div>'
                    } else {
                        myCase = '<div class="modalIncorrectText">' + data.inputedText + '</div>' +
                            '<div class="checkOutput"><img class="modalpngOutput" src="style\\Pictures\\cryingFace.png" width="100" height="100"></div>'+
                            '<div class="modaltextOutput">We detected a typo here!</div>';
                        mySupposeBlock='<div class="suggestInModal">'+
                            '<div class="suggestTitleInModal">We assumed that you meant one of this <img class="" src="style\\Pictures\\thinking.png" '+
                            'width="35" height="35"></div><div class="suggestModalList">'+ data.suggest +'</div></div>'
                    }
                    var url="";
                    if (data.language == "English") {
                        url = "style\\Pictures\\usa.png";
                    } else {
                        url = "style\\Pictures\\usa.png";
                    }
                    console.log(myCase);

                    $('.queries').append('<button type="button" id="'+data.textId+'"class="btn btn-success tagButton" data-toggle="modal"' +
                        'data-target="#Modal'+data.textId+'" data-placement="bottom" title="'+data.inputedText+'">' +
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
                        mySupposeBlock+

                        '<div class="suggestInModal">'+
                        '<span>'+
                        '<div class="userDetail">'+
                        '<img class="" src="style\\Pictures\\user.png" width="28" height="28" data-toggle="icon" title="username"> '+data.mycurrentUser+
                        '<p><img class="timeicon" src="style\\Pictures\\time.png" width="28" height="28" data-toggle="icon" title="Time when was created"> '+data.dateCreated+
                        '</div>'+
                        '<div class="wrapButton">'+
                        '<button type="button" class="btn btn-primary myCloseButton" data-dismiss="modal">Close</button>'+
                        '</div>'+
                        '</span>'+
                        '</div>'+

                        '</div>'+
                        '</div>'+
                        '</div>'


                    );
                    console.log("fine");
                    $('[data-toggle="modal"]').tooltip();
                    $('[data-toggle="icon"]').tooltip();
                    /*
                    setTimeout(function() {  $('#loadProcces').hide(); }, 100000);
                    $('#loadProcces').hide();
                    $('#submit_btn').show();
                    $('#areaForInput').show();*/

                }
                else {/*
                    setTimeout(function() {  $('#loadProcces').hide(); }, 5000);
                    $('#loadProcces').hide();
                    $('#submit_btn').show();
                    $('#areaForInput').show();*/
                }

            },
            error: function(){
                console.log("error")
            }
        })



    }

    formDelete.on('submit', function(e){
        e.preventDefault();
        var idOfText =$("deleteId").val();
        console.log(idOfText);
        delQuery(idOfText);
    });

    function delQuery(idOfText){
        var data = {};
        data.idText = idOfText;
        console.log(data.idText);
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
        /*
        $('#areaForInput').hide();
        $('#submit_btn').hide();
        $('#loadProcces').show();
        */

        checkText(inputedText, language)

    });

    $("#pngCorrect").mouseover(function(){
        console.log('Enter');
        var audio = $("#sound-correct")[0];
        audio.play();
    });

    $("#pngIncorrect").mouseover(function(){
        console.log('Enter');
        var audio = $("#sound-incorrect")[0];
        audio.play();
    });

    $("#helloPng").mouseover(function(){
        console.log('Enter');
        var audio = $("#sound-hello")[0];
        audio.play();
    });




});


