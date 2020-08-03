function getInfo(id, Cover, Title, Date, Time, Resolution, FrameRate, VideoByteRate, AudioByteRate) {
    $('#info_cover').attr('src', Cover)
    $('#info_title').text(Title)
    $('#info_framerate').text(FrameRate + '帧/s')
    $('#info_resolution').text(Resolution)
    $('#info_videobyterate').text(VideoByteRate + 'Kbps')
    $('#info_audiobyterate').text(AudioByteRate + 'Kbps')
}

function changeSettings(r, s, rs) {
    $.get('/updateConfig', {
        roomid: $('#listenroomid').val() == '' ? $('#listenroomid').attr('placeholder') : $('#listenroomid').val(),
        UID: $('#listenUID').val() == '' ? $('#listenUID').attr('placeholder') : $('#listenUID').val(),
        records: r,
        status: s,
        record_status: rs,
        savepath: $('#savepath').val() == '' ? $('#savepath').attr('placeholder') : $('#savepath').val()
    }, function (res) {
        if (res['code'] == 1) {
            alert('Successful')
        }
    })
}

function RecordStart() {
    $.get('/MonitorControl', {
        'code': 1
    }, () => {
        location.reload()
    })
}

function RecordStop() {
    $.get('/MonitorControl', {
        'code': 0
    }, () => {
        location.reload()
    })
}

function RecordRestart() {
    $.get('/MonitorControl', {
        'code': -1
    }, () => {
        location.reload()
    })
}