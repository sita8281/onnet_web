function showSimpleModal(label, text) {
    $('#span-modal-label').text(label);
    $('#text-modal-info').html(text);
    $('#simple-modal-block').fadeToggle(400);
    $('html').css({
        overflow: 'hidden',
        height: '100%'
    });
}


// открыть окно с текстом полученым с сервера
function showAjaxModal(label, url, post_param) {

    $('#span-modal-label').text('Ошибка');
    $('#text-modal-info').html('Не удалось загрузить данные');

    $.ajax({
        type: "post",
        url: url,
        data: {iid: post_param},
        dataType: "html",
        success: function (response) {
            $('#span-modal-label').text(label);
            $('#text-modal-info').html(response);
            $('#simple-modal-block').fadeToggle(400);
            $('html').css({
                overflow: 'hidden',
                height: '100%'
            });
        },
        error: function (err) {
            $('#simple-modal-block').fadeToggle(400);
            $('html').css({
                overflow: 'hidden',
                height: '100%'
            });
        }
    });
    
}