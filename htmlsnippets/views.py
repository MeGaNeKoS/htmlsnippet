from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from htmlsnippets.models import HTMLSnippet


def render_snippet(request, pk):
    snippet = get_object_or_404(HTMLSnippet, pk=pk)

    if request.META.get('HTTP_ACCEPT') == 'application/json':
        json_data = {
            'title': snippet.title,
            'tag': snippet.tag,
            'content': snippet.code
        }
        return JsonResponse(json_data)

    return render(request, 'htmlsnippets/render.html', {'context': snippet})
