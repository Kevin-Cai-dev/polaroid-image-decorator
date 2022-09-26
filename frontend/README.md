# polaroid-image-decorator-frontend

Frontend for the polaroid image generator web app. This is a Next.js app used to
render a simple SPA with a download option. Downloaded images are prefixed with `POLAROID`.

## Setup

Environment variables need to be set (`.env.local` file) if running locally to
specify backend URL:

```bash
NEXT_PUBLIC_API_ENDPOINT=http://localhost:{BE_PORT}
```

## Development

To run it locally:

```bash
yarn # OR npm install
yarn dev # OR npm run dev
```
