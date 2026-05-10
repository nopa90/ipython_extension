# ipyforge-kernel

A FastAPI server + Pi extension for controlling an IPython kernel via HTTP.

## Setup

```bash
cd /Users/johnjanecek/Projects/pi-dev-tools/ipython_extension
uv sync
```

## Start a kernel (for remote access)

Create the IPython profile first (one time):

```bash
unv run ipython profile create pi-dev 
```

Start the kernel, binding to all interfaces so it can accept remote connections:

```bash
uv run ipython kernel --profile=pi-dev --ip=0.0.0.0 -f /tmp/remote-kernel.json
```

This writes a connection file to `/tmp/remote-kernel.json`. Copy this file to the machine
running the FastAPI server and update `cfg.json` to point at it.

## Connect with jupyter console

On the **same machine** as the kernel:

```bash
uv run jupyter console --existing /tmp/remote-kernel.json
```

If connecting from a **different machine**, edit the `ip` field in the copied `kernel.json`
to the kernel machine's IP address first. Then:

```bash
uv run jupyter console --existing /path/to/copied/kernel.json
```

## Start the FastAPI server

```bash
cd /Users/johnjanecek/Projects/pi-dev-tools/ipython_extension
uv run python server/main.py
```

## Install the Pi extension

Copy `extension/index.ts` to one of these locations for auto-discovery:

| Location | Scope |
|----------|-------|
| `~/.pi/agent/extensions/` | Global (all projects) |
| `~/your-project/.pi/extensions/` | Per-project |

Run `/reload` in Pi to pick it up.
