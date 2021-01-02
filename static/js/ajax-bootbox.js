function ajax(id){
            const files_div = $('#replaceable-content')
            const endpoint = ''
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
                            $.getJSON(endpoint)
                                    .done(response => {
                                    // fade out the files_div, then:
                                    files_div.fadeTo('slow', 0).promise().then(() => {
                                    // replace the HTML contents
                                    files_div.html(response['html_from_view'])
                                    // fade-in the div with new contents
                                    files_div.fadeTo('slow', 1)
                                })
                            })
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