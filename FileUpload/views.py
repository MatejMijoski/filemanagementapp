from django.core.mail import send_mail
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse, FileResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import FileUploadForm, EditProfileForm, CommentForm, ChangeTagsForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView
from .models import Uploaded, UserTags
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.files import File
from os.path import basename
from urllib.request import urlretrieve, urlcleanup
from urllib.parse import urlsplit, urlparse

admin_email = ""


# Download the file from the URL and
# replace it in the file field
def download_to_file_field(url, field):
    try:
        tempname, _ = urlretrieve(url)
        field.save(basename(urlsplit(url).path), File(open(tempname, 'rb')))
    finally:
        urlcleanup()


# Home Page View
@login_required
def index(request):
    user = request.user
    files = Uploaded.objects.filter(user=user)
    userTags = UserTags.objects.all()
    form = FileUploadForm

    # Paginate through the files
    paginator = Paginator(files, 6)
    page = request.GET.get('page', 1)

    try:
        files_paginated = paginator.page(page)
    except PageNotAnInteger:
        files_paginated = paginator.page(1)
    except EmptyPage:
        files_paginated = paginator.page(paginator.num_pages)

    # Search for the files
    url_parameter = request.GET.get("q")

    if url_parameter:
        filesSearch = Uploaded.objects.filter(user=user, name__icontains=url_parameter)
    else:
        filesSearch = Uploaded.objects.filter(user=user)
    context = {'form': form, 'page': page, 'files': files_paginated, 'userTags': userTags}

    # Refresh the files on search or delete
    if request.is_ajax():
        html = render_to_string(
            template_name="files_searched.html",
            context={'userTags': userTags, "filesSearch": filesSearch}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            user = request.user
            download_to_file_field(url=form.instance.link, field=form.instance.file)
            form.save()
            subject = "A new file has been uploaded!"
            message = "User: " + user.username + "\nFile name: " + str(
                form.cleaned_data['file']) + "\nFile Description:" + str(form.cleaned_data['description'])
            send_mail(subject, message, user.email, [admin_email, ])
            return HttpResponseRedirect(reverse('index'))
    else:
        form = FileUploadForm
    return render(request, 'index.html', context)


# Log In View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(index)
    return render(request, 'login.html')


# Log Out View
def logout_view(request):
    logout(request)
    return redirect('login.html')


# View for each tag
@login_required()
def tagged(request, slug):
    tag = get_object_or_404(UserTags, slug=slug)
    files = Uploaded.objects.filter(user=request.user, usertags=tag)
    userTags = UserTags.objects.all()
    context = {
        'tag': tag,
        'files': files,
        'userTags': userTags,
    }
    return render(request, 'tagged.html', context)


# View Profile
@login_required()
def view_profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'accounts/profile.html', context)


# Edit Profile
@login_required()
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)


# Delete File for button
class FileDelete(DeleteView):
    model = Uploaded
    success_url = reverse_lazy('index')
    template_name = 'FileManagement/delete_file.html'


# Add new description
@csrf_exempt
def add_comment_to_file(request, pk):
    file = get_object_or_404(Uploaded, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.file = file
            comment.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = CommentForm()
    return render(request, 'index.html', {'form': form})


# Change tags
@csrf_exempt
def change_tags(request, pk):
    file = get_object_or_404(Uploaded, pk=pk)
    if request.method == "POST":
        form = ChangeTagsForm(request.POST, instance=file)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = CommentForm()
    return render(request, 'index.html', {'form': form})


def auth_file_check(request):
    url = request.build_absolute_uri()
    if not '//' in url:
        url = 'http://' + url
    o = urlparse(url)
    user = o.path.split("/")
    print(o.path[5:])
    if str(request.user) == user[2].split("_", 1)[1] or request.user.is_superuser:
        # Change link to path where files will be stored
        return FileResponse(open(path + o.path[5:], 'rb'), content_type='application/pdf')
    else:
        return HttpResponseRedirect(reverse(index))
