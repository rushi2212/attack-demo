# DDoS Demo - Quick Start Guide

## ✅ Setup Complete!

The DDoS demo is now fully functional. Here's how to run it:

---

## **Step 1: Terminal 1 - Start the Server**

```powershell
cd "c:\Users\rushi\OneDrive\Documents\B.E Project\Project Demo\ddos_demo"
node server.js
```

**Expected Output:**
```
==================================================
DDoS Demo Server Started
==================================================
Server running on http://localhost:3000
Waiting for DDoS simulation...
==================================================
```

---

## **Step 2: Terminal 2 - Launch Locust Attack**

```powershell
cd "c:\Users\rushi\OneDrive\Documents\B.E Project\Project Demo\ddos_demo"
python -m locust -f locustfile.py --host=http://localhost:3000
```

**Expected Output:**
```
[timestamp] locust/main.py: Starting web interface at http://0.0.0.0:8089
```

---

## **Step 3: Open Locust Web UI**

1. Open browser and go to: **http://localhost:8089**
2. You'll see the Locust dashboard with settings:
   - **Number of users:** Start with 100
   - **Spawn rate:** Set to 10-20
   - **Host:** Should show `http://localhost:3000`

3. Click **"Start Swarming"**

---

## **Attack Scenarios**

### 🟢 Light Attack (Safe Testing)
- **Users:** 50
- **Spawn Rate:** 5
- **Result:** Server handles easily, RPS: ~500

### 🟡 Medium Attack
- **Users:** 150  
- **Spawn Rate:** 15
- **Result:** Response times increase, visible lag

### 🔴 Heavy Attack (Realistic DDoS)
- **Users:** 300+
- **Spawn Rate:** 25
- **Result:** Server becomes unresponsive

---

## **Monitoring**

### In Server Terminal:
```
[12:34:56 PM] Requests: 1250 | RPS: 450
[12:34:57 PM] Requests: 1700 | RPS: 480
[12:34:58 PM] Requests: 2150 | RPS: 500
```

### In Locust Web Dashboard:
- **Statistics Tab:** Request count, response times
- **Charts Tab:** Real-time RPS graph
- **Failures Tab:** Failed/timed-out requests

---

## **Stop the Demo**

1. Press `Ctrl+C` in Locust terminal to stop the attack
2. Press `Ctrl+C` in server terminal to stop the server
3. If needed, free port 3000: `netstat -ano | findstr ":3000"` then `taskkill /PID <pid> /F`

---

## **Files Included**

- `server.js` - Target server with request tracking
- `locustfile.py` - Locust attack configuration
- `DDOS_GUIDE.md` - Detailed documentation
- `RUN_DDOS.md` - This quick start guide
