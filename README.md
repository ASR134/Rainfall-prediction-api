# 🌧️ Rainfall Prediction API

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

A machine learning-powered REST API that predicts whether it will rain based on weather parameters. Built with **FastAPI** and a trained ML model, this API can be easily integrated with any frontend application (Streamlit, React, Vue, mobile apps, etc.).

---

## 🚀 Features

- 🔮 **Intelligent Rain Prediction** – Binary classification (Rain / No Rain)
- ⚡ **FastAPI Backend** – High-performance async API with automatic Swagger UI
- 🧠 **Server-Side Feature Engineering** – Automatically computes derived features (e.g., `temp_range`)
- 🧪 **Interactive Testing** – Built-in Swagger documentation at `/docs`
- 🌐 **Cloud-Ready** – Deploy to Render, Railway, AWS, or any cloud platform
- 📊 **Production-Ready** – Optimized model loading and efficient inference

---

## 🧠 Model Inputs

The API expects the following weather parameters:

| Parameter       | Type  | Description                              | Example |
|-----------------|-------|------------------------------------------|---------|
| `pressure`      | float | Atmospheric pressure (hPa)               | 1012.5  |
| `temperature`   | float | Average temperature (°C)                 | 26.0    |
| `humidity`      | float | Relative humidity (%)                    | 70.0    |
| `cloud`         | float | Cloud cover (%)                          | 60.0    |
| `sunshine`      | float | Hours of sunshine                        | 5.0     |
| `winddirection` | float | Wind direction (0–360°, 0 = North)       | 180.0   |
| `windspeed`     | float | Wind speed (km/h)                        | 10.0    |
| `max_temp`      | float | Maximum temperature of the day (°C)      | 30.0    |
| `min_temp`      | float | Minimum temperature of the day (°C)      | 22.0    |

> ℹ️ **Note:** `temp_range = max_temp - min_temp` is computed automatically by the API during inference.

---

## 📦 Project Structure

```
rainfall-api/
│
├── main.py                  # FastAPI application
├── rainfall_model.pkl       # Trained ML model
├── requirements.txt         # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Git ignore rules
└── Dockerfile              # (Optional) Docker configuration
```

---

## 🛠️ Setup & Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/rainfall-api.git
cd rainfall-api
```

### 2️⃣ Create a Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the API

```bash
uvicorn main:app --reload
```

The API will start at `http://127.0.0.1:8000`

### 5️⃣ Open Swagger UI

Visit the interactive API documentation:

👉 **http://127.0.0.1:8000/docs**

---

## 🔌 API Endpoints

### **POST** `/predict`

Predicts whether it will rain based on input weather parameters.

#### Request Body (JSON)

```json
{
  "pressure": 1012.5,
  "temperature": 26.0,
  "humidity": 70.0,
  "cloud": 60.0,
  "sunshine": 5.0,
  "winddirection": 180.0,
  "windspeed": 10.0,
  "max_temp": 30.0,
  "min_temp": 22.0
}
```

#### Response

```json
{
  "prediction": "Rain"
}
```

or

```json
{
  "prediction": "No Rain"
}
```

### **GET** `/`

Health check endpoint.

#### Response

```json
{
  "message": "Rainfall Prediction API is running!"
}
```

---

## 🧪 Testing the API

### Using cURL

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "pressure": 1012.5,
    "temperature": 26.0,
    "humidity": 70.0,
    "cloud": 60.0,
    "sunshine": 5.0,
    "winddirection": 180.0,
    "windspeed": 10.0,
    "max_temp": 30.0,
    "min_temp": 22.0
  }'
```

### Using Python `requests`

```python
import requests

url = "http://127.0.0.1:8000/predict"
data = {
    "pressure": 1012.5,
    "temperature": 26.0,
    "humidity": 70.0,
    "cloud": 60.0,
    "sunshine": 5.0,
    "winddirection": 180.0,
    "windspeed": 10.0,
    "max_temp": 30.0,
    "min_temp": 22.0
}

response = requests.post(url, json=data)
print(response.json())
```

---

## ☁️ Deployment

### Deploy to Render

1. Push your code to GitHub
2. Create a new **Web Service** on [Render](https://render.com)
3. Connect your GitHub repository
4. Set the following:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Deploy! 🚀

### Deploy to Railway

1. Install the [Railway CLI](https://docs.railway.app/develop/cli)
2. Run:
   ```bash
   railway login
   railway init
   railway up
   ```

### Deploy with Docker

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:

```bash
docker build -t rainfall-api .
docker run -p 8000:8000 rainfall-api
```

---

## 🧠 How the Model Was Trained

The rainfall prediction model was trained using historical weather data with the following approach:

1. **Data Collection:** Weather observations including temperature, humidity, pressure, wind metrics, and rainfall records
2. **Feature Engineering:** 
   - Created `temp_range` feature (max_temp - min_temp)
   - Normalized numerical features
   - Handled missing values and outliers
3. **Model Selection:** Tested multiple algorithms (Logistic Regression, Random Forest, XGBoost)
4. **Training:** Used scikit-learn with cross-validation for robust performance
5. **Evaluation:** Achieved strong performance on validation set using metrics like accuracy, precision, and recall
6. **Serialization:** Saved the trained model using `joblib` for efficient loading

> 💡 **Future Improvements:** Plans to integrate time-series features and ensemble methods for better accuracy.

---

## 🧰 Tech Stack

- **[FastAPI](https://fastapi.tiangolo.com/)** – Modern, fast web framework for building APIs
- **[scikit-learn](https://scikit-learn.org/)** – Machine learning library for model training
- **[pandas](https://pandas.pydata.org/)** – Data manipulation and preprocessing
- **[joblib](https://joblib.readthedocs.io/)** – Model serialization
- **[uvicorn](https://www.uvicorn.org/)** – ASGI server for production deployment

---

## 📝 Requirements

```txt
fastapi==0.104.1
uvicorn==0.24.0
scikit-learn==1.3.2
pandas==2.1.3
joblib==1.3.2
pydantic==2.5.0
```

---

## 📌 Important Notes

- ✅ Ensure feature names and order match the training data exactly
- ✅ The model is loaded once at startup for optimal performance
- ✅ API is designed to be consumed by any frontend or mobile application
- ✅ CORS is enabled for cross-origin requests (configure as needed)

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙌 Author

**Aman Rawat**

- 💼 [LinkedIn](https://www.linkedin.com/in/aman-singh-rawat-758160328/)
- 🐙 [GitHub](https://github.com/ASR134)
- 📧 Email: amansinghrawat992752@gmail.com

---

## 🌟 Support

If you found this project helpful, please give it a ⭐️!

---

<div align="center">

**Built with ❤️ using FastAPI and Machine Learning**

</div>
