function add_description(file_id){
    var display = $('.additional-description-' + file_id).css('display')
    if(display == "none"){
        $(".additional-description-" + file_id).fadeIn(300);
    }
    else{
        $('.additional-description-' + file_id).fadeOut(300);
    }
}
