<div align="center">

<br/>

<img width="100" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Flag_of_Nepal.svg/800px-Flag_of_Nepal.svg.png" alt="Nepal"/>

<br/>

# 🏛️ Nepal Online Tax Payment System

### *कर तिर्नुस् — सजिलो, छिटो, सुरक्षित*
### *Pay Tax — Easy. Fast. Secure.*

<br/>

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.x-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org)
[![eSewa](https://img.shields.io/badge/eSewa-Integrated-60BB46?style=for-the-badge)](https://esewa.com.np)
[![Khalti](https://img.shields.io/badge/Khalti-Integrated-5C2D91?style=for-the-badge)](https://khalti.com)
[![IPS](https://img.shields.io/badge/IPS-Integrated-E63946?style=for-the-badge)](https://ips.gov.np)
[![License](https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge)]()
[![Status](https://img.shields.io/badge/Status-Production-blue?style=for-the-badge)]()

<br/>

> A modern, fully dynamic **Online Tax Payment Portal** for Nepal — enabling taxpayers from local municipalities to view and pay **House & Land Tax**, **Business Tax**, and **Local Level Tax** online using **eSewa**, **Khalti**, and **IPS (Interbank Payment System)**. Built with **Python + Django** using the **latest payment gateway integrations**.

<br/>

---

</div>

## 📌 Table of Contents

- [Overview](#-overview)
- [Screenshots](#-screenshots)
- [Payment Gateways](#-payment-gateways)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [System Workflow](#-system-workflow)
- [Installation](#-installation)
- [Project Structure](#-project-structure)
- [Payment Integration Guide](#-payment-integration-guide)
- [API Endpoints](#-api-endpoints)
- [Roles & Access](#-roles--access)
- [Reports & Invoice](#-reports--invoice)
- [Deployment](#-deployment)
- [License](#-license)

---

## 🌏 Overview

The **Nepal Online Tax Payment System** is a government-grade digital platform that modernizes local tax collection across Nepal. Taxpayers can log in, view all their pending and paid taxes across multiple categories, make secure online payments through any of the three supported payment gateways, and instantly download **official PDF invoices and reports** — eliminating the need to visit municipal offices.

### 💡 Tax Categories Supported

| Tax Type | Description |
|---|---|
| 🏠 **House Tax** | Residential property tax based on ward and house type |
| 🌾 **Land Tax** | Agricultural and non-agricultural land tax |
| 🏢 **Business Tax** | Annual commercial business registration & renewal tax |
| 🏛️ **Local Level Tax** | Municipality/Gaupalika imposed local service charges |

---

## 📸 Screenshots

> 📷 Add your screenshots to a `/screenshots` folder in your repo — they will render automatically below.

<br/>

### 🏠 Taxpayer Dashboard
![Dashboard](screenshots/dashboard.png)

---

### 🧾 Tax Records — House, Land & Business
![Tax Records](screenshots/tax-records.png)

---

### 💳 Payment Gateway Selection
![Payment Selection](screenshots/payment-selection.png)

---

### ✅ eSewa Payment Flow
![eSewa Payment](screenshots/esewa-payment.png)

---

### 💜 Khalti Payment Flow
![Khalti Payment](screenshots/khalti-payment.png)

---

### 🏦 IPS Payment Flow
![IPS Payment](screenshots/ips-payment.png)

---

### 📄 Tax Invoice / Receipt
![Invoice](screenshots/invoice.png)

---

### 📊 Admin Dashboard
![Admin](screenshots/admin-dashboard.png)

---

> 📂 **To add screenshots:** Create a `screenshots/` folder in the root of your repo and add PNG/JPG files with the names above.

---

## 💳 Payment Gateways

### 🟢 eSewa — Latest v2 Integration

eSewa is Nepal's most widely used digital wallet. This system uses the **latest eSewa payment API v2** with HMAC-SHA256 signature verification.

```
Flow:  Taxpayer → Select eSewa → Redirect to eSewa → Pay → Callback → Verify → Receipt
```

| Parameter | Value |
|---|---|
| API Version | v2 (Latest) |
| Signature | HMAC-SHA256 |
| Environment | Live + Sandbox |
| Callback | Server-to-server verification |

---

### 🟣 Khalti — Latest Khalti Payment API

Khalti is a leading digital payment platform in Nepal. Uses the **latest Khalti Checkout API** with `pidx`-based lookup verification.

```
Flow:  Taxpayer → Select Khalti → Initiate Payment → Redirect → Pay → Verify via pidx → Receipt
```

| Parameter | Value |
|---|---|
| API Version | Latest (pidx-based) |
| Auth | Secret Key Header |
| Environment | Live + Test |
| Verification | Server-side lookup |

---

### 🔴 IPS — Interbank Payment System (Nepal Clearing House)

IPS is operated by **Nepal Clearing House Ltd (NCHL)** and supports direct bank account payments across all major Nepali banks.

```
Flow:  Taxpayer → Select IPS → NCHL Redirect → Choose Bank → Pay → Webhook → Receipt
```

| Parameter | Value |
|---|---|
| Operator | Nepal Clearing House Ltd (NCHL) |
| Supports | All major Nepali banks |
| Environment | Live + UAT |
| Verification | NCHL webhook callback |

---

## ✨ Features

### 👤 Taxpayer Portal
- Secure login with citizenship number or registered phone/email
- View all tax records linked to their profile — house, land, business, local
- View due amount, due date, penalty/fine if overdue
- Full payment history with date, amount, gateway used
- Download official PDF invoice/receipt for any payment
- Multi-year tax record view

### 🏠 House & Land Tax
- Property details — location (ward, municipality), area, type
- Calculated tax amount based on local government rates
- Overdue fines auto-calculated per day
- Partial and full payment support
- Linked to land ownership records

### 🏢 Business Tax
- Business registration details (PAN, registration number, type)
- Annual business tax and renewal fee
- Penalty tracking for late payment
- Multi-branch business support

### 🏛️ Local Level Tax
- Municipality / Gaupalika specific charges
- Water tax, garbage collection, road maintenance, etc.
- Configurable tax types per local government

### 💰 Online Payment (eSewa / Khalti / IPS)
- Choose preferred gateway at checkout
- Secure redirect to gateway, return to portal after payment
- Server-side payment verification (no client-side trust)
- Duplicate payment prevention
- Failed/cancelled payment handling with retry
- Transaction ID and reference stored per payment

### 🧾 Invoice & Reports
- Instant PDF invoice generation after successful payment
- Official format with municipality letterhead
- QR code on invoice for authenticity verification
- Taxpayer can download past invoices anytime
- Bulk report for all payments in a date range

### 🖥️ Admin Panel
- Overview dashboard — total collected, pending, overdue
- Add/edit/manage tax records per taxpayer
- View and reconcile all payments by gateway
- Manual payment recording (counter payment)
- Generate collection reports by tax type, date, ward
- Export reports to PDF and Excel

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11+ |
| Framework | Django 4.x |
| Database | PostgreSQL 15+ |
| ORM | Django ORM |
| Frontend | Django Templates + Bootstrap 5 |
| PDF Generation | ReportLab / WeasyPrint |
| Payment | eSewa v2, Khalti API, IPS (NCHL) |
| Authentication | Django Auth + Custom Backend |
| Async Tasks | Celery + Redis (for notifications) |
| File Storage | Django FileStorage / AWS S3 |
| API | Django REST Framework (DRF) |
| Environment | python-decouple / django-environ |
| Server | Gunicorn + Nginx |

---

## 🔄 System Workflow

```
👤 Taxpayer Logs In (Citizenship No. / Phone)
          │
          ▼
📋 Dashboard — View All Tax Records
   ┌──────────────┬──────────────┬────────────────┐
   │  House Tax   │  Land Tax    │  Business Tax  │
   │  Local Tax   │  Overdue     │  Paid History  │
   └──────────────┴──────────────┴────────────────┘
          │
          ▼
🔲 Select Tax to Pay → View Bill Summary
          │
          ▼
💳 Choose Payment Gateway
   ┌──────────┬──────────┬──────────┐
   │  eSewa   │  Khalti  │   IPS    │
   └──────────┴──────────┴──────────┘
          │
          ▼
🔀 Redirect to Gateway → Taxpayer Pays
          │
          ▼
🔁 Gateway Callback → Server Verifies Payment
          │
    ┌─────┴─────┐
    │           │
   ✅          ❌
  Success     Failed / Cancelled
    │              │
    ▼              ▼
💾 Save to DB   Show Error + Retry
    │
    ▼
🧾 Generate PDF Invoice
    │
    ▼
📩 Email/SMS Receipt to Taxpayer
    │
    ▼
📊 Admin Dashboard Updated
```

---

## ⚙️ Requirements

- Python >= 3.11
- pip >= 23.x
- PostgreSQL >= 15
- Redis (for Celery task queue)
- Nginx + Gunicorn (production)

---

## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/nepal-tax-payment-system.git
cd nepal-tax-payment-system
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment
```bash
cp .env.example .env
```

Edit `.env`:
```env
# Django
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/nepal_tax_db

# eSewa (v2 - Latest)
ESEWA_MERCHANT_CODE=your-merchant-code
ESEWA_SECRET_KEY=your-secret-key
ESEWA_PAYMENT_URL=https://rc-epay.esewa.com.np/api/epay/main/v2/form
ESEWA_VERIFY_URL=https://rc-epay.esewa.com.np/api/epay/transaction/status/

# Khalti (Latest)
KHALTI_SECRET_KEY=your-khalti-secret-key
KHALTI_INITIATE_URL=https://a.khalti.com/api/v2/epayment/initiate/
KHALTI_LOOKUP_URL=https://a.khalti.com/api/v2/epayment/lookup/

# IPS / NCHL
IPS_MERCHANT_ID=your-merchant-id
IPS_APP_ID=your-app-id
IPS_APP_NAME=NepalTaxPortal
IPS_SECRET_KEY=your-ips-secret
IPS_BASE_URL=https://uat.ipg.nchl.com.np

# Email
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your@email.com
EMAIL_HOST_PASSWORD=your-app-password

# SMS (Sparrow SMS)
SPARROW_SMS_TOKEN=your-token
SPARROW_SMS_FROM=TaxPortal

# Redis (Celery)
CELERY_BROKER_URL=redis://localhost:6379/0
```

### 5. Run migrations
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6. Load initial data (optional)
```bash
python manage.py loaddata provinces districts municipalities
```

### 7. Run the development server
```bash
python manage.py runserver
```

🌐 Visit: `http://localhost:8000`
🔐 Admin: `http://localhost:8000/admin`

### 8. Start Celery worker (in a separate terminal)
```bash
celery -A config worker --loglevel=info
```

---

## 📁 Project Structure

```
nepal-tax-payment-system/
│
├── config/                          # Django project settings
│   ├── settings/
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   ├── celery.py
│   └── wsgi.py
│
├── apps/
│   │
│   ├── taxpayer/                    # Taxpayer registration & profile
│   │   ├── models.py
│   │   ├── views.py
│   │   └── urls.py
│   │
│   ├── tax/                         # Tax records & categories
│   │   ├── models.py                # HouseTax, LandTax, BusinessTax, LocalTax
│   │   ├── views.py
│   │   ├── serializers.py
│   │   └── urls.py
│   │
│   ├── payments/                    # Payment processing
│   │   ├── models.py                # Payment, Transaction
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── gateways/
│   │       ├── __init__.py
│   │       ├── base.py              # Abstract base gateway
│   │       ├── esewa.py             # eSewa v2 integration
│   │       ├── khalti.py            # Khalti latest API
│   │       └── ips.py               # IPS / NCHL integration
│   │
│   ├── invoices/                    # PDF invoice generation
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── generators.py            # ReportLab / WeasyPrint PDF logic
│   │   └── templates/
│   │       └── invoice_template.html
│   │
│   ├── reports/                     # Admin reports & exports
│   │   ├── views.py
│   │   └── exporters.py             # PDF + Excel export
│   │
│   └── notifications/               # Email + SMS
│       ├── tasks.py                 # Celery async tasks
│       └── senders.py
│
├── templates/                       # Django HTML templates
│   ├── base.html
│   ├── dashboard/
│   ├── tax/
│   ├── payments/
│   └── admin/
│
├── static/                          # CSS, JS, images
├── media/                           # Uploaded files
├── requirements.txt
├── .env.example
└── manage.py
```

---

## 🔌 Payment Integration Guide

### ✅ eSewa v2 (Latest)

```python
# apps/payments/gateways/esewa.py

import hmac, hashlib, base64
from django.conf import settings

def generate_esewa_signature(total_amount, transaction_uuid, product_code):
    message = f"total_amount={total_amount},transaction_uuid={transaction_uuid},product_code={product_code}"
    secret = settings.ESEWA_SECRET_KEY.encode('utf-8')
    signature = hmac.new(secret, message.encode('utf-8'), hashlib.sha256)
    return base64.b64encode(signature.digest()).decode('utf-8')

def verify_esewa_payment(product_code, total_amount, transaction_uuid):
    import requests
    params = {
        "product_code": product_code,
        "total_amount": total_amount,
        "transaction_uuid": transaction_uuid,
    }
    response = requests.get(settings.ESEWA_VERIFY_URL, params=params)
    data = response.json()
    return data.get("status") == "COMPLETE"
```

---

### ✅ Khalti (Latest pidx-based)

```python
# apps/payments/gateways/khalti.py

import requests
from django.conf import settings

def initiate_khalti_payment(amount_paisa, order_id, return_url, taxpayer_name, phone):
    headers = {"Authorization": f"Key {settings.KHALTI_SECRET_KEY}"}
    payload = {
        "return_url": return_url,
        "website_url": settings.SITE_URL,
        "amount": amount_paisa,        # in paisa (Rs. 100 = 10000 paisa)
        "purchase_order_id": order_id,
        "purchase_order_name": f"Tax Payment - {order_id}",
        "customer_info": {"name": taxpayer_name, "phone": phone},
    }
    response = requests.post(settings.KHALTI_INITIATE_URL, json=payload, headers=headers)
    return response.json()             # Returns { pidx, payment_url }

def verify_khalti_payment(pidx):
    headers = {"Authorization": f"Key {settings.KHALTI_SECRET_KEY}"}
    response = requests.post(settings.KHALTI_LOOKUP_URL, json={"pidx": pidx}, headers=headers)
    data = response.json()
    return data.get("status") == "Completed"
```

---

### ✅ IPS / NCHL

```python
# apps/payments/gateways/ips.py

import hashlib, hmac
from django.conf import settings

def generate_ips_token(merchant_id, app_id, ref_id, amount):
    raw = f"{merchant_id}{app_id}{ref_id}{amount}"
    token = hmac.new(
        settings.IPS_SECRET_KEY.encode(),
        raw.encode(),
        hashlib.sha256
    ).hexdigest()
    return token

def build_ips_payload(ref_id, amount, remarks):
    return {
        "merchantId":   settings.IPS_MERCHANT_ID,
        "appId":        settings.IPS_APP_ID,
        "appName":      settings.IPS_APP_NAME,
        "txnAmt":       str(amount),
        "referenceId":  ref_id,
        "remarks":      remarks,
        "token":        generate_ips_token(
                            settings.IPS_MERCHANT_ID,
                            settings.IPS_APP_ID,
                            ref_id, amount
                        ),
    }
```

---

## 🔌 API Endpoints

```
# Auth
POST   /api/auth/login/                        → Taxpayer login
POST   /api/auth/logout/                       → Logout

# Tax Records
GET    /api/taxes/                             → All tax records for logged-in taxpayer
GET    /api/taxes/house/                       → House tax records
GET    /api/taxes/land/                        → Land tax records
GET    /api/taxes/business/                    → Business tax records
GET    /api/taxes/local/                       → Local level tax records

# Payments
POST   /api/payments/initiate/                 → Initiate payment (returns gateway URL)
GET    /api/payments/esewa/callback/           → eSewa success callback
GET    /api/payments/esewa/failure/            → eSewa failure callback
GET    /api/payments/khalti/callback/          → Khalti return URL handler
POST   /api/payments/ips/webhook/              → IPS server webhook
GET    /api/payments/history/                  → Taxpayer payment history

# Invoices
GET    /api/invoices/{payment_id}/             → View invoice details
GET    /api/invoices/{payment_id}/download/    → Download PDF invoice

# Reports (Admin)
GET    /api/admin/reports/summary/             → Collection summary
GET    /api/admin/reports/export/pdf/          → Export report as PDF
GET    /api/admin/reports/export/excel/        → Export report as Excel
```

---

## 👥 Roles & Access

| Role | Access |
|---|---|
| **Taxpayer** | View own tax records, pay online, download invoices |
| **Ward Officer** | View payments in own ward, manual payment entry |
| **Municipality Admin** | Full tax management, reports, all taxpayers |
| **Super Admin** | System-wide access, gateway config, all municipalities |

---

## 🧾 Reports & Invoice

### PDF Invoice includes:
- 🏛️ Municipality / Gaupalika official letterhead
- Taxpayer name, address, citizenship number
- Tax type, period, amount, fine/penalty (if any)
- Payment date, gateway used, transaction ID
- QR code for authenticity verification
- Official stamp placeholder

### Reports available:
- Daily / Monthly / Yearly collection report
- Gateway-wise collection breakdown (eSewa / Khalti / IPS)
- Tax-type wise collection (House / Land / Business / Local)
- Ward-wise and municipality-wise summary
- Overdue taxpayers list
- Export to **PDF** and **Excel (.xlsx)**

---

## 🔐 Security

- CSRF protection on all forms and API endpoints
- HMAC-SHA256 signature verification for eSewa
- Server-side `pidx` lookup for Khalti (never trust client)
- IPS webhook token verification
- Django authentication with session management
- Role-based access control on every view
- Duplicate payment prevention via idempotency checks
- All secrets stored in environment variables — never in code
- SQL injection protection via Django ORM
- Rate limiting on payment initiation endpoints

---

## 🌐 Deployment

```bash
# Collect static files
python manage.py collectstatic --noinput

# Run database migrations
python manage.py migrate

# Start Gunicorn
gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 4

# Start Celery
celery -A config worker --loglevel=info --detach
```

**Nginx config snippet:**
```nginx
server {
    listen 80;
    server_name yourdomain.gov.np;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static/ {
        alias /path/to/staticfiles/;
    }

    location /media/ {
        alias /path/to/media/;
    }
}
```

Set in `.env`:
```env
DEBUG=False
ALLOWED_HOSTS=yourdomain.gov.np
```

---

## 🤝 Contributing

1. Fork the repository
2. Create your branch — `git checkout -b feature/your-feature`
3. Commit changes — `git commit -m 'Add: feature description'`
4. Push — `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

<br/>

**🇳🇵 Digitizing Tax Collection for Nepal**

*eSewa · Khalti · IPS — All in One Portal*

<br/>

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.x-092E20?style=flat-square&logo=django)](https://djangoproject.com)
[![eSewa](https://img.shields.io/badge/eSewa-v2-60BB46?style=flat-square)](https://esewa.com.np)
[![Khalti](https://img.shields.io/badge/Khalti-Latest-5C2D91?style=flat-square)](https://khalti.com)
[![IPS](https://img.shields.io/badge/IPS-NCHL-E63946?style=flat-square)](https://nchl.com.np)
[![Made in Nepal](https://img.shields.io/badge/Made%20in-Nepal%20🇳🇵-blue?style=flat-square)]()

</div>
