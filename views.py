from django.contrib.auth import models, forms
from django.core.urlresolvers import reverse_lazy

from base import views

from applications.authentication import (
    mixins
)

from . import (
    conf,
    forms as user_management_forms
)


class List(
    mixins.SuperAdminRequiredMixin,
    views.BaseListView
):
    queryset = models.User.objects.all()

    def __init__(self):
        super(List, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)

        for user in context[self.context_object_name]:
            user.url_name = conf.USER_DETAIL_URL_NAME

        return context


class Create(
    mixins.SuperAdminRequiredMixin,
    views.BaseCreateView
):
    model = models.User
    form_class = user_management_forms.CustomUserForm

    def get_success_url(self):
        return reverse_lazy(conf.USER_DETAIL_URL_NAME, kwargs={
            'pk': self.object.id
        })


class Detail(
    mixins.SuperAdminRequiredMixin,
    views.BaseDetailView
):
    template_name = "user_management/detail.html"
    model = models.User

    def __init__(self):
        super(Detail, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)

        context['reassign_password_reversed_url'] = self.reassign_password_reversed_url()

        return context

    def reassign_password_reversed_url(self):
        return reverse_lazy(
            conf.USER_RE_ASSIGN_PASSWORD_URL_NAME,
            kwargs={
                "pk": self.get_object().id
            }
        )


class Update(
    mixins.SuperAdminRequiredMixin,
    views.BaseUpdateView
):
    """
    Update a Groups from a User
    """
    model = models.User
    form_class = user_management_forms.UserGroups

    def __init__(self):
        super(Update, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.USER_DETAIL_URL_NAME, kwargs={
            'pk': self.object.id
        })


class ReAssignPassword(
    mixins.SuperAdminRequiredMixin,
    views.BaseUpdateView
):
    model = models.User
    form_class = forms.SetPasswordForm

    def __init__(self):
        super(ReAssignPassword, self).__init__()

    def get_form(self, form_class=None):
        return self.form_class(self.get_object(), data=self.request.POST or None)

    def form_valid(self, form):
        print("Form Valid")
        return super(ReAssignPassword, self).form_valid(form)

    def form_invalid(self, form):
        print("Form INVALID")
        print(form.errors)
        return super(ReAssignPassword, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy(conf.USER_DETAIL_URL_NAME, kwargs={
            'pk': self.object.id
        })


class Delete(
    mixins.SuperAdminRequiredMixin,
    views.BaseDeleteView
):
    """
    Delete a  User
    """
    model = models.User

    def __init__(self):
        super(Delete, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.USER_LIST_URL_NAME)
