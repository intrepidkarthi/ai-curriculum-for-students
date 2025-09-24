---
marp: true
paginate: true
class: lead
---

# Cloud & DevOps (AI‑assisted CI/CD)

Containerize a tiny API + run tests in CI — with local LLM help

---

## Today’s Plan (60m)

- Why containers + CI/CD (5m)
- Draft with LLM: API, Dockerfile, CI plan (10m)
- Build & run: local Docker + tests (25m)
- Wire CI: push → green checks (15m)
- Wrap: notes, pitfalls, next steps (5m)

---

## Why containers + CI/CD

- Immutable runtime: works on my machine → works anywhere
- Reproducible builds: Dockerfile = source of truth
- CI: every PR gets tested automatically
- Fast feedback: catch regressions early

---

## The tiny API we’ll build

- Stack: FastAPI + Uvicorn
- Endpoints
  - GET /health → {"status": "ok"}
  - GET /sum?a=1&b=2 → {"sum": 3}
- Tests: `pytest` using `fastapi.testclient`

---

## Ollama Quick Check (local-only)

- VS Code Task: "Local AI: Check Ollama" (runs a short generation)
- CLI:
```bash
ollama list
curl -s http://127.0.0.1:11434/api/tags | head -c 200
```
- If slow: use a smaller model (e.g., phi3:mini). See LOCAL_AI_SETUP.md

---

## Model Presets (speed vs quality)

- `phi3:mini` — fastest; great for unit tests and small diffs
- `llama3.2:3b-instruct` — balanced; better reasoning while still light
- `mistral:7b-instruct` — optional; stronger laptops only
- Tip: switch models in Continue settings mid-session

---

## Pull/Run models (Ollama)

```bash
ollama pull phi3:mini
ollama pull llama3.2
# optional if your laptop is strong:
ollama pull mistral
ollama pull codellama
# run a reasoning model (optional)
ollama run deepseek-r1
```

---

## Live with Continue + Ollama

- Prompt 1: API scaffold + tests
- Prompt 2: Dockerfile + .dockerignore
- Prompt 3: GitHub Actions CI (cache pip, run pytest)
- Iterate: paste → run → minimal diffs → green

---

## Copy-ready prompts — API & Tests

- API scaffold (FastAPI):
```text
Create a FastAPI app with GET /health -> {"status":"ok"} and GET /sum?a&b -> {"sum": a+b}.
Provide app/main.py only, no comments. Use Python 3.11 typing.
```
- Unit tests (pytest + TestClient):
```text
Write pytest tests for the /health and /sum endpoints, including missing parameter failure.
Return a single file tests/test_app.py that imports app.main:app via TestClient.
```

---

## Copy-ready prompts — Dockerfile & .dockerignore

- Dockerfile:
```text
Draft a minimal Dockerfile for a FastAPI app using python:3.11-slim.
Install from requirements.txt, copy app to /app/app, and run uvicorn app.main:app on 0.0.0.0:8000.
```
- .dockerignore:
```text
Generate a .dockerignore for a Python project: __pycache__/, *.pyc, .venv/, .git/, .mypy_cache/, .pytest_cache/, node_modules/.
```

---

## Copy-ready prompts — GitHub Actions CI

- CI yaml:
```text
Write a GitHub Actions workflow to run pytest on push/PR to main/master using Python 3.11.
Use actions/checkout@v4 and actions/setup-python@v5, cache pip, install -r requirements.txt, run pytest -q.
```
- Minimal diff fix:
```text
Given this failing CI log and the current Dockerfile/CI yaml, propose a minimal diff patch to fix it.
Only output the unified diff needed.
```

---

## Dockerfile — Anatomy

- Base: python:3.11‑slim
- Workdir, copy requirements, install, copy app
- Expose 8000 (optional); CMD uvicorn

---

## Build & Run (local)

- Build: `docker build -f sessions/session03_cloud_devops/Dockerfile -t s3-api:latest .`
- Run: `docker run --rm -p 8000:8000 s3-api:latest`
- Test: `curl http://localhost:8000/health`

---

## CI pipeline (GitHub Actions)

- Uses Python 3.11, installs requirements, runs pytest
- Optional: add lint (ruff) or type check (mypy)
- Optional: build image in CI (later session)

---

## Prompt patterns (DevOps)

- Draft: “Generate a minimal Dockerfile for …; prefer slim image; non‑root if possible.”
- Fix: “Image too large; propose a smaller base or multi‑stage build.”
- CI: “Add steps to cache pip; run pytest with -q; fail on non‑zero.”

---

## The Evolution of Deployments

- **Act 1: The Wild West (Manual)**
  - `FTP`/`SCP` files directly to a server. Hope you don't forget a file!
- **Act 2: The Age of Servers (Automation Scripts)**
  - VMs (Virtual Machines) + shell scripts. Better, but servers still need patching and care.
- **Act 3: The Age of Containers (Reproducibility)**
  - Docker/Containers. Package your app and its environment together. Works everywhere!
- **Act 4: The Cloud Native Era (Orchestration)**
  - Kubernetes/Serverless. Manage fleets of containers automatically. Focus on code, not servers.

---

## DevOps is a Culture, Not Just Tools

It's a mindset of **shared ownership** to deliver value faster and more reliably.

- **Before**: Devs write code, Ops handles deployment. "It works on my machine!"
- **After**: Devs and Ops work together. Everyone is responsible for the entire lifecycle, from code to production.

**Key ideas**: Automate everything, measure everything, and improve continuously.

---

## Cloud Service Models: An Analogy

How much do you want to manage yourself?

- **On-Premise**: You build and manage everything. (Making pizza from scratch at home)
- **IaaS (Infrastructure as a Service)**: Rent servers, storage, networking. (Buying a pre-made pizza base and adding your own toppings)
  - *Examples: AWS EC2, Google Compute Engine*
- **PaaS (Platform as a Service)**: Rent a platform to run your app. (Ordering a pizza for delivery)
  - *Examples: Heroku, AWS Elastic Beanstalk*
- **SaaS (Software as a Service)**: Rent a finished product. (Dining at a pizza restaurant)
  - *Examples: Gmail, Salesforce*

---

## Beyond CI: Advanced Deployment Strategies

Once your tests pass (CI), how do you release to users safely (CD)?

- **Blue-Green Deployment**: Run two identical production environments ("Blue" and "Green"). Release to the inactive one, test it, then switch traffic over instantly. Zero downtime.

- **Canary Release**: Release the new version to a small subset of users (the "canaries"). Monitor for errors. If all is well, gradually roll it out to everyone.

- **Feature Flags**: Deploy new code to production but keep it hidden behind a "flag". Turn it on for specific users (or internally) to test it before a full release.

---

## A Day in the Life of a DevOps Engineer

It's a mix of proactive improvement, reactive problem-solving, and collaboration.

- **Morning:** Check monitoring dashboards, review overnight alerts.
- **Mid-day:** Consult with a dev team on infrastructure for a new feature.
- **Afternoon:** Write a script to automate a manual process (Infrastructure as Code).
- **Ongoing:** Improve CI/CD pipeline speed and reliability.
- **"Firefighting":** Respond to a production outage or performance issue.

---

## The Cost of the Cloud: Don't Get a Surprise Bill!

Cloud is a utility model, like electricity. You pay for what you use.

- **What you pay for:**
  - **Compute:** Per-second billing for servers/containers.
  - **Storage:** Per-GB cost for files and databases.
  - **Data Transfer:** Especially data going *out* of the cloud ("egress fees").
- **How to manage it:**
  - Shut down dev/test environments when not in use.
  - Set budget alerts.
  - **Tag** resources to track costs by project or team.

---

## Infrastructure as Code (IaC): A Blueprint for Your Cloud

The Old Way: Clicking in a web console (slow, error-prone, not repeatable).
The New Way (IaC): Define infrastructure (servers, databases, networks) in code.

- **Benefits:** Reproducible, version-controlled (git), and collaborative (Pull Requests).
- **Popular Tools:** Terraform, AWS CloudFormation, Pulumi, Bicep.

*You've already done this! Your Dockerfile and GitHub Actions YAML are forms of IaC.*

---

## Monitoring & Observability: Is It Working?

After deployment, how do you know if your app is healthy?

- **Logs:** Detailed, timestamped records of events. ("User X failed to log in at 10:05 AM").
- **Metrics:** Aggregated numerical data over time. ("CPU usage is at 90%").
- **Traces:** A view of a single request's journey through all your services. ("The login request was slow because the database query took 3 seconds").

*Together, these are the "Three Pillars of Observability."*

---

## A Typical Cloud Architecture (Web Service)

<img src="https://i.imgur.com/LJQ5k2c.png" style="background: white;" alt="A diagram showing a typical cloud architecture. A user request goes through a Load Balancer, which distributes traffic to multiple Web Servers (VMs or Containers). These servers communicate with a managed Database. This setup is shown within a Virtual Private Cloud (VPC) for security." />

---

## The DevOps Toolchain

Different tools are used at each stage of the software lifecycle.

- **Plan:** Jira, Trello
- **Code:** VS Code, Git, GitHub
- **Build:** Docker, Gradle, Maven
- **Test:** Pytest, JUnit, Selenium
- **Release:** GitHub Actions, Jenkins
- **Deploy:** Terraform, Ansible, Kubernetes
- **Operate & Monitor:** Prometheus, Grafana, Datadog

*No one uses everything! Teams pick the tools that best fit their needs.*

---

## Career Paths & Certifications

- **Roles:**
  - **Cloud Engineer:** Builds and manages cloud infrastructure.
  - **DevOps Engineer:** Focuses on the CI/CD pipeline and automation.
  - **Site Reliability Engineer (SRE):** Focuses on the reliability, performance, and scalability of production systems.
  - **Platform Engineer:** Builds internal tools and platforms for developers.
- **Getting Started Certifications:**
  - AWS Certified Cloud Practitioner
  - Microsoft Certified: Azure Fundamentals
  - HashiCorp Certified: Terraform Associate

---

## Practical App Example 1: Campus Event & Club Finder

**The Goal:** An app to help students discover campus events and clubs that match their interests.

- **Architecture:**
  1. **Data Ingestion:** A scheduled script scrapes official university calendars and student group pages.
  2. **AI Tagging:** The scraped event descriptions are sent to an LLM (like Claude or GPT) to be tagged with keywords (e.g., 'sports', 'tech', 'music', 'free food').
  3. **API:** A simple API allows users to search for events by date, keyword, or club name.
  4. **Frontend:** A mobile-friendly web app displays events in a clean, searchable interface.

- **Cloud/DevOps Concepts in Action:**
  - **Scheduled Tasks (Cron):** For automated data scraping.
  - **AI for Data Enrichment:** Using an LLM to add valuable metadata to raw data.
  - **Search & Discovery:** A core product pattern for many applications.

---

## Practical App Example 2: Class Registration Notifier

**The Goal:** Get a text message the instant a spot opens up in a full class.

- **Architecture:**
  1. **The Scraper:** A serverless function (AWS Lambda) runs every minute, checking the university's registration portal for a specific class section.
  2. **State Management:** A simple database (like DynamoDB) stores which user is watching which class.
  3. **Notification:** If a spot opens, the function uses a service like **Twilio** to send an SMS alert to the user.
  4. **Frontend:** A simple UI where students can input the class number and their phone number.

- **Cloud/DevOps Concepts in Action:**
  - **High-Frequency Scheduled Automation:** Running a task much more frequently than a daily cron job.
  - **Serverless at Scale:** Can support thousands of students watching different classes with minimal cost.
  - **Third-Party API Integration:** Connecting to a service like Twilio.

---

## Practical App Example 3: Automated Meme Generator Bot

**The Goal:** A bot for social media that takes an image and text, and creates a meme.

- **Architecture:**
  1. **The Trigger:** A user uploads an image to a specific cloud storage bucket (e.g., Amazon S3).
  2. **The Event:** The upload event triggers a serverless function (AWS Lambda).
  3. **Image Processing:** The function uses a library like `Pillow` in Python to draw the top and bottom text onto the image.
  4. **The Result:** The final meme image is saved to a different 'output' bucket, ready to be shared.

- **Cloud/DevOps Concepts in Action:**
  - **Event-Driven Architecture:** The entire workflow is stateless and triggered by an event.
  - **Image Manipulation:** A common use case for serverless functions.
  - **Cost-Effective:** You only pay for the few milliseconds of compute time it takes to generate one meme.

---

## Practical App Example 4: YouTube Video Summarizer

**The Goal:** Paste a YouTube URL and get an AI-generated summary and comment analysis.

- **Architecture:**
  1. **Frontend:** A simple web app where the user pastes the YouTube URL.
  2. **Backend API:** A serverless function uses the YouTube Data API to fetch the video's transcript and comments.
  3. **Asynchronous AI Jobs:** The function submits two tasks to a queue (like AWS SQS):
     - Task 1: Send transcript to an LLM for summarization.
     - Task 2: Send comments to an LLM for sentiment analysis.
  4. **Display Results:** Once the tasks are complete, the results are saved, and the frontend can display them.

- **Cloud/DevOps Concepts in Action:**
  - **Asynchronous Workflows & Task Queues:** The right way to handle long-running tasks.
  - **Chaining AI Services:** Combining multiple LLM calls to create a sophisticated result.
  - **API Integration:** Working with a major third-party API (YouTube).

---

## Practical App Example 5: Collaborative Spotify Playlist

**The Goal:** A web app where friends can log in and add songs to a shared playlist.

- **Architecture:**
  1. **Frontend:** A React or Svelte app that handles the user interface.
  2. **Authentication:** Users log in via **Spotify's OAuth 2.0** flow. The app never sees their password, it just gets a temporary token to act on their behalf.
  3. **Backend API:** A small API (on **Heroku**, **Fly.io**, or **PaaS**) that uses the user's token to interact with the Spotify API (e.g., search for tracks, add tracks to a playlist).
  4. **Real-time Updates:** Use WebSockets to instantly show when someone else adds a new song to the playlist.

- **Cloud/DevOps Concepts in Action:**
  - **OAuth 2.0:** The standard for secure, third-party authentication.
  - **API Proxying:** The backend acts as a secure proxy between the user and the Spotify API.
  - **PaaS (Platform as a Service):** Heroku or Fly.io make it incredibly easy to deploy a web application from a Git repository.

---

## Practical App Example 6: Multiplayer Game Backend

**The Goal:** A backend to manage the state for a simple real-time multiplayer game.

- **Architecture:**
  1. **Game Client:** (e.g., Unity, Godot, or browser-based) connects to the backend via **WebSockets** for low-latency communication.
  2. **Game Servers:** A fleet of **Docker containers** running a stateful application (e.g., in Node.js or C#). Managed by a container orchestrator like **Kubernetes** (e.g., **Amazon EKS**).
  3. **State Management:** A fast in-memory database like **Redis** is used to store temporary game state (player locations, scores).
  4. **Player Accounts:** A persistent database like **PostgreSQL** stores user accounts and long-term progress.

- **Cloud/DevOps Concepts in Action:**
  - **Stateful Applications:** A more complex challenge than stateless APIs.
  - **Container Orchestration:** Kubernetes automatically manages scaling and healing of the game server fleet.
  - **Low-Latency Networking:** Critical for a good user experience in real-time applications.

---

## Practical App Example 7: "Link in Bio" Page (like Linktree)

**The Goal:** A fast, simple, and cheap-to-host personal landing page.

- **Architecture:**
  1. **Frontend:** A static website (HTML, CSS, JS) built with a generator like Hugo or Astro. Hosted on **Netlify**, **Vercel**, or **GitHub Pages**.
  2. **Analytics:** To track link clicks, the frontend sends a request to a serverless function (**Netlify Functions**, **AWS Lambda**) which records the event.
  3. **Data Store:** The click data is stored in a simple, low-cost NoSQL database or even a Google Sheet via its API.

- **Cloud/DevOps Concepts in Action:**
  - **Jamstack:** The frontend is pre-built and served from a CDN, making it incredibly fast and secure.
  - **Git-based Workflow:** `git push` to the main branch automatically triggers a new deployment on Netlify/Vercel.
  - **Minimal Cost:** Hosting for the static site is often free, and serverless function calls are extremely cheap.

---

## Practical App Example 8: Real-time Polling App

**The Goal:** A web app where users can vote and see results update live.

- **Architecture:**
  1. **Frontend:** A modern JavaScript app (React, Vue) hosted on a static hosting service like **Netlify** or **AWS S3 + CloudFront** for global speed.
  2. **Backend API:** A containerized API on **AWS Fargate** or **Google Kubernetes Engine** handles incoming votes.
  3. **Database:** A scalable NoSQL database like **Amazon DynamoDB** or **Firestore** stores the poll results.
  4. **Real-time:** A WebSocket API or a service like **Pusher** pushes live updates to all connected users.

- **Cloud/DevOps Concepts in Action:**
  - **Microservices:** Frontend and backend are decoupled and can be scaled independently.
  - **Managed Services:** Using a managed database (DynamoDB) reduces operational overhead.
  - **CI/CD:** Separate pipelines for frontend and backend allow for independent updates.

---

## Practical App Example 9: AI Flashcard Generator

**The Goal:** Upload lecture notes (PDF) and get a set of flashcards to study from.

- **Architecture:**
  1. **Frontend:** A simple web page to upload a PDF file directly to **Amazon S3**.
  2. **Event Trigger:** The S3 upload triggers a Lambda function.
  3. **AI Processing:** The function sends the PDF to an AI service like **Anthropic Claude** or **OpenAI's GPT-4** with a prompt: "Generate question/answer flashcards from this document."
  4. **Display:** The results are saved to a database, and the user is redirected to a page where they can view and study the generated flashcards.

- **Cloud/DevOps Concepts in Action:**
  - **Third-Party API Integration:** Calling an external AI service.
  - **Processing Unstructured Data:** Handling file uploads and parsing them.
  - **Asynchronous Workflow:** The user can close the page while the AI works; the results will be ready when they return.

---

## Capstone Example: "Project UniVerse"

**The Goal:** A platform for students across colleges to connect based on interests and collaborate on projects, research, and hobbies.

- **Key Features:**
  - **Smart Profiles:** Users list skills (Python, UI/UX), interests (Game Dev, AI), and current classes. An AI model suggests potential collaborators.
  - **Project Hub:** A feed where students can post ideas ("Need a React dev for a hackathon app") and recruit teammates.
  - **Collaboration Spaces:** For each project, an integrated chat, a shared document editor, and a simple task board.

- **Cloud/DevOps Concepts in Action:** This is a full-fledged application that uses everything we've discussed.
  - **Microservices Architecture:** The app is broken down into smaller, independent services (User Service, Project Service, Chat Service, etc.), each in its own Docker container.
  - **Container Orchestration:** A **Kubernetes** cluster manages the hundreds of containers needed to run the app at scale.
  - **Multiple Databases:** Using the right tool for the job: **PostgreSQL** for user/project data, **Redis** for caching, and **Elasticsearch** for powerful search across profiles and projects.
  - **Real-time Communication:** A **WebSocket** service handles live chat and notifications.
  - **Advanced CI/CD:** Dozens of separate CI/CD pipelines, one for each microservice, allowing teams to deploy updates independently and safely using **Canary Releases**.
  - **Infrastructure as Code (IaC):** The entire cloud infrastructure (Kubernetes cluster, databases, networking) is defined in **Terraform**.

---

## Building for Free: The Student Developer Stack

You don't need a credit card to build real-world applications. Leverage free tiers and student packs!

**Your #1 Starting Point: The GitHub Student Developer Pack**
- A massive bundle of free developer tools. Get it with your student email.
- Includes: Free domain names (e.g., `.me`), cloud credits for AWS/Azure/GCP, and access to dozens of professional tools.

**Hosting Your Application (Backend & Full-Stack):**
- **PaaS (Platform as a Service):** Easiest way to start.
  - **Heroku / Render:** Free tier for small apps (often "sleeps" when inactive). Perfect for portfolio projects.
  - **Fly.io:** Generous free tier for containers and small databases.
- **Serverless (The most cost-effective way):**
  - **Vercel / Netlify:** Free hosting for static frontends and a large free tier for serverless functions.
  - **AWS/GCP/Azure Free Tiers:** Offer millions of serverless function calls per month for free, forever.

**Databases & Storage:**
- **PostgreSQL:** **Supabase** or **Railway** offer generous free-tier databases with integrated APIs.
- **NoSQL:** **MongoDB Atlas** and **Firebase** have perpetual free tiers for smaller projects.
- **Object Storage:** **Cloudflare R2** or the **AWS S3** free tier are great for storing user uploads.

**A Free Stack for "Project UniVerse":**
- **Frontend:** React app hosted on **Vercel**.
- **Backend:** Serverless functions on **Vercel** or **AWS Lambda**.
- **Database:** Free-tier **Supabase** PostgreSQL database.
- **Authentication:** **Clerk** or **Auth0**'s free tier for user logins.
- **Code & CI/CD:** Hosted on **GitHub** (free private repos & actions).

---

## Common pitfalls

- Wrong module path in CMD: `uvicorn app.main:app` vs actual path
- Forgetting to open 0.0.0.0 in containers
- Missing requirements in CI
- Large images: prefer slim + no cache

---

## Resources & Links

- Code: `sessions/session03_cloud_devops/`
- Tasks: VS Code → Run Task → “Session 3: Docker Build API”, “Session 3: Docker Run API”
- CI: `.github/workflows/ci.yml`
- Local models: use Continue + Ollama for Dockerfile/CI drafts

---

## Wrap

- We containerized the app and got tests running in CI
- Next: add lint/mypy, multi‑stage builds, or deploy to a free host
