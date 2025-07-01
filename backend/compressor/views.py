import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .huffman_runner import compress, decompress

def home(request):
    return render(request, 'compressor/upload.html')

def compress_view(request):
    if request.method == 'POST' and request.FILES.get('input_file'):
        input_file = request.FILES['input_file']
        fs = FileSystemStorage()
        saved_path = fs.save(input_file.name, input_file)
        full_path = fs.path(saved_path)

        output_path = compress(full_path)
        output_filename = os.path.basename(output_path)

        # Delete original uploaded file
        if os.path.exists(full_path):
            os.remove(full_path)

        return render(request, 'compressor/download.html', {
            'file_url': fs.url(output_filename),
            'file_path': output_path  # Pass for scheduled deletion
        })

    return render(request, 'compressor/upload.html')


def decompress_view(request):
    if request.method == 'POST' and request.FILES.get('huff_file'):
        huff_file = request.FILES['huff_file']
        fs = FileSystemStorage()
        saved_path = fs.save(huff_file.name, huff_file)
        full_path = fs.path(saved_path)

        output_path = decompress(full_path)
        output_filename = os.path.basename(output_path)

        # Delete uploaded .huff file
        if os.path.exists(full_path):
            os.remove(full_path)

        return render(request, 'compressor/download.html', {
            'file_url': fs.url(output_filename),
            'file_path': output_path
        })

    return render(request, 'compressor/decompress.html')

