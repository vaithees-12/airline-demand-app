# ✈️ Airline Demand Dashboard

A real-time dashboard to visualize global flight demand using live OpenSky Network data. Built with **Flask (Python)** for the backend and **Chart.js + HTML/CSS** for the frontend, hosted with **GitHub Pages** and **Render**.

---

## 🌐 Live Demo

- **Frontend (GitHub Pages):** [🌍 View Dashboard](https://vaithees-12.github.io/airline-demand-app/)
- **Backend API (Render):** [🚀 Live API](https://airline-backend-m39q.onrender.com)

---

## 🧩 Features

✅ Real-time popular airline routes  
✅ Simulated ticket price trends  
✅ Top countries by demand (based on live origin_country counts)  
✅ High-demand hours of the day  
✅ Clean & responsive design with Chart.js visualizations  

---

## ⚙️ Tech Stack

| Layer       | Technology                      |
|------------|----------------------------------|
| Frontend    | HTML, CSS, Chart.js              |
| Backend     | Python (Flask), Pandas, Requests |
| API Source  | [OpenSky Network](https://opensky-network.org/) |
| Hosting     | GitHub Pages (Frontend), Render (Backend) |

---

## 📸 Screenshot

![Dashboard Screenshot](![Screenshot (67)](https://github.com/user-attachments/assets/37382caf-827b-4fd7-b331-b4683660fbf1)
)


---

## 🔧 Setup Instructions

### Backend (Flask API)

```bash
# Clone repo & go to directory
git clone https://github.com/vaithees-12/airline-demand-app.git
cd airline-demand-app

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run server
python app.py
