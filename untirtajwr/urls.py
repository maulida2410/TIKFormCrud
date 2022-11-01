from django.contrib import admin
from django.urls import path
from seputaruntirta.views import untirtajwr, tambah_Dosen, tambah_Staf, tambah_Mahasiswa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('seputaruntirta/', untirtajwr),
    path('tambahdosen/', tambah_Dosen),
    path('tambahstaf/', tambah_Staf),
    path('tambahmhs/', tambah_Mahasiswa)
]  