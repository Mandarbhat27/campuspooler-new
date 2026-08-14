# CampusPool 🚗🎓

CampusPool is a campus carpooling platform that connects students who are commuting to and from college so they can share rides, split fuel costs, and cut down on solo trips. The project includes a Flask + MongoDB backend, a Flutter mobile app, a React (Vite + TypeScript) web rebuild, and a standalone algorithms demo used for a Design & Analysis of Algorithms (DAA) presentation.

## ✨ Features

- **Ride posting & matching** – riders post upcoming trips; the backend matches nearby passengers using geolocation-based algorithms.
- **Route & fare intelligence** – Dijkstra-based shortest path routing, greedy passenger–rider matching, clustering, and a vehicle-mileage-aware fare calculator.
- **Identity verification** – ID card verification via OCR (`pytesseract`) and selfie-to-ID face matching (`deepface`).
- **Real-time updates** – WebSocket support via Flask-SocketIO for live ride/request events.
- **Auth & profiles** – JWT-based authentication, user profiles, and ride request management.
- **Multi-platform clients** – a Flutter app (Android, iOS, web, desktop) and a lighter React web client, both talking to the same REST API.

## 🗂️ Project Structure

```
campuspooler-new/
├── app/           # Flutter client (Android, iOS, web, Windows, macOS, Linux)
├── backend/       # Flask REST API + Socket.IO server
│   ├── ai/            # OCR verification & face matching
│   ├── algorithms/    # Matching, clustering, Dijkstra, fare calculation
│   ├── middleware/    # Auth middleware
│   ├── models/        # MongoDB models/schemas
│   ├── routes/        # API blueprints (auth, profile, rides, requests, verify)
│   └── app.py         # App entry point
├── daa_demo/      # Standalone script demoing the core algorithms for presentations
└── web-app/       # React + Vite + TypeScript web rebuild of the app
```

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Mobile app | Flutter / Dart |
| Web client | React 19, Vite, TypeScript, React Router, Leaflet |
| Backend | Python, Flask, Flask-SocketIO, Flask-CORS |
| Database | MongoDB (via `pymongo`) |
| Auth | JWT (`PyJWT`), `flask-bcrypt` |
| AI / Verification | `deepface` (face matching), `pytesseract` + `Pillow` (OCR) |
| Algorithms | `networkx`, `numpy` (graph, matching, clustering) |

## 🚀 Getting Started

### Prerequisites

- Python 3.10+ and `pip`
- Node.js 18+ and `npm`
- Flutter SDK (for the mobile app)
- A running MongoDB instance
- `tesseract-ocr` installed on your system (required by `pytesseract`)

### 1. Backend (Flask API)

```bash
cd backend
pip install -r requirements.txt
python app.py
```

The API server starts on `http://127.0.0.1:5000`. Configure environment variables (e.g. `SECRET_KEY`, MongoDB connection string) in a `.env` file inside `backend/`.

Key endpoints are grouped under:
- `/api/auth` – registration & login
- `/api/profile` – user profile management
- `/api/rides` – posting and finding rides
- `/api/requests` – ride requests between riders and passengers
- `/api/verify` – ID/OCR and face-match verification

### 2. Web App (React + Vite)

```bash
cd web-app
npm install
npm run dev
```

The web app expects the backend API to be running at `http://127.0.0.1:5000/api`.

### 3. Algorithms Demo (DAA presentation)

A standalone script that demonstrates the core algorithms (Haversine distance, greedy matching, Dijkstra's shortest path, and fare calculation) and generates presentation-ready output images.

```bash
cd daa_demo
pip install networkx matplotlib numpy
python campuspool_daa.py
```

## 🧠 Algorithms Used

- **Haversine formula** – real-world distance between GPS coordinates
- **Greedy matching** – pairs passengers with nearby riders
- **Dijkstra's algorithm** – shortest-path route finding
- **Clustering** – grouping nearby ride requests
- **Fare calculator** – splits cost based on vehicle mileage and fuel prices

## 📌 Notes

- The React web app is a lighter rebuild of the Flutter app aimed at browser-based use, and it reuses the same backend API.
- Uploaded verification images (ID cards, selfies) are stored under `backend/uploads/`.

## 🤝 Contributing

Issues and pull requests are welcome. Please open an issue to discuss significant changes before submitting a PR.

## 📄 License

No license has been specified for this repository yet. Add a `LICENSE` file to clarify usage terms.
