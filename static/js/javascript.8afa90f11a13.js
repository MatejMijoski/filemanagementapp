function add_description(file_id){
    var display = $('.additional-description-' + file_id).css('display')
    if(display == "none"){
        $(".additional-description-" + file_id).fadeIn(300);
    }
    else{
        $('.additional-description-' + file_id).fadeOut(300);
    }
}

      $(document).ready(function() {
            var counter = 0;

                 $('.js-example-basic-multiple').select2();

                 $('.form').submit(function() {
                    var selectVals = $('#select-tags').val();
                    $('#hidden-usertags').val(selectVals);
                });

                 $('#select-tags').on('select2:open', function (e) {
                    setTimeout(function() {
                        $('.select2-results__option').each(function(){
                            var id = $(this).html();
                            var color = $('[value=' + id + ']').attr('data-id');
                            $(this).css('background-color', color);
                        });
                    }, 50);
                 });

                 $('#select-tags').on('change', function (e) {
                    $('#select2-select-tags-container > li').each(function(){
                        var title = $(this).attr('title');
                        var color = $('[value=' + title + ']').attr('data-id');
                        $(this).css('background-color', color);
                    });
                 });


                 $('#inputGroupFile01').on('change',function(){

                 var fileExtension = ['jpeg', 'jpg', 'png', 'doc', 'docx', 'odt', 'pdf', 'xls', 'xlsx', 'ods', 'ppt', 'pptx', 'txt'];
                 if ($.inArray($(this).val().split('.').pop().toLowerCase(), fileExtension) == -1) {
                    alert("The following files are allowed : "+fileExtension.join(', ') + ".");
                }else{
                //get the file name
                var fileName = $(this).val().split('\\').pop();
                //replace the "Choose a file" label
                $(this).next('.custom-file-label').html(fileName);
                    }
                });

                $('#orgForm').submit(function(){
                console.log($('#name').val().length);
                if($('#name').val().length > 30){
                    $('.error-name').css("display", "block");
                    $('.error-name').html("The name field should be less than 30 characters.");
                    return false;
                }else if($('#name').val() === ""){
                    $('.error-name').css("display", "block");
                    $('.error-name').html("The name field is required.");
                    return false;
                }else{
                    $('.error-name').css("display", "none");
                    $('.error-name').html("");
                }
                if($('#description').val().length > 200){
                    $('.error-description').css("display", "block");
                    $('.error-description').html("The description field should be less than 200 characters.");
                    return false;
                }else if($('#description').val() === ""){
                    $('.error-description').css("display", "block");
                    $('.error-description').html("The description field is required.");
                    return false;
                }else{
                    $('.error-description').css("display", "none");
                    $('.error-description').html("");
                }
                if($('#inputGroupFile01').val() === ""){
                    $('.error-file').css("display", "block");
                    $('.error-file').html("The file field is required");
                    return false;
                }else{
                    $('.error-file').css("display", "none");
                    $('.error-file').html("");
                }

                $('#select2-select-tags-container > li').each(function(){
                       counter+=1;
                    });

                if(counter === 0 ){
                    $('.error-tags').css("display", "block");
                    $('.error-tags').html("The tags field is required");
                    return false;
                }else{
                    $('.error-tags').css("display", "none");
                    $('.error-tags').html("");
                }
                counter=0;

                });



                var id = null;
    var element = null;
    var dataid = null;
        $('.change-tags-btn').click(function(){
            id = $(this).attr('onclick').replace(/[^0-9]/gi, '');
            setTimeout(function(){
                $('.change-tags-select').select2()
            },1000);

             $('#change-' + id).on('change', function (e) {
                  setTimeout(function(){
                   $('#select2-change-' + id + '-container > li').each(function(){
                   var title = $(this).attr('title');
                   var color = $('[value=' + title + ']').attr('data-id');
                   $('#select2-change-' + id + '-container').find('[title="' + title + '"]').css('background-color', color);
                 });
                 },100);
            });
        });

        $('.change-tags-select').on('select2:open', function (e) {
                    setTimeout(function() {
                       $('.select2-results__option').each(function(){
                       var id = $(this).html();
                       var color = $('[value=' + id + ']').attr('data-id');
                       $(this).css('background-color', color);
                 });
             }, 50);
        });



        $('#change-' + id).on('change', function (e) {
        console.log('1');
              $('form.change-' + id).find('#select2-change-' + id + '-container > li').each(function(){
                   var title = $(this).attr('title');
                           console.log('[title="' + title + '"]');

                   var color = $('[value=' + title + ']').attr('data-id');
                   console.log($('#select2-change-' + id + '-container').find('[title="' + title + '"]').attr('data-select2-id'));
                   $('#select2-change-' + id + '-container').find('[title="' + title + '"]').css('background-color', color);
           });
        });

        $('.change-tags-form').submit(function() {
           var selectVals = $('.change-tags-select').val();
           $('.change-hidden-usertags').val(selectVals);
        });

            });



function change_tags(file_id){
    var display = $('.change-tags-' + file_id).css('display')
    setTimeout(function(){$('.change-tags-select').select2()}, 500);

    if(display == "none"){
        $(".change-tags-" + file_id).fadeIn(300);
    }
    else{
        $('.change-tags-' + file_id).fadeOut(300);
    }
}
