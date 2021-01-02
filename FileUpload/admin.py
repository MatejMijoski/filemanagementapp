import os
import zipfile
from io import BytesIO

from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.http import HttpResponse
from django.utils.html import format_html

from FileUpload.models import Uploaded, AdminTags, UserTags, Comment, AdminTagsAll, UserTagsAll
from django.contrib.auth.models import User


def download_files(modeladmin, request, queryset):
    byte_data = BytesIO()
    zip_file = zipfile.ZipFile(byte_data, "w")

    for file in queryset:
        filename = os.path.basename(os.path.normpath(file.file.url))
        zip_file.write(path + file.file.url[5:], file.name + ".pdf")
    zip_file.close()

    response = HttpResponse(byte_data.getvalue(), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=files.zip'

    # Print list files in zip_file
    zip_file.printdir()

    return response


download_files.short_description = "Download Files"


class CommentInline(admin.TabularInline):
    model = Comment


class UserFilterList(SimpleListFilter):
    title = "user"
    parameter_name = "user"

    def lookups(self, request, model_admin):
        if not request.user.is_superuser:
            visible_users = model_admin.get_visible_users(request)
            # Sub user - return same group users
            return ((user.id, user) for user in visible_users)
        else:
            # Superuser - return all users
            return ((user.id, user) for user in User.objects.filter())

    def queryset(self, request, queryset):
        return queryset.filter(user=self.value()) if self.value() else queryset


class FileAdmin(admin.ModelAdmin):
    list_display = ('description', 'file_link', 'time_uploaded', 'file')
    # Filter option in Admin
    list_filter = [UserFilterList, 'time_uploaded', 'usertags', 'admintags']
    actions = [download_files]
    exclude = ['link']

    inlines = [CommentInline, ]

    def file_link(self, obj):
        if obj.file:
            return format_html("<a href='%s' download>Download</a>" % (obj.file.url,))
        else:
            return "No attachment"

    file_link.allow_tags = True
    file_link.short_description = 'File Download'


# Register your models here.
admin.site.register(Uploaded, FileAdmin)
admin.site.register(UserTags)
admin.site.register(AdminTags)

