document.addEventListener('DOMContentLoaded', function(){

            let convertApi = ConvertApi.auth({secret: '46mk2cFKVfLbr4pd'})
let elResult = document.getElementById('link')
let elResult1 = document.getElementById('result')


// On file input change, start conversion
document.getElementById('inputGroupFile01').addEventListener('change', async e => {
    var extension = $('#inputGroupFile01').val().split('.').pop().toLowerCase()
    var fileExtension = ['jpeg', 'jpg', 'png', 'doc', 'docx', 'odt', 'pdf', 'xls', 'xlsx', 'ods', 'ppt', 'pptx'];
    if ($.inArray(extension, fileExtension) == -1) {
        return false;
    }
    document.getElementById('file-converting').innerHTML = "The file is being converted.";
    document.getElementById('submit').disabled = true;
    document.documentElement.style.cursor = 'wait'
    try {

        // Converting DOCX to PDF file
        let params = convertApi.createParams()
        params.add('file', e.currentTarget.files[0])
        let result = await convertApi.convert(extension, 'pdfa', params)

        // Showing link with the result file
        elResult.value = result.files[0].Url

    } finally {
        document.documentElement.style.cursor = 'default'
    }
    document.getElementById('submit').disabled = false;
    document.getElementById('file-converting').innerHTML = "";
})
}, false);
