# DDoS Demo - How to Perform Attack

This guide explains how to run a simulated DDoS attack using Locust on the Node.js server.

## Prerequisites

Install required packages:

```bash
# Install Node.js dependencies
npm install express

# Install Python packages
pip install locust
```

## Step-by-Step Guide

### Step 1: Start the Target Server

Open Terminal 1 and run:

```bash
cd ddos_demo
node server.js
```

**Expected Output:**
```
Server running on http://localhost:3000
```

The server will start listening on `http://localhost:3000`

---

### Step 2: Launch Locust for DDoS Simulation

Open Terminal 2 and run:

```bash
cd ddos_demo
locust -f locustfile.py --host=http://localhost:3000
```

**Output:**
```
[2024-11-13 12:00:00] locust/main.py: Starting web interface at http://0.0.0.0:8089
[2024-11-13 12:00:00] locust/main.py: Starting Locust 2.x.x
```

This starts Locust's web interface at `http://localhost:8089`

---

### Step 3: Configure Attack Parameters

1. **Open Browser:** Go to `http://localhost:8089`

2. **Set Attack Parameters:**
   - **Number of users:** 100 (simulated concurrent users)
   - **Spawn rate:** 10 (new users per second)
   - **Host:** `http://localhost:3000` (should already be set)

3. **Click "Start Swarming"** button

---

### Step 4: Observe the Attack

#### In Locust Web Dashboard:
- **Statistics tab:** Shows request count, response times, failures
- **Charts tab:** Real-time graphs of requests/second, response time
- **Failures tab:** Failed requests due to server overload

#### In Server Terminal:
You'll see the server getting hammered with requests and may eventually crash or timeout.

---

## Attack Scenarios

### Light Attack (Testing)
- **Users:** 10
- **Spawn Rate:** 5
- **Duration:** 30 seconds
- **Effect:** Server handles easily, no degradation

### Medium Attack
- **Users:** 50
- **Spawn Rate:** 10
- **Duration:** 1 minute
- **Effect:** Response times increase, some requests slow down

### Heavy Attack (Realistic DDoS)
- **Users:** 200+
- **Spawn Rate:** 20+
- **Duration:** 5+ minutes
- **Effect:** Server becomes unresponsive, requests timeout/fail

---

## How It Works

### Server (Node.js)
```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Server is running!');  // Simple endpoint
});

app.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});
```

- Single endpoint `/` that returns simple text
- No rate limiting or DDoS protection
- Will get overwhelmed by many concurrent requests

### Client Simulator (Locust - Python)
```python
from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 2)  # Wait 1-2 seconds between requests
    
    @task
    def index(self):
        self.client.get("/")  # Send GET request to /
```

- Each simulated user makes requests every 1-2 seconds
- With 100 users = ~50-100 requests per second
- Distributed load testing tool

---

## What is DDoS?

**DDoS (Distributed Denial of Service):**
- Multiple sources send massive traffic to target
- Goal: Make server unavailable to legitimate users
- Overwhelms server resources (CPU, bandwidth, memory)
- Server can't handle all requests, becomes unresponsive

**In this demo:**
- Locust = simulated attackers
- Node.js server = target
- Single machine instead of distributed, but same principle

---

## Key Metrics to Monitor

| Metric | What it means |
|--------|---------------|
| **Requests/sec** | How many requests hit the server |
| **Response Time** | How long server takes to respond (should increase during attack) |
| **Failures** | Number of failed/timed-out requests |
| **Failure Rate** | Percentage of requests that fail |
| **CPU Usage** | Server CPU gets maxed out |
| **Memory Usage** | Server memory gets exhausted |

---

## Advanced Locust Command Options

```bash
# Run with specific number of users (no web UI)
locust -f locustfile.py --host=http://localhost:3000 -u 100 -r 10 -t 60s

# Flags:
# -u 100    = 100 concurrent users
# -r 10     = spawn 10 new users per second
# -t 60s    = run for 60 seconds
# --headless = no web UI, run in background
```

---

## Stopping the Attack

1. **In Locust:** Click "Stop" button in web interface
2. **Or:** Press `Ctrl+C` in terminal running Locust
3. **Server:** Press `Ctrl+C` to stop Node.js server

---

## Mitigation Techniques (How to Defend)

### 1. Rate Limiting
```javascript
const rateLimit = require('express-rate-limit');

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});

app.use(limiter);
```

### 2. Load Balancing
Distribute traffic across multiple servers

### 3. WAF (Web Application Firewall)
Block suspicious traffic patterns

### 4. CDN (Content Delivery Network)
Cloudflare, Akamai - absorb DDoS traffic

### 5. IP Filtering
Block IPs making excessive requests

---

## Educational Purpose Only

⚠️ **WARNING:** 
- This demo is for **educational purposes only**
- Performing DDoS attacks on real systems is **illegal**
- Violates Computer Fraud and Abuse Act (CFAA)
- Can result in federal prosecution and imprisonment
- Only test on systems you own or have explicit permission to test

---

## References

- [Locust Documentation](https://docs.locust.io/)
- [Node.js Express Server](https://expressjs.com/)
- [DDoS Attacks - OWASP](https://owasp.org/www-community/attacks/Denial_of_Service)
- [Rate Limiting - OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Nodejs_Security_Cheat_Sheet.html)
