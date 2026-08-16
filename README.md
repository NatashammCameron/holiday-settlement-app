# Holiday Settlement App

A full-stack web application for tracking and settling shared holiday expenses. Users can create holidays, add participants, record expenses and automatically calculate how much each person owes, reducing the complexity of splitting costs within a group.

## Features

### Authentication

- User registration
- Secure login
- Password hashing
- JWT authentication
- Protected routes
- User-specific data access

### Holiday Management

- Create holidays
- View holidays
- Update holidays
- Delete holidays
- User ownership of holidays

### Participant Management

- Add participants to a holiday
- Edit participant details
- Remove participants
- Retrieve participants for a holiday

### Expense Management

- Record expenses
- Track who paid
- Split expenses between participants
- Edit expenses
- Delete expenses

### Settlement Calculation

- Automatic balance calculation
- Settlement recommendations
- Payment tracking
- Simplified debt resolution

---

## Tech Stack

### Frontend

- React
- TypeScript
- Vite
- React Router

### Backend

- Python
- FastAPI
- SQLAlchemy

### Database

- PostgreSQL

### Authentication

- JWT (JSON Web Tokens)
- bcrypt
- Passlib

### Testing

- Pytest
- Vitest
- React Testing Library

---

## Architecture

```text
React Frontend
      │
      ▼
FastAPI REST API
      │
      ▼
PostgreSQL Database
```

---

## API Overview

### Authentication

```http
POST /auth/register
POST /auth/login
GET /auth/me
```

### Holidays

```http
GET /holidays
POST /holidays
GET /holidays/{id}
PUT /holidays/{id}
DELETE /holidays/{id}
```

### Participants

```http
GET /participants/holiday/{holiday_id}
POST /participants
PUT /participants/{id}
DELETE /participants/{id}
```

### Expenses

```http
GET /expenses/holiday/{holiday_id}
POST /expenses
PUT /expenses/{id}
DELETE /expenses/{id}
```

### Settlements

```http
GET /settlements/holiday/{holiday_id}
GET /settlements/holiday/{holiday_id}/payments
```

---

## Getting Started

### Clone the Repository

```bash
git clone <repository-url>
cd holiday-settlement-app
```

---

### Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file:

```env
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
```

Start the API:

```bash
uvicorn app.main:app --reload
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

---

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

## Running Tests

### Backend

```bash
pytest
```

### Frontend

```bash
npx vitest run
```

---

## Security

- Passwords are stored as hashes
- JWT authentication protects API endpoints
- Users can only access their own holidays
- Protected routes prevent unauthorized access

---

## Future Enhancements

- Email settlement summaries
- Demo guest account
- Google authentication
- Deployment
- Improved validation and user feedback
- Responsive mobile design

---

## Project Goals

This project was developed to improve understanding of:

- Full-stack application development
- REST API design
- Database modelling
- Authentication and authorization
- Automated testing
- React and TypeScript development
- Python web development with FastAPI

---

## Author

Natasha Cameron
