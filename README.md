🚦 NetCapture Lite – A Simple Network Traffic Analyzer Using TShark
NetCapture Lite is a beginner-friendly network traffic analysis tool that captures live network packets using TShark and analyzes the data using Python (Pandas and Matplotlib). It provides visualizations of traffic patterns and includes a simple detection mechanism for potential port scanning attacks.

📌 Features
Capture live network traffic with TShark
Save captured data in CSV format
Visualize traffic volume over time
Identify top 5 source IP addresses by packet count
Detect basic port scanning behavior
Easy to use with simple shell and Python scripts
🛠️ Technologies Used
Tool	Purpose
TShark	Packet capture
Bash Script	Automate packet capture
Python 3	Data processing and visualization
Pandas	Data manipulation
Matplotlib	Plotting graphs
📁 Project Structure
NetCaptureLite/ 
├── capture.sh # Script to capture packets using TShark
├── parse_and_plot.py # Python script to analyze and visualize traffic 
├── traffic.csv # Captured network traffic data (CSV) 
├── traffic_over_time.png # Generated graph: traffic volume over time 
├── top_source_ips.png # Generated graph: top 5 source IPs 
├── README.md # Project description and instructions

yaml Copy code

🚀 Installation & Setup
Follow the steps below to set up the environment and run the tool:

1. Install TShark
TShark is the command-line version of Wireshark used for packet capturing.

Ubuntu/Debian:
sudo apt update
sudo apt install tshark
Fedora:


sudo dnf install wireshark-cli
Windows:

Download and install Wireshark from https://www.wireshark.org/download.html
TShark is included with Wireshark.

Note: You may need administrative/root privileges to capture packets.

2. Verify TShark Installation
Run:


tshark --version
You should see version info printed if installed correctly.

3. Install Python 3
Make sure Python 3 is installed:

python3 --version
If not installed:

Ubuntu/Debian:


sudo apt install python3 python3-pip
Windows:
Download and install from https://www.python.org/downloads/

4. Install Python Dependencies
Install the required Python libraries:


pip3 install pandas matplotlib
or if pip3 is not recognized, try:


pip install pandas matplotlib
5. Configure the Capture Script
Edit capture.sh and set your network interface:


INTERFACE="wlan0"  # Change this to your active network interface
To find your network interface, run:


ip a
6. Make capture.sh Executable

chmod +x capture.sh
7. Capture Network Traffic
Run the capture script with root privileges (required for capturing network packets):


sudo ./capture.sh
This captures 100 packets and saves the data to traffic.csv.

8. Analyze and Visualize Traffic
Run the Python analysis script:


python3 parse_and_plot.py
This generates:

traffic_over_time.png (traffic volume over time graph)

top_source_ips.png (top 5 source IPs graph)

Prints alerts if potential port scanning is detected.

▶️ Usage Summary

sudo ./capture.sh
python3 parse_and_plot.py
📊 Sample Output


⚠️ Important Notes
Use this tool only on networks where you have permission to capture traffic.

Capturing packets requires administrative privileges.

Packet capture results depend on your network activity.

🚨 Basic Threat Detection
The tool flags source IPs that communicate with more than 10 unique destination IPs as possible port scanners.

💡 Future Improvements
Real-time monitoring dashboard (e.g., using Streamlit)

GeoIP mapping of IP addresses

Automated alerts (email/SMS)

Database storage for captured logs

Customizable filters and capture duration
