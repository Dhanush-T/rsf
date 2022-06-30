from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import Permission, Group
from wagtail.models import GroupPagePermission, GroupCollectionPermission, Collection

from researchers.models import ResearcherPage, ResearchesPage
from wagtail.images.models import Image
import imaplib

departments = [
    "Architecture",
    "Chemical Engineering",
    "Civil Engineering",
    "Chemistry",
    "Computer Applications",
    "Computer Science and Engineering",
    "Electrical and Electronics Engineering",
    "Electronics and Communication Engineering",
    "Humanities and Social Sciences",
    "Instrumentation and Control Engineering",
    "Mechanical Engineering",
    "Metallurgical and Materials Engineering",
    "Physics",
    "Production Engineering",
    "Management Studies",
    "Mathematics",
    "Energy and Environment",
    "CECASE",
]


class IMAPAuthentication(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwars):
        username = username.strip()
        username = username.split("@")[0]
        host = "students.nitt.edu"
        try:
            M = imaplib.IMAP4_SSL(host=host, port="993")
            M.login(username, password)
            M.logout()
        except:
            return None
        UserModel = get_user_model()
        user = None
        group = None
        page = None
        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            try:
                if username[0] == "4" and len(username) == 9:
                    user = UserModel.objects.create_user(
                        username=username, password=None
                    )

                    user.user_permissions.add(
                        Permission.objects.get(codename="access_admin")
                    )

                    group = Group.objects.create(name=username)

                    group.user_set.add(user)

                    user.groups.add(group)

                    page = ResearcherPage(
                        title=username,
                        owner=user,
                        bio="Yet to be Filled",
                        department="Architecture",
                        name=username,
                        email=username + "@nitt.edu",
                        phone_number="",
                        intrests="Yet to be filled",
                    )

                    image = None
                    try:
                        image = Image.objects.get(title="noprofile")
                    except Image.DoesNotExist:
                        image = None

                    page.image = image

                    researches_page = (
                        ResearchesPage.objects.filter().first().add_child(instance=page)
                    )
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


class DevAuthentication(ModelBackend):
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
            try:
                if username[0] == "4" and len(username) == 9:

                    department = departments[int(username[1:3]) - 1]

                    user = UserModel.objects.create_user(
                        username=username, password=None
                    )

                    user.user_permissions.add(
                        Permission.objects.get(codename="access_admin")
                    )

                    group = Group.objects.create(name=username)

                    group.user_set.add(user)

                    user.groups.add(group)

                    page = ResearcherPage(
                        title=username,
                        owner=user,
                        bio="Yet to be Filled",
                        department=department,
                        name=username,
                        email=username + "@nitt.edu",
                        phone_number="",
                        intrests="Yet to be filled",
                    )

                    image = None
                    try:
                        image = Image.objects.get(title="noprofile")
                    except Image.DoesNotExist:
                        image = None

                    page.image = image

                    researches_page = (
                        ResearchesPage.objects.filter().first().add_child(instance=page)
                    )
                    researches_page.save()
                    page.save()

                    for permission_type in ["add", "edit", "publish"]:
                        GroupPagePermission.objects.create(
                            group=group, page=page, permission_type=permission_type
                        )

                    for permission in ["add_image", "change_image", "view_image"]:
                        GroupCollectionPermission.objects.create(
                            group=group,
                            collection=Collection.objects.filter(name="Root").first(),
                            permission=Permission.objects.get(codename=permission),
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
