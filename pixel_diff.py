from PIL import Image as PILImage
import os

print('\n Generating PNG images ... ', end='', flush=True)
max_filename_len = 0
filenames_list = []
export_filenames_list = []
for file in os.listdir('images'):
    filename, extension = os.path.splitext(file)
    if extension != '.svg':
        continue
    basic_filename = filename.replace('_original', '').replace('_pure_svg', '')
    if basic_filename not in filenames_list:
        filenames_list.append(basic_filename)
        filename_len = len(basic_filename)
        if filename_len > max_filename_len:
            max_filename_len = filename_len
    export_filenames_list.append(file)
# Inkscape is required.
# If I use --export-dpi=72, it exports 461x346 instead of 460x345 as exported by Matplotlib's savefig('png')
os.system(f'cd images && inkscape --export-type=png --export-width=460 {' '.join(export_filenames_list)} > NUL 2>&1')
print('Done\n')

for i in range(len(filenames_list)):
    filename1 = filenames_list[i] + "_original"
    filename2 = filenames_list[i] + "_pure_svg"
    img1 = PILImage.open(f'images/{filename1}.png')
    w, h = img1.size
    img1 = img1.load()
    img2 = PILImage.open(f'images/{filename2}.png').load()
    n = 0
    for r in range(w):
        for c in range(h):
            if img1[r, c] != img2[r, c]:
                n += 1
    pretty_filename = (filenames_list[i] + '_*.png').ljust(max_filename_len+6)
    if n:
        print(f' {pretty_filename} ::  Mismatch for {str(n).rjust(4)} pixels. ({round(n * 100.0 / (640.0 * 480.0), 1)}%)')
    else:
        print(f' {pretty_filename} ::  Both are same.')
    del img2
    del img1
