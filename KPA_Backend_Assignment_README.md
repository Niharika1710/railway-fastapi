# 🚀 KPA Backend Assignment

This project implements **two functional APIs** (POST and GET) for **wheel specification forms** using **FastAPI**, integrated with **PostgreSQL on Railway**.

It fulfills the assignment requirement to develop API endpoints adhering to the provided structure, ensuring correct data flow and persistence.

---

## ✅ Tech Stack

- **FastAPI** – Web framework
- **SQLAlchemy** – ORM for database operations
- **PostgreSQL** – Database (hosted on Railway)
- **Railway** – Deployment platform for backend and database
- **Uvicorn** – ASGI server

---

## ⚙️ Project Setup Instructions

1️⃣ **Clone the repository:**

```bash
git clone <your-repository-link>
cd <your-repository-folder>
```

2️⃣ **Create a virtual environment and activate it:**

```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

3️⃣ **Install dependencies:**

```bash
pip install -r requirements.txt
```

4️⃣ **Configure environment variables:**

Create a `.env` file:

```env
DATABASE_URL=your_postgresql_database_url
```

*(Use the Railway PostgreSQL URL.)*

5️⃣ **Run the server locally:**

```bash
uvicorn main:app --reload
```

---

## 📌 API Endpoints

### 1️⃣ POST API: Create Wheel Specification Form

**URL:**

```
POST /api/forms/wheel-specifications
```

**Description:**

Stores a new wheel specification form in the PostgreSQL database.

**Request Body Example:**

```json
{
  "formNumber": "WHEEL-2025-003",
  "submittedBy": "user_id_123",
  "submittedDate": "2025-07-03",
  "fields": {
    "treadDiameterNew": "915 (900-1000)",
    "lastShopIssueSize": "837 (800-900)",
    "condemningDia": "825 (800-900)",
    "wheelGauge": "1600 (+2,-1)"
  }
}
```

**Response:**

```json
{
  "success": true,
  "message": "Wheel specification submitted successfully.",
  "data": {
    "formNumber": "WHEEL-2025-003",
    "status": "Saved",
    "submittedBy": "user_id_123",
    "submittedDate": "2025-07-03"
  }
}
```

---

### 2️⃣ GET API: Fetch Wheel Specification Forms with Filters

**URL:**

```
GET /api/forms/wheel-specifications
```

**Optional Query Parameters:**

- `formNumber`: Filter by form number
- `submittedBy`: Filter by submitter
- `submittedDate`: Filter by submission date

**Example:**

```
/api/forms/wheel-specifications?formNumber=WHEEL-2025-003
```

**Response:**

```json
{
  "success": true,
  "message": "Filtered wheel specification forms fetched successfully.",
  "data": [
    {
      "formNumber": "WHEEL-2025-003",
      "submittedBy": "user_id_123",
      "submittedDate": "2025-07-03",
      "fields": {
        "treadDiameterNew": "915 (900-1000)",
        "lastShopIssueSize": "837 (800-900)",
        "condemningDia": "825 (800-900)",
        "wheelGauge": "1600 (+2,-1)"
      }
    }
  ]
}
```

---

## 🚀 Deployment URL for Testing

Access your deployed FastAPI backend and Swagger UI for live testing:

```
https://railway-fastapi-production-6c41.up.railway.app/docs
```

Test POST and GET APIs directly using the Swagger interface.

---

## 📝 Assumptions and Limitations

✅ The `formNumber` field is **unique** in the database to prevent duplicates.

✅ Request body fields are expected to follow the provided structure.

✅ Database URL is configured securely via environment variables.

✅ Filtering in the GET API is exact match for `formNumber`, `submittedBy`, and `submittedDate`.

✅ This implementation demonstrates functionality for **backend assessment with FastAPI and PostgreSQL** and is ready for integration with the provided frontend.

---

## ✅ Next

Once added:
- Commit this `README.md` to your repository.
- Record your screen demonstration.
- Prepare your submission with:
  - GitHub repository or zipped source code
  - Updated Postman collection with working APIs
  - Screen recording link
