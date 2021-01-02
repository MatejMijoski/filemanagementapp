from colorfield.fields import ColorField
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager
from taggit.models import GenericTaggedItemBase, TagBase


class UserTags(TagBase):
    color = ColorField(default='#FF0000')
    objects: models.Manager()

    class Meta:
        verbose_name = _("User Tags")
        verbose_name_plural = _("UserTags")


class AdminTags(TagBase):
    color = ColorField(default='#FF0000')

    class Meta:
        verbose_name = _("Admin Tags")
        verbose_name_plural = _("AdminTags")


class AdminTagsAll(GenericTaggedItemBase):
    tag = models.ForeignKey(
        AdminTags,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_items",
    )


class UserTagsAll(GenericTaggedItemBase):
    tag = models.ForeignKey(
        UserTags,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_items",
    )


def user_directory_path(user, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(user.user, filename)


# Model for all uploaded files
class Uploaded(models.Model):
    objects: models.Manager()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="users")
    time_uploaded = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    file = models.FileField(blank=True, upload_to=user_directory_path)
    admintags = TaggableManager(blank=True, through=AdminTagsAll, verbose_name="Admin Tags")
    usertags = TaggableManager(through=UserTagsAll, verbose_name="User Tags")
    additional_description = models.CharField(max_length=50, blank=True)
    link = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.description} {self.file}"

    class Meta:
        verbose_name = 'File'


# Model for comments
class Comment(models.Model):
    objects: models.Manager()
    file = models.ForeignKey('Uploaded', on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()

    def __str__(self):
        return self.text
