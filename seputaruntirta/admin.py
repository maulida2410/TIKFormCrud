from django.contrib import admin
from seputaruntirta.models import Dosen, Staf, Mahasiswa, Kelompok

# Register your models here.
admin.site.register(Dosen)
admin.site.register(Staf)
admin.site.register(Mahasiswa)
admin.site.register(Kelompok)