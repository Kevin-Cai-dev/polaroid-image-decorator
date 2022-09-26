# polaroid-image-decorator

A program to add polaroid-esque white borders to images, created since I
couldn't find a good, existing solution without any hoops to jump through.

This repo consists of two parts:

**Web app**: An interactive website which allows you to upload an image, generate
a polaroid-esque version, and download it

- [`frontend`](/frontend/): contains the frontend of the web app, a simple single-page
  application.

  `Next.js, Tailwind, DaisyUI, Typescript`

- [`backend`](/backend/): contains the image processing logic of the web app, a simple REST
  endpoint which takes in image files and returns a polaroid-esque version back.

  `Python, FastAPI, Pillow`

**CLI**: The [original version](/cli/), a CLI program which allows image(s) to be
converted and saved in the same location as the original

## FAQ

> **Is it tested?**

:)

> **The deployed frontend keeps failing, why is this happening?**

Either some of the options specified cannot be used, or the backend is down
since Heroku is making changes to their free plans :(
