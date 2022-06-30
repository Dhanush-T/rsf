from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import Permission, Group
from wagtail.models import GroupPagePermission

from researchers.models import ResearcherPage, ResearchesPage
from wagtail.images.models import Image
import imaplib


class IMAPAuthentication(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwars):
        username = username.strip()
        username = username.split("@")[0]
        # host = "students.nitt.edu"
        try:
            pass
            # M = imaplib.IMAP4_SSL(host=host, port="993")
            # M.login(username, password)
            # M.logout()
        except:
            return None
        UserModel = get_user_model()
        user = None
        group = None
        page = None
        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            print("User does not exist")
            try:
                if username[0] == '4' and len(username)==9:
                    print("User is a student")
                    user = UserModel.objects.create_user(username=username, password=None)

                    user.user_permissions.add(Permission.objects.get(codename="access_admin"))

                    group = Group.objects.create(name=username)

                    group.user_set.add(user)

                    user.groups.add(group)

                    page = ResearcherPage(
                        title=username,
                        owner=user,
                        bio="Yet to be Filled",
                        department="Architecture",
                        contact_name=username,
                        email=username+"@nitt.edu",
                        phone_number="",
                        intrests="Yet to be filled"
                    )

                    image = None
                    try:
                        image = Image.objects.get(title="noprofile")
                    except Image.DoesNotExist:
                        image = None
                    
                    page.image = image


                    researches_page = ResearchesPage.objects.get(slug="researcher").add_child(instance=page)
                    researches_page.save()
                    page.save()
                    
                    for permission_type in ["add", "edit", "publish"]:
                        GroupPagePermission.objects.create(
                            group=group, page=page, permission_type=permission_type
                        )
                    
                    user.save()

            except Exception as e:
                print(e)
                if user:
                    user.delete()
                if group:
                    group.delete()
                if page:
                    page.delete()
                return None
        
        return user

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
