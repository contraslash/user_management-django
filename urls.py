from django.conf.urls import url

from . import (
    conf,
    views
)

urlpatterns = [
    url(
        r'^usuario/$',
        views.List.as_view(),
        name=conf.USER_LIST_URL_NAME
    ),
    url(
        r'^usuario/crear/$',
        views.Create.as_view(),
        name=conf.USER_CREATE_URL_NAME
    ),
    url(
        r'^usuario/(?P<pk>\d+)/$',
        views.Detail.as_view(),
        name=conf.USER_DETAIL_URL_NAME
    ),
    url(
        r'^usuario/(?P<pk>\d+)/actualizar/$',
        views.Update.as_view(),
        name=conf.USER_UPDATE_URL_NAME
    ),
    url(
        r'^usuario/(?P<pk>\d+)/reasignar-contraseña/$',
        views.ReAssignPassword.as_view(),
        name=conf.USER_RE_ASSIGN_PASSWORD_URL_NAME
    ),
    url(
        r'^usuario/(?P<pk>\d+)/eliminar/$',
        views.Delete.as_view(),
        name=conf.USER_DELETE_URL_NAME
    ),
]