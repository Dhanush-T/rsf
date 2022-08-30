import datetime

from wagtail.core.models import Page
from researchers.models import SeminarAndViva


class SeminarPage(Page):
    max_count = 1
    parent_page_types = ["home.HomePage"]

    template = "seminar/seminar_page.html"

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        seminar_and_viva_voice = SeminarAndViva.objects.all()

        context["seminar_and_viva_voice"] = seminar_and_viva_voice

        if seminar_and_viva_voice:

            seminar_after_today = SeminarAndViva.objects.filter(
                date__gte=datetime.date.today(), type="Seminar"
            ).order_by("-date")

            if request.GET.get("department", None):
                department = request.GET.get("department", None)
                seminar_after_today = seminar_after_today.filter(
                    department=department
                )

            context["seminar_after_today"] = seminar_after_today

            viva_voice_after_today = SeminarAndViva.objects.filter(
                date__gte=datetime.date.today(), type="Viva Voice"
            ).order_by("-date")

            if request.GET.get("department", None):
                department = request.GET.get("department", None)
                viva_voice_after_today = viva_voice_after_today.filter(
                    department=department
                )

            context["viva_voice_after_today"] = viva_voice_after_today

        return context

