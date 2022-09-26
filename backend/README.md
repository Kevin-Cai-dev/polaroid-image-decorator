# polaroid-image-decorator-backend

Backend for the polaroid image generator web app. This is based on `FastAPI` and
uses the python `Pillow` library for image processing.

## Setup

Environment variables need to be set (local `.env` file) if running locally to
specify allowed origins:

```bash
PRODUCTION_URL={production_url} # optional
LOCAL_URL=http://localhost:{FE_PORT}
```

## Development

To run it locally:

```bash
pip install requirements.txt
uvicorn main:app
```
