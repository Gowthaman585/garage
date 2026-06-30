# Docker Compose: Running Multiple Containers Together 🐋🔗

Up until now I was running containers one at a time with `docker run`. Today I learned **Docker Compose** — a way to define and spin up multiple containers together using a single YAML file. One command, everything starts. That felt like a proper upgrade.

---

## The `compose.yaml` File

```yaml
services:
  web_server:
    image: nginx:alpine
    ports:
      - "8080:80"
    container_name: compose_web

  database_server:
    image: redis:alpine
    container_name: compose_db
```

Two services defined here:

- **`compose_web`** — an Nginx web server (Alpine-based, lightweight). Port `80` inside the container is mapped to port `8080` on my machine so I can access it from the browser.
- **`compose_db`** — a Redis in-memory database. No port mapping needed here since it's just internal.

Both use Alpine-based images to keep things small and fast. ⚡

---

## Running It

Just one command to bring everything up in detached mode (runs in the background):

```bash
docker compose up -d
```

Docker pulled both images and started downloading them in parallel:

![Docker pulling nginx and redis images](compose-load.png)

A few seconds later, everything was up:

![Both containers started successfully](compose-completed.png)

Docker automatically created a shared network (`docker-compose_default`) so the two containers can talk to each other without any extra config. That's one of the nicest things about Compose — networking is handled for you.

---

## Proof It Works 🟢

Opened `http://localhost:8080` in the browser — Nginx was live:

![Nginx welcome page on localhost:8080](nginx.png)

---

## What I Learned

- **`compose.yaml`** is the single source of truth for your whole multi-container setup — services, ports, names, all in one place.
- **`docker compose up -d`** pulls images, creates the network, and starts all containers in one shot. No more running multiple `docker run` commands.
- Docker Compose automatically creates a **shared network** for all services in the file — so `compose_web` and `compose_db` can reach each other by their service names.
- The `-d` flag runs everything in the background (detached), so your terminal isn't blocked.
- To tear everything down cleanly: `docker compose down`.

---

## Quick Reference

| Command | What it does |
|---|---|
| `docker compose up -d` | Start all services in the background |
| `docker compose down` | Stop and remove all containers + network |
| `docker compose ps` | Check status of running services |
| `docker compose logs` | View logs from all services |

---

*Part of my ongoing Docker learning notes on CachyOS / Arch Linux.*
