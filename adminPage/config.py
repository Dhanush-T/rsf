from wagtail.users.apps import WagtailUsersAppConfig


class CustomUsersAppConfig(WagtailUsersAppConfig):
    group_viewset = "adminPage.views.GroupViewSet"
