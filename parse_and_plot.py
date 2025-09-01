import pandas as pd
import matplotlib.pyplot as plt

def main():
    try:
        df = pd.read_csv("traffic.csv")
    except FileNotFoundError:
        print(" Error: 'traffic.csv' not found. Please run capture.sh first.")
        return

    df = df.dropna(subset=["ip.src", "ip.dst"])
    df = df.rename(columns={
        'frame.time_epoch': 'timestamp',
        'ip.src': 'src_ip',
        'ip.dst': 'dst_ip',
        'ip.proto': 'protocol',
        'frame.len': 'length'
    })

    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df['length'] = pd.to_numeric(df['length'], errors='coerce')
    df.set_index('timestamp', inplace=True)

    traffic_over_time = df['length'].resample('10S').sum()
    plt.figure(figsize=(10, 5))
    traffic_over_time.plot()
    plt.title("Traffic Volume Over Time (Bytes per 10 seconds)")
    plt.xlabel("Time")
    plt.ylabel("Bytes")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("traffic_over_time.png")
    plt.show()

    top_src = df['src_ip'].value_counts().head(5)
    plt.figure(figsize=(8, 4))
    top_src.plot(kind='bar', color='skyblue')
    plt.title("Top 5 Source IPs by Packet Count")
    plt.xlabel("Source IP")
    plt.ylabel("Packet Count")
    plt.tight_layout()
    plt.savefig("top_source_ips.png")
    plt.show()

    suspect_ips = df.groupby('src_ip')['dst_ip'].nunique()
    suspect_ips = suspect_ips[suspect_ips > 10]

    if not suspect_ips.empty:
        print("Possible Port Scanning Detected from these IPs:")
        print(suspect_ips)
    else:
        print(" No suspicious scanning behavior detected.")

if __name__ == "__main__":
    main()
