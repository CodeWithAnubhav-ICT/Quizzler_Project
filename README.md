# 🧠 Quizzler: Dynamic Trivia Interface
### Day 34: #100DaysOfCode | Python Development Portfolio

Quizzler is a production-grade GUI application that delivers a seamless trivia experience by orchestrating real-time data from the Open Trivia Database. The project demonstrates advanced concepts in **Object-Oriented Programming (OOP)**, **API integration**, and **Asynchronous UI State Management**.

---

## 🛠️ Technical Stack
| Category | Tools |
| :--- | :--- |
| **Language** | Python 3.11+ |
| **Library** | Tkinter (GUI), Requests (API) |
| **Architecture** | Model-View-Controller (MVC) |
| **Data Source** | Open Trivia Database (REST API) |

---

## 🔐 Key Features & Logic

### 🔹 MVC Architecture
The project is strictly organized into four logical layers to ensure scalability and maintainability:
* **Model (`question_model.py`):** Defines the data structure for trivia objects.
* **View (`ui.py`):** Manages the Tkinter root window, canvas rendering, and user interactions.
* **Controller (`quiz_brain.py` & `main.py`):** Coordinates the application lifecycle, score tracking, and logic flow.

### 🔹 Defensive UI Design
To ensure a robust user experience, the application implements **State-Driven Button Logic**. When a user submits an answer, both interactive buttons are immediately disabled during the feedback phase (background color change). This prevents "rapid-click" exploits and ensures data integrity before the next question is loaded.

### 🔹 HTML Entity Normalization
Leverages the `html` library to perform server-side unescaping of strings. This ensures that questions containing special characters (e.g., `&quot;`, `&#039;`) are rendered correctly in the GUI.

### 🔹 Asynchronous Feedback Loop
Uses the `.after()` method in Tkinter to manage non-blocking delays. This allows the UI to remain responsive while providing visual feedback (Green/Red canvas flashes) without freezing the main application thread.

---

## 🚀 Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/CodeWithAnubhav-ICT/Quizzler-App.git](https://github.com/CodeWithAnubhav-ICT/Quizzler-App.git)
