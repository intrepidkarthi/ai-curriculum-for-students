# Session 09 — n8n Local Workshop (No Paid Tools)

This guide walks you through a local-only n8n workflow to orchestrate a simple multi-step AI-assisted flow without any paid APIs.

## Prerequisites
- n8n running locally (Docker or desktop)
- VS Code Continue + Ollama running locally

## What you’ll build (10–15 min)
A workflow that:
1) Accepts a POST request (Webhook)
2) Cleans and validates the text (Function)
3) Uses a local LLM (via Continue, outside n8n) to draft a reply prompt you can paste back
4) Branches on a simple rule (IF) and formats a friendly response (Function)
5) Responds synchronously (Respond to Webhook)

Note: Since we’re avoiding paid APIs, we won’t call an external LLM node. Instead, we’ll generate the LLM copy in VS Code Continue and paste it into the flow as needed.

## Steps

### 1) Webhook (POST)
- Method: POST
- Path: /ai-helper
- Test URL will look like: http://localhost:5678/webhook-test/ai-helper

### 2) Function — sanitize input
Example JS:
```javascript
const body = $json;
const text = (body.text || '').replace(/<[^>]*>/g, '').trim();
return [{ text }];
```

### 3) IF — simple rule (empty or too short)
- Condition: `{{ $json["text"].length > 10 }}`
- True → proceed
- False → respond with a short error message

### 4) Function — format response
For True branch:
```javascript
const text = $json.text;
// Paste a prompt result generated locally via VS Code Continue + Ollama
// Example: A friendly, concise rewrite plan or next-step suggestion
const reply = `Thanks! Here’s a concise plan for: "${text}"\n- Step 1: ...\n- Step 2: ...\n- Step 3: ...`;
return [{ reply }];
```
For False branch:
```javascript
return [{ reply: "Please provide a bit more detail (at least a short sentence)." }];
```

### 5) Respond to Webhook
- Set "Response Body" to `{{$json.reply}}`
- Status: 200

## How to use with local LLM
- In VS Code Continue (Provider: Ollama), ask the local LLM to “Draft a friendly, 3-step plan for [user text]. Keep it short and helpful.”
- Copy the drafted content into the Function node’s `reply` template.
- Alternatively, generate patterns (templates) once and reuse.

## Extensions (choose one)
- Add a second branch: if the text includes keywords (e.g., “deadline”), add a date reminder line.
- Add a small CSV lookup step (fees, dates) using a Function node (no external APIs).
- Add logging: append a simple JSON line to a file using a Function node plus n8n filesystem node.

## Testing
- Use `curl`:
```bash
curl -s -X POST "http://localhost:5678/webhook-test/ai-helper" \
  -H 'Content-Type: application/json' \
  -d '{"text":"Help me plan my placement prep for 4 weeks"}' | jq .
```

## Deliverable
- Screenshot of the flow and a short README note explaining your branches and the local LLM step.
