---
marp: true
paginate: true
class: lead
---

# Full-Stack Development & Modern Frameworks (AI‑assisted)

Build a minimal API + micro front‑end with local LLM support (Ollama + Continue)

---

## Today’s Plan (60m)

- 0–10: MERN/MEAN overview; microservices basics
- 10–40: Notes API + micro front‑end (fetch/POST); prompt for validation rules
- 40–55: Add pagination or input validation
- 55–60: Homework brief

---

## Learning Objectives

- Explain API‑first thinking; basic validation and pagination
- Build a minimal notes API and call it from a micro front‑end
- Use a local LLM (Ollama + Continue) to draft spec, handlers, tests, and docs

---

## Full‑Stack Overview (quick)

- MERN/MEAN at a glance: front‑end, API, DB, auth
- Microservices vs monolith: start simple, keep clear contracts
- API‑first development: spec → handlers → tests → UI

---

## Project Brief — Notes API + Micro Front‑End

- In‑memory storage (no DB) for speed
- Endpoints: create/list/delete notes
- Validation: `text` required, trimmed, 1–280 chars
- Front‑end: single HTML page with `fetch()` and minimal styling

---

## Minimal API Spec (copy‑ready)

```yaml
Base URL: http://localhost:8000
Entity: Note { id: uuid, text: string(1..280), created_at: ISO-8601 }
Endpoints:
  POST /notes
    Body: { "text": "..." }
    201: { id, text, created_at }
    400: { error: "validation_error", details: { text: "reason" } }
  GET /notes?limit=10&offset=0
    200: { items: [Note], total: number, limit: number, offset: number }
  DELETE /notes/{id}
    204: (no body)
    404: { error: "not_found" }
Validation:
  - text required; trim; length 1..280
```

---

## Copy‑ready Prompt — API Spec

```text
Propose a minimal REST API spec for a notes app with POST /notes, GET /notes with limit/offset, and DELETE /notes/{id}. Include JSON schemas and validation rules for "text" (1..280 chars), and example error payloads.
```

---

## Copy‑ready Prompt — Validation Rules

```text
Suggest concise validation rules for a "text" field (notes): trimming, length bounds, and disallowed-only-whitespace. Provide 2 positive and 2 negative examples.
```

---

## Copy‑ready Prompt — Front‑end fetch

```text
Generate a vanilla JS fetch() snippet to call POST /notes and handle JSON validation errors. Return either { ok:true, data } or { ok:false, error } and show minimal inline error handling.
```

---

## Live with Continue + Ollama

- Models: `phi3:mini` (fast) or `llama3.2:3b-instruct` (balanced)
- Flow: problem → generate handlers/tests → run → minimal diff → iterate
- Preflight: ensure models pulled; have offline prompts ready if needed

---

## Exercise — Build Core Endpoints

- Implement POST /notes with validation and standardized error JSON
- Implement GET /notes with `limit`/`offset` and `total`
- Implement DELETE /notes/{id} with 204 and 404
- Keep all state in memory for this session

---

## Optional Add‑ons (choose 1)

- Pagination polish: default `limit=10`, clamp to max 50
- Validation polish: trim input; enforce 1..280; return consistent error shape
- Bonus: basic profanity filter list on the server

---

## Micro Front‑End (vanilla)

- Minimal HTML: input + button + list
- JS: `fetch()` POST to create; GET to list; DELETE on click
- UX: show error messages from `{ error, details }`

---

## Examples Menu (student picks)

- Social & fun: Polls & Voting; Feedback Wall; Secret Santa
- Campus life: Lost & Found Board; Event RSVP; Office Hours Queue
- Productivity: Habit Tracker; Flashcards; Todo with Streaks
- Web utilities: URL Shortener; Pastebin/Snippet Box; Bookmark Manager

---

## Practical App Example 1: Campus Event & Club Finder

**The Goal:** An app to help students discover campus events and clubs that match their interests.

- Architecture:
  1. Data Ingestion: A scheduled script scrapes official university calendars and student group pages.
  2. AI Tagging: The scraped event descriptions are sent to an LLM (like Claude or GPT) to be tagged with keywords (e.g., 'sports', 'tech', 'music', 'free food').
  3. API: A simple API allows users to search for events by date, keyword, or club name.
  4. Frontend: A mobile-friendly web app displays events in a clean, searchable interface.

- Cloud/DevOps Concepts in Action:
  - Scheduled Tasks (Cron): For automated data scraping.
  - AI for Data Enrichment: Using an LLM to add valuable metadata to raw data.
  - Search & Discovery: A core product pattern for many applications.

---

## Practical App Example 2: Class Registration Notifier

**The Goal:** Get a text message the instant a spot opens up in a full class.

- Architecture:
  1. The Scraper: A serverless function (AWS Lambda) runs every minute, checking the university's registration portal for a specific class section.
  2. State Management: A simple database (like DynamoDB) stores which user is watching which class.
  3. Notification: If a spot opens, the function uses a service like Twilio to send an SMS alert to the user.
  4. Frontend: A simple UI where students can input the class number and their phone number.

- Cloud/DevOps Concepts in Action:
  - High-Frequency Scheduled Automation: Running a task much more frequently than a daily cron job.
  - Serverless at Scale: Can support thousands of students watching different classes with minimal cost.
  - Third-Party API Integration: Connecting to a service like Twilio.

---

## Practical App Example 3: Automated Meme Generator Bot

**The Goal:** A bot for social media that takes an image and text, and creates a meme.

- Architecture:
  1. The Trigger: A user uploads an image to a specific cloud storage bucket (e.g., Amazon S3).
  2. The Event: The upload event triggers a serverless function (AWS Lambda).
  3. Image Processing: The function uses a library like Pillow in Python to draw the top and bottom text onto the image.
  4. The Result: The final meme image is saved to a different 'output' bucket, ready to be shared.

- Cloud/DevOps Concepts in Action:
  - Event-Driven Architecture: The entire workflow is stateless and triggered by an event.
  - Image Manipulation: A common use case for serverless functions.
  - Cost-Effective: You only pay for the few milliseconds of compute time it takes to generate one meme.

---

## Practical App Example 4: YouTube Video Summarizer

**The Goal:** Paste a YouTube URL and get an AI-generated summary and comment analysis.

- Architecture:
  1. Frontend: A simple web app where the user pastes the YouTube URL.
  2. Backend API: A serverless function uses the YouTube Data API to fetch the video's transcript and comments.
  3. Asynchronous AI Jobs: The function submits two tasks to a queue (like AWS SQS):
     - Task 1: Send transcript to an LLM for summarization.
     - Task 2: Send comments to an LLM for sentiment analysis.
  4. Display Results: Once the tasks are complete, the results are saved, and the frontend can display them.

- Cloud/DevOps Concepts in Action:
  - Asynchronous Workflows & Task Queues: The right way to handle long-running tasks.
  - Chaining AI Services: Combining multiple LLM calls to create a sophisticated result.
  - API Integration: Working with a major third-party API (YouTube).

---

## Practical App Example 5: Collaborative Spotify Playlist

**The Goal:** A web app where friends can log in and add songs to a shared playlist.

- Architecture:
  1. Frontend: A React or Svelte app that handles the user interface.
  2. Authentication: Users log in via Spotify's OAuth 2.0 flow. The app never sees their password, it just gets a temporary token to act on their behalf.
  3. Backend API: A small API (on Heroku, Fly.io, or PaaS) that uses the user's token to interact with the Spotify API (e.g., search for tracks, add tracks to a playlist).
  4. Real-time Updates: Use WebSockets to instantly show when someone else adds a new song to the playlist.

- Cloud/DevOps Concepts in Action:
  - OAuth 2.0: The standard for secure, third-party authentication.
  - API Proxying: The backend acts as a secure proxy between the user and the Spotify API.
  - PaaS (Platform as a Service): Heroku or Fly.io make it incredibly easy to deploy a web application from a Git repository.

---

## Practical App Example 6: Multiplayer Game Backend

**The Goal:** A backend to manage the state for a simple real-time multiplayer game.

- Architecture:
  1. Game Client: (e.g., Unity, Godot, or browser-based) connects to the backend via WebSockets for low-latency communication.
  2. Game Servers: A fleet of Docker containers running a stateful application (e.g., in Node.js or C#). Managed by a container orchestrator like Kubernetes (e.g., Amazon EKS).
  3. State Management: A fast in-memory database like Redis is used to store temporary game state (player locations, scores).
  4. Player Accounts: A persistent database like PostgreSQL stores user accounts and long-term progress.

- Cloud/DevOps Concepts in Action:
  - Stateful Applications: A more complex challenge than stateless APIs.
  - Container Orchestration: Kubernetes automatically manages scaling and healing of the game server fleet.
  - Low-Latency Networking: Critical for a good user experience in real-time applications.

---

## Practical App Example 7: "Link in Bio" Page (like Linktree)

**The Goal:** A fast, simple, and cheap-to-host personal landing page.

- Architecture:
  1. Frontend: A static website (HTML, CSS, JS) built with a generator like Hugo or Astro. Hosted on Netlify, Vercel, or GitHub Pages.
  2. Analytics: To track link clicks, the frontend sends a request to a serverless function (Netlify Functions, AWS Lambda) which records the event.
  3. Data Store: The click data is stored in a simple, low-cost NoSQL database or even a Google Sheet via its API.

- Cloud/DevOps Concepts in Action:
  - Jamstack: The frontend is pre-built and served from a CDN, making it incredibly fast and secure.
  - Git-based Workflow: `git push` to the main branch automatically triggers a new deployment on Netlify/Vercel.
  - Minimal Cost: Hosting for the static site is often free, and serverless function calls are extremely cheap.

---

## Practical App Example 8: Real-time Polling App

**The Goal:** A web app where users can vote and see results update live.

- Architecture:
  1. Frontend: A modern JavaScript app (React, Vue) hosted on a static hosting service like Netlify or AWS S3 + CloudFront for global speed.
  2. Backend API: A containerized API on AWS Fargate or Google Kubernetes Engine handles incoming votes.
  3. Database: A scalable NoSQL database like Amazon DynamoDB or Firestore stores the poll results.
  4. Real-time: A WebSocket API or a service like Pusher pushes live updates to all connected users.

- Cloud/DevOps Concepts in Action:
  - Microservices: Frontend and backend are decoupled and can be scaled independently.
  - Managed Services: Using a managed database (DynamoDB) reduces operational overhead.
  - CI/CD: Separate pipelines for frontend and backend allow for independent updates.

---

## Practical App Example 9: AI Flashcard Generator

**The Goal:** Upload lecture notes (PDF) and get a set of flashcards to study from.

- Architecture:
  1. Frontend: A simple web page to upload a PDF file directly to Amazon S3.
  2. Event Trigger: The S3 upload triggers a Lambda function.
  3. AI Processing: The function sends the PDF to an AI service like Anthropic Claude or OpenAI's GPT-4 with a prompt: "Generate question/answer flashcards from this document."
  4. Display: The results are saved to a database, and the user is redirected to a page where they can view and study the generated flashcards.

- Cloud/DevOps Concepts in Action:
  - Third-Party API Integration: Calling an external AI service.
  - Processing Unstructured Data: Handling file uploads and parsing them.
  - Asynchronous Workflow: The user can close the page while the AI works; the results will be ready when they return.

---

## Capstone Example: "Project UniVerse"

**The Goal:** A platform for students across colleges to connect based on interests and collaborate on projects, research, and hobbies.

- Key Features:
  - Smart Profiles: Users list skills (Python, UI/UX), interests (Game Dev, AI), and current classes. An AI model suggests potential collaborators.
  - Project Hub: A feed where students can post ideas ("Need a React dev for a hackathon app") and recruit teammates.
  - Collaboration Spaces: For each project, an integrated chat, a shared document editor, and a simple task board.

- Cloud/DevOps Concepts in Action: This is a full-fledged application that uses everything we've discussed.
  - Microservices Architecture: The app is broken down into smaller, independent services (User Service, Project Service, Chat Service, etc.), each in its own Docker container.
  - Container Orchestration: A Kubernetes cluster manages the hundreds of containers needed to run the app at scale.
  - Multiple Databases: Using the right tool for the job: PostgreSQL for user/project data, Redis for caching, and Elasticsearch for powerful search across profiles and projects.
  - Real-time Communication: A WebSocket service handles live chat and notifications.
  - Advanced CI/CD: Dozens of separate CI/CD pipelines, one for each microservice, allowing teams to deploy updates independently and safely using Canary Releases.
  - Infrastructure as Code (IaC): The entire cloud infrastructure (Kubernetes cluster, databases, networking) is defined in Terraform.

---

## Building for Free: The Student Developer Stack

You don't need a credit card to build real-world applications. Leverage free tiers and student packs!

- Your #1 Starting Point: The GitHub Student Developer Pack
  - A massive bundle of free developer tools. Get it with your student email.
  - Includes: Free domain names (e.g., .me), cloud credits for AWS/Azure/GCP, and access to dozens of professional tools.

- Hosting Your Application (Backend & Full-Stack):
  - PaaS (Platform as a Service): Easiest way to start.
    - Heroku / Render: Free tier for small apps (often "sleeps" when inactive). Perfect for portfolio projects.
    - Fly.io: Generous free tier for containers and small databases.
  - Serverless (The most cost-effective way):
    - Vercel / Netlify: Free hosting for static frontends and a large free tier for serverless functions.
    - AWS/GCP/Azure Free Tiers: Offer millions of serverless function calls per month for free, forever.

- Databases & Storage:
  - PostgreSQL: Supabase or Railway offer generous free-tier databases with integrated APIs.
  - NoSQL: MongoDB Atlas and Firebase have perpetual free tiers for smaller projects.
  - Object Storage: Cloudflare R2 or the AWS S3 free tier are great for storing user uploads.

- A Free Stack for "Project UniVerse":
  - Frontend: React app hosted on Vercel.
  - Backend: Serverless functions on Vercel or AWS Lambda.
  - Database: Free-tier Supabase PostgreSQL database.
  - Authentication: Clerk or Auth0's free tier for user logins.
  - Code & CI/CD: Hosted on GitHub (free private repos & actions).

---

## Resources & Links

- Reusable prompts: `prompts/reusable_prompts.md` (Session 05 section)
- Local models: `LOCAL_AI_SETUP.md`
- Optional docs: FastAPI, Express, JSON Schema

---

## Wrap + Homework

- Built an API + micro front‑end with LLM support
- Homework: add one endpoint; include LLM‑generated tests and updated docs
- Artifact: short screen recording + API README
