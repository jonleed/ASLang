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

## Standalone OpenCV camera demo

The camera demo is intentionally separate from the lessons page. Run the website in one terminal, then start this service in a second terminal:

```bash
cd CV
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-demo.txt
python hello.py
```

Open [http://localhost:5000/video](http://localhost:5000/video) in its own browser tab. It streams the default webcam as MJPEG and may prompt you to give the terminal camera permission. Stop the service with `Ctrl+C`.

On macOS, AirPlay Receiver may already use port 5000. Leave it running and use a different port instead:

```bash
PORT=5050 python hello.py
```

Then open [http://localhost:5050/video](http://localhost:5050/video).

### Historical classifier source

`CV/webcam.py` and `CV/Model/` are the separate hackathon-era hand-classification experiment. They remain unchanged and are not connected to the lessons page or the standalone camera demo. Its original dependency list omits `Flask` and `Flask-SocketIO`, and TensorFlow 2.14 requires Python 3.10 or 3.11; it is preserved for reference rather than treated as a supported launch path.

## Checks

```bash
npm run lint
npm run build
```

`npm run build` succeeds without Firebase values. The build currently reports dependency warnings for optional native modules and outdated browser-compatibility data; these do not prevent the application from running.
