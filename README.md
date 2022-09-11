# polaroid-image-resizing
A quick script to add polaroid-esque borders to images.
Don't know if it'll work outside of Unix environments.

The new images will be suffixed with `_POLAROID` and saved as `.jpg` in the same
location as the original files.

```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt

python3 create_image.py <img_paths>
```