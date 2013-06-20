from django.conf.urls import patterns, url
from views import ArticleListView, ArticleCreateView, ArticleDetailView,\
    ArticleUpdateView, ArticleDeleteView

urlpatterns = patterns(
    '',
    url(r'^$',
        ArticleListView.as_view(),
        name='article-list'),
    url(r'^add/$',
        ArticleCreateView.as_view(),
        name='article-create'),
    url(r'^(?P<pk>[\w\d]+)/$',
        ArticleDetailView.as_view(),
        name='article-detail'),
    url(r'^(?P<pk>[\w\d]+)/edit/$',
        ArticleUpdateView.as_view(),
        name='article-update'),
    url(r'^(?P<pk>[\w\d]+)/delete/$',
        ArticleDeleteView.as_view(),
        name='article-delete'),
)
