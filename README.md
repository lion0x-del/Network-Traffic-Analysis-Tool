# 🚦 NetCapture Lite – A Simple Network Traffic Analyzer Using TShark

**NetCapture Lite** is a beginner-friendly network traffic analysis tool that captures live network packets using **TShark** and analyzes the data using **Python (Pandas + Matplotlib)**.

It provides visualizations of traffic patterns and includes a simple detection mechanism for potential port scanning attacks.

---

## 📌 Features

- Capture live network traffic with **TShark**
- Save captured data in **CSV format**
- Visualize traffic volume over time
- Identify **top 5 source IP addresses** by packet count
- Detect basic **port scanning behavior**
- Easy to use with simple **Shell and Python scripts**

---

## 🛠️ Technologies Used

| Tool | Purpose |
| --- | --- |
| TShark | Packet capture |
| Bash Script | Automate packet capture |
| Python 3 | Data processing and visualization |
| Pandas | Data manipulation |
| Matplotlib | Plotting graphs |

---

## 📁 Project Structure

NetCaptureLite/
├── [capture.sh](http://capture.sh/) # Script to capture packets using TShark

├── parse_and_plot.py # Python script to analyze and visualize traffic

├── traffic.csv # Captured network traffic data (CSV)

├── traffic_over_time.png # Graph: traffic volume over time

├── top_source_ips.png # Graph: top 5 source IPs

└── [README.md](http://readme.md/) # Project description and instructions

---

## 🚀 Installation & Setup

### 1. Install TShark

TShark is the command-line version of Wireshark used for packet capturing.

**Ubuntu/Debian**

```
sudo apt update
sudo apt install tshark
Fedora

sudo dnf install wireshark-cli
Windows
Download & install Wireshark → <https://www.wireshark.org/download.html>
(TShark is included with Wireshark)

⚠️ Root/Administrator privileges may be required to capture packets.

2. Verify TShark Installation

tshark --version
3. Install Python 3
Check if Python is installed:

python3 --version
If not installed:

Ubuntu/Debian


sudo apt install python3 python3-pip
Windows
Download from → <https://www.python.org/downloads/>

4. Install Python Dependencies

pip3 install pandas matplotlib
(Use pip if pip3 is not available)

5. Configure the Capture Script
Edit capture.sh and set your network interface:

INTERFACE="wlan0"   # Change this to your active network interface
Find your interface:
ip a
6. Make capture.sh Executable

chmod +x capture.sh
7. Capture Network Traffic
Run the capture script with root privileges:

sudo ./capture.sh
(Default: captures 100 packets → saves to traffic.csv)

8. Analyze and Visualize Traffic

python3 parse_and_plot.py
This generates:

traffic_over_time.png → traffic volume over time graph

top_source_ips.png → top 5 source IPs graph

Alerts if potential port scanning is detected

▶️ Usage Summary

sudo ./capture.sh
python3 parse_and_plot.py
📊 Sample Output
📈 Graphs saved as .png files

⚠️ Alerts shown in terminal if suspicious activity is detected

⚠️ Important Notes
Use this tool only on networks where you have permission

Packet capturing requires root/administrator privileges

Results depend on current network activity

🚨 Basic Threat Detection
The tool flags source IPs that connect to more than 10 unique destination IPs as possible port scanners.

💡 Future Improvements
Real-time monitoring dashboard (e.g., Streamlit)

GeoIP mapping of IP addresses

Automated alerts (email/SMS)

Database storage for captured logs

Customizable filters & capture duration
```
