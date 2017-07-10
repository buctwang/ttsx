# -*- coding:utf-8 -*-
from haystack.generic_views import SearchView


class MySearchView(SearchView):
    """My custom search view."""

    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        context['title'] = '搜索结果'
        context['search_style'] = '1'
        return context