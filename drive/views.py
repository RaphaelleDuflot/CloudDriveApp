from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UploadFileForm
from .models import Document
from django.db import models

# Create your views here.

def check_disk_space(user, file_size):
    total_size = Document.objects.filter(user=user).aggregate(models.Sum('size'))['size__sum'] or 0
    if total_size + file_size > 100 * 1024 * 1024:  # 100 Mo
        return False
    return True




def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            user_file = form.save(commit=False)
            #user_file.user = request.user
            user_file.user = None
            file_size = user_file.file.size

            # Vérifier la limite d’espace disque
            if file_size > 40 * 1024 * 1024:  # 40 Mo
                messages.error(request, "La taille de fichier maximale autorisée est de 40 Mo.")
            #elif not check_disk_space(request.user, file_size):
            elif not check_disk_space(None, file_size):
                messages.error(request, "Espace disque dépassé !")
            else:
                user_file.save()  # Enregistrer le fichier
                return redirect('file_list')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})