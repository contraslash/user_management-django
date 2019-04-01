from django.utils.translation import ugettext_lazy as _
from django.urls import reverse_lazy

from base import conf

USER_PREFIX = "USER"

USER_LIST_URL_NAME = USER_PREFIX + conf.LIST_SUFFIX
USER_CREATE_URL_NAME = USER_PREFIX + conf.CREATE_SUFFIX
USER_DETAIL_URL_NAME = USER_PREFIX + conf.DETAIL_SUFFIX
USER_UPDATE_URL_NAME = USER_PREFIX + conf.UPDATE_SUFFIX
USER_RE_ASSIGN_PASSWORD_URL_NAME = USER_PREFIX + "_re_assign_password"
USER_DELETE_URL_NAME = USER_PREFIX + conf.DELETE_SUFFIX


MENUS = {
        "name": _("User Management"),
        "fa_icon": "fa-user",
        "sub_menus": [
            {
                "name": _("Users"),
                "url_reversed": reverse_lazy(USER_LIST_URL_NAME)
            },
        ]
    }
