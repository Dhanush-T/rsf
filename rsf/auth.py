from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import Permission, Group
from wagtail.models import GroupPagePermission, GroupCollectionPermission, Collection

from researchers.models import ResearcherPage, ResearchesPage
from wagtail.images.models import Image
import imaplib
import requests
import os

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


class RequestAuthentication(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwars):
        username = username.strip()
        username = username.split("@")[0]
        host = "students.nitt.edu"
        try:
            if username == os.environ.get("ADMIN_USERNAME"):
                return get_user_model().objects.get(username=username)
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Language': 'en-GB,en;q=0.9,fr;q=0.8,ta-IN;q=0.7,ta;q=0.6,en-US;q=0.5,hi;q=0.4',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Origin': 'https://' + host,
                'Referer': 'https://students.nitt.edu/horde/login.php',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
                'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
            }

            data = {
                'app': '',
                'login_post': '1',
                'url': '',
                'anchor_string': '',
                'horde_user': username,
                'horde_pass': password,
                'horde_select_view': 'auto',
            }

            response = requests.post('https://students.nitt.edu/horde/login.php', headers=headers, data=data)

            if response.url == 'https://students.nitt.edu/horde/login.php':
                raise Exception("Invalid credentials")
            else:
                pass

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
                        interests="Yet to be filled",
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

                    root_collection = Collection.get_first_root_node()
                    root_collection.add_child(name=username)

                    for permission in ["add_image", "change_image", "view_image"]:
                        GroupCollectionPermission.objects.create(
                            group=group,
                            collection=Collection.objects.filter(name=username).first(),
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

class IMAPAuthentication(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwars):
        username = username.strip()
        username = username.split("@")[0]
        host = "students.nitt.edu"
        try:
            if username == os.environ.get("ADMIN_USERNAME"):
                return get_user_model().objects.get(username=username)
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
                        interests="Yet to be filled",
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

                    root_collection = Collection.get_first_root_node()
                    root_collection.add_child(name=username)

                    for permission in ["add_image", "change_image", "view_image"]:
                        GroupCollectionPermission.objects.create(
                            group=group,
                            collection=Collection.objects.filter(name=username).first(),
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

                    root_collection = Collection.get_first_root_node()
                    root_collection.add_child(name=username)

                    for permission in ["add_image", "change_image", "view_image"]:
                        GroupCollectionPermission.objects.create(
                            group=group,
                            collection=Collection.objects.filter(name=username).first(),
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
