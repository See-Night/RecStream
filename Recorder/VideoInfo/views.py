from django.http.response import JsonResponse
from .models import VideoInfo
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def addVideoInfo(request):
	try:
		newVideo = VideoInfo(
            FileName=request.POST['FileName'],
            Title=request.POST['Title'],
            Time=request.POST['Time'],
            Date=request.POST['Date'],
            LiveURL=request.POST['LiveURL'],
            Resolution=request.POST['Resolution'],
            FrameRate=request.POST['FrameRate'],
            VideoByteRate=request.POST['VideoByteRate'],
            AudioByteRate=request.POST['AudioByteRate']
        )
		newVideo.save()
		return JsonResponse({
			'status': True,
			'msg': 'OK'
		})
	except Exception as e:
		return JsonResponse({
			'status': False,
			'msg': e
		})


def delVideoInfo(request):
    pass
