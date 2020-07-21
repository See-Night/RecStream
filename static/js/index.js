window.onload = function () {
    StatusSelfAdapting($(window).width())
    record_calendarSelfAdapting($(window).width())
    RecordSearchSelfAdapting($(window).width())

    $(window).resize(() => {
        StatusSelfAdapting($(window).width())
        record_calendarSelfAdapting($(window).width())
        RecordSearchSelfAdapting($(window).width())
    })
}

function toInfoPage(id) {
    window.open(window.location.protocol + "//" + window.location.host + '/Info?id=' + id)
}

function record_calendarSelfAdapting(width) {
    if (width < 900) {
        $('#rec_cal').attr({
            'class': 'row mt-3 mb-3 d-flex flex-column'
        })
        $('#calendar').attr({
            'class': 'col p-4 d-flex flex-column bg-light shadow-sm mb-2'
        })
        $('#recordlist').attr({
            'class': 'col d-flex flex-column align-items-between p-0 mt-2'
        })
        $('#recordlist').children().attr({
            'class': 'col bg-light p-3 d-flex flex-column'
        })
    }
    else {
        $('#rec_cal').attr({
            'class': 'row mt-3 mb-3 d-flex justify-content-between'
        })
        $('#calendar').attr({
            'class': 'col-4 p-4 d-flex flex-column bg-light shadow-sm'
        })
        $('#recordlist').attr({
            'class': 'col-8 d-flex flex-column align-items-end p-0'
        })
        $('#recordlist').children().attr({
            'class': 'col-11 bg-light p-3 d-flex flex-column'
        })
    }
}

function StatusSelfAdapting(width) {
    if (width < 900) {
        $('#statusinfo').attr({
            'class': 'd-flex justify-content-center flex-column'
        })
        for (var i = 0; i < $('#statusinfo').children().length; i++) {
            $($('#statusinfo').children()[i]).attr({
                'class': 'col p-4 mt-3 mb-3 d-flex flex-column justify-content-center border-dark border'
            })
        }
    }
    else {
        $('#statusinfo').attr({
            'class': 'd-flex justify-content-center'
        })
        for (var i = 0; i < $('#statusinfo').children().length; i++) {
            $($('#statusinfo').children()[i]).attr({
                'class': 'col-3 p-4 m-3 d-flex flex-column justify-content-center border-dark border'
            })
        }
    }
}

function RecordSearchSelfAdapting(width) {
    if (width < 900) {
        $('#RecordSearch').attr({
            'class': 'd-flex col'
        })
    }
    else {
        $('#RecordSearch').attr({
            'class': 'd-flex col-6'
        })
    }
}
