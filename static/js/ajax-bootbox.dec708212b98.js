function ajax(id){
    var id =id;
    bootbox.confirm("Are you sure you want to delete this file?",
        function (result) {
            if (result) {
                $.ajax({
                    method: "DELETE",
                    url: "delete/" + id,
                    beforeSend: function(xhr) {
                        xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
                        },
                        success: function(){
                        $('#replaceable-content').load(' #replaceable-content', function(){$(this).children().unwrap()})
                        $('.tags').load(' .tags', function(){$(this).children().unwrap()})
                         }
                      });
                    }
                });

    function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
        return cookieValue;
    }
}
