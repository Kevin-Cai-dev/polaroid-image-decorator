# polaroid-image-decorator-cli

A quick script to add polaroid-esque borders to images.
Don't know if it'll work outside of Unix environments.

The new images will be suffixed with `_POLAROID` and saved as `.jpg` in the same
location as the original files.

It defaults to a square aspect ratio and `md`
thickness borders (3% on each end of the longer image dimension)

```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt

python3 create_image.py [...flags] <...image_paths>
```

## Examples

Original Image

<img src="examples/DSCF2874.JPG" alt="" width=600>

With default settings

<img src="examples/DSCF2874_POLAROID_normal.jpg" alt="" width=600>

With `--nb` flag (no border)

<img src="examples/DSCF2874_POLAROID_no_border.jpg" alt="" width=600>

With `--xl` flag (xl thickness border)

<img src="examples/DSCF2874_POLAROID_xl_border.jpg" alt="" width=600>

with `--5-4` flag (5:4 aspect ratio)

<img src="examples/DSCF2874_POLAROID_5_4_ratio.jpg" alt="" width=600>
