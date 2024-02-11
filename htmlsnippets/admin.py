from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from htmlsnippets.models import HTMLSnippet


class HTMLSnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'render_preview')

    def render_preview(self, obj):
        # Create the URL for the view you want to open in a new tab
        url = reverse('htmlsnippets_htmlsnippet_render', args=[obj.pk])
        # HTML structure for the preview with an arrow symbol
        return format_html(
            '<a href="{}" target="_blank" style="text-decoration:none;">'
            '<small>{}</small>'
            '&nbsp;&#x2197;</a>',  # North East arrow
            url, obj.code[:50]
        )


admin.site.register(HTMLSnippet, HTMLSnippetAdmin)
