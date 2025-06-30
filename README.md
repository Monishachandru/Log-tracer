# 🔍 Forensic Log Parser & Visualizer

**Forensic Log Parser** is a Streamlit-based interactive tool for parsing, analyzing, and visualizing log data. It supports log formats such as `.txt`, `.log`, and `.vlog`, and includes features like anomaly detection, event timelines, and IP geo-location tracking.

---

## 📦 Features

* ✅ Upload and parse multiple log files
* 📋 Auto-extracts fields like timestamps, user IDs, IPs, file access, and event types
* 📈 Interactive timeline visualization of events
* ⚠️ Anomaly detection using:

  * Z-score statistics
  * Isolation Forest (machine learning)
* 🌍 Geo-location mapping of IP addresses
* 📁 Export parsed logs in CSV, JSON, or TXT formats
* 💡 Clean UI with themed reports, summary stats, and download options

---

## 🚀 Getting Started

### 🔧 Prerequisites

Ensure you have the following installed:

* Python 3.7+
* pip

### 📥 Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/forensic-log-parser.git
   cd forensic-log-parser
   ```

2. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```

### ▶️ Run the App

```bash
streamlit run forensic_parser.py
```

---

## 📂 Supported Log Format

Each log line should contain fields such as:

```text
[ts:timestamp] EVNT:XR-xxx usr:username IP:ip_address =>/file_path pidxxxx
```

Example:

```text
[ts:1717381287] EVNT:XR-LOGIN usr:john_doe IP:192.168.1.1 =>/login pid2345
```

---

## 📊 Visualization Tabs

1. **Summary Report:** Overview of log entries by user, IP, and event type.
2. **Event Timeline:** Time-series of events grouped in 10-second bins.
3. **Alerts & Anomalies:** Detects suspicious activity using statistical and machine learning models.
4. **Geo-location:** Maps IP addresses to geographic locations using external API.

---

## 📤 Export Options

Parsed data can be downloaded in:

* JSON
* CSV
* Plain Text (TXT)

---

## 🧠 Technologies Used

* Python
* Streamlit
* Pandas, Plotly, Matplotlib, Scikit-learn, SciPy
* Requests (for IP resolution)

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for more information.

---

## 🙌 Acknowledgments

Developed as part of a digital forensics and log analysis toolkit. Suitable for academic, investigative, or system monitoring use.

