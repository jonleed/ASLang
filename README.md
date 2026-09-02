# ASLang

An early hackathon prototype for learning American Sign Language. The project has a Next.js frontend, optional Firebase authentication/progress tracking, and an experimental local Python camera/classification service.

## Run the frontend

Use Node.js 18 or newer, then run:

```bash
npm ci
npm run dev
```

Open [http://localhost:3000](http://localhost:3000). The home page and lesson navigation work without any credentials.

### Restore sign-in and saved progress

The original Firebase keys were intentionally not committed. Copy `.env.example` to `.env.local` and fill in the Firebase web-app settings for the `aslang-b56b7` project (or a replacement Firebase project):

```bash
cp .env.example .env.local
```

The project needs Google Authentication enabled and a Realtime Database at the configured URL. Until those variables are supplied, pressing **Sign In** reports that Firebase needs configuration; the rest of the frontend remains usable.

## Historical camera lesson

The first lesson includes an unfinished webcam experiment in `CV/`. It expects a local webcam and listens on port 5000. This component has not been restored or validated; the frontend expects Socket.IO `video_frame` events, while the backend exposes an HTTP `/video` stream and only logs Socket.IO connections. It may therefore start without displaying a stream.

The original dependency list also omits `Flask` and `Flask-SocketIO`, even though `webcam.py` imports them. They must be installed manually to experiment with the historical service. Use Python 3.10 or 3.11 (TensorFlow 2.14 does not support newer Python releases), then from a second terminal:

```bash
cd CV
python3.10 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install Flask Flask-SocketIO
python webcam.py
```

The model files are tracked in `CV/Model`; the service needs permission to use your webcam. No changes have been made to make this experiment functional.

## Checks

```bash
npm run lint
npm run build
```

`npm run build` succeeds without Firebase values. The build currently reports dependency warnings for optional native modules and outdated browser-compatibility data; these do not prevent the application from running.
