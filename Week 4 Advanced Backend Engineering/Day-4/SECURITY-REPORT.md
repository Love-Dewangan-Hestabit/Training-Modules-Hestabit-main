## Week 4 (Day 4) - Security, Validation, Rate Limiting and Hardening

**Name: Love Dewangan**  
**Email: love.dewangan@hestabit.in**

## Task

Security Controls Implemented

- Validation using JOI and Zod
- Prevention of NoSQL Injection, XSS, Parameter pollution.
- CORS policy enforcement
- Global rate limiting using express-rate-limit
- Payload size limiting via express.json({ limit })

## Security Report

**Extreme Query Values**

**Threat:** Abuse of pagination parameters causing memory exhaustion or performance degradation.

**Test:**
GET /api/products?limit=1000000

![Extreme Query Values](./screenshots/Exteme_Values.png)

**Negative Numeric Parameters**

**Threat:** Bypassing logic with invalid numeric values.

**Test:**
GET /api/products?minPrice=-100

![Negative Numeric Parameters](./screenshots/Negative_parameter.png)

**NoSQL Injection**

**Threat:** Manipulating MongoDB queries using injected operators.

**Test:**
GET /api/products?search[$gt]=

![NoSQL Injection](./screenshots/NoSQL_Injection.png)

**HTTP Parameter Pollution**

**Threat:** Supplying the same query parameter multiple times to bypass validation.

**Test:**
GET /api/products?minPrice=100&minPrice=0

![Parameter_pollution](./screenshots/Parameter_pollution.png)

**Cross-Site Scripting (XSS)**

**Threat:** Injection of executable scripts into stored or reflected responses.

**Test:**
GET /api/products?search=<script>alert(1)</script>

![Cross-Site Scripting](./screenshots/XSS_test.png)

**Payload Size Abuse**

**Threat:** Large request bodies causing memory exhaustion (DoS).

**Test:**
POST /api/products with description > payload size limit

![Payload Size Abuse](./screenshots/Payload_limit_test.png)

**Rate Limiting**

**Threat:** Brute-force or denial-of-service via rapid repeated requests.

**Test:**
30 rapid consecutive requests to GET /api/products

![Rate Limiting](./screenshots/Rate_limit_test.png)

**Regular Expression Safety**

**Threat:** ReDoS attacks via catastrophic backtracking.

**Test:**
GET /api/products?search=AAAA...(5000 chars)

![Regular Expression Safety](./screenshots/Safe_regex_expression.png)
