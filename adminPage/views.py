from wagtail.users.views.groups import (
    GroupViewSet as WagtailGroupViewSet,
    IndexView as WagtailIndexView,
)
from django.db.models import Q


class IndexView(WagtailIndexView):
    def get_queryset(self):
        return super().get_queryset().filter(~Q(name__startswith="4"))


class GroupViewSet(WagtailGroupViewSet):
    index_view_class = IndexView
