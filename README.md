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

## OpenCV camera demos

Both camera demos are intentionally separate from the lessons page. Run the website in one terminal, then start either service in a second terminal.

### Annotated sign classifier

This is the hand-box and sign-letter demo. It loads the saved model from `CV/Model/`, then draws the detected hand box and its predicted ASL letter onto the video stream.

```bash
cd CV
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements-classifier.txt
PORT=5051 python webcam.py
```

Open [http://localhost:5051/video](http://localhost:5051/video) in its own browser tab. Give the terminal camera permission if macOS asks. The server is not connected to the lessons page.

### Raw camera stream

This lighter demo serves the webcam without recognition:

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

### Original dependency snapshot

`requirements.txt` is retained as the full hackathon-era dependency snapshot. The dedicated `requirements-classifier.txt` contains the classifier runtime dependencies needed on current macOS/Python 3.11.

## Checks

```bash
npm run lint
npm run build
```

`npm run build` succeeds without Firebase values. The build currently reports dependency warnings for optional native modules and outdated browser-compatibility data; these do not prevent the application from running.
