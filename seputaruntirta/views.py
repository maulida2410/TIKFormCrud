from django.shortcuts import render
from seputaruntirta.forms import FormDosen, FormStaf, FormMahasiswa

# Create your views here.
def untirtajwr(request):
    return render(request, 'index.html')

def tambah_Dosen(request):
    if request.POST:
        form = FormDosen(request.POST)
        form.save()
        form = FormDosen()
        pesan = "Data berhasil disimpan"

        konteks = {
            'form': form,
            'pesan': pesan,
        }
        return render(request, 'tambahdosen.html', konteks)

    else:
        form = FormDosen()
        konteks = {
            'form': form,
        }

    return render(request, 'tambahdosen.html', konteks)

def tambah_Staf(request):
    if request.POST:
        form = FormStaf(request.POST)
        form.save()
        form = FormStaf()
        pesan = "Data berhasil disimpan"

        konteks = {
            'form': form,
            'pesan': pesan,
        }
        return render(request, 'tambahstaf.html', konteks)

    else:
        form = FormStaf()
        konteks = {
            'form': form,
        }

    return render(request, 'tambahstaf.html', konteks)
    

def tambah_Mahasiswa(request):
     if request.POST:
        form = FormMahasiswa(request.POST)
        form.save()
        form = FormMahasiswa()
        pesan = "Data berhasil disimpan"

        konteks = {
            'form': form,
            'pesan': pesan,
        }
        return render(request, 'tambahmhs.html', konteks)

     else:
        form = FormMahasiswa()
        konteks = {
            'form': form,
        }

        return render(request, 'tambahmhs.html', konteks)
    