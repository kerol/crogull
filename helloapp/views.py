# coding: utf-8
from crogull.response import Response, JsonResponse


async def index(request):
    # return Response('hello', status=200)
    return JsonResponse({'foo': 'bar'})
