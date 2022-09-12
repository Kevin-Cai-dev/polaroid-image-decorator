# polaroid-image-resizing

A quick script to add polaroid-esque borders to images.
Don't know if it'll work outside of Unix environments.

The new images will be suffixed with `_POLAROID` and saved as `.jpg` in the same
location as the original files in a square aspect ratio.

```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt

python3 create_image.py <img_paths>
```

## Example

Original Image
![Original image](examples/DSCF2874.JPG)

Resulting Image (with `_POLAROID.jpg` extension)
![Polaroid effect applied](examples/DSCF2874_POLAROID.jpg)

Resulting Image (with `-n` flag)
![Polaroid effect applied](examples/DSCF2874_POLAROID_no_border.jpg)
