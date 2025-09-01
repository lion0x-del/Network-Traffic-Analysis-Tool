#!/bin/bash

echo "🔹 Starting packet capture using TShark..."

INTERFACE="wlan0"
OUTPUT_FILE="traffic.csv"
PACKET_COUNT=100

tshark -i $INTERFACE -c $PACKET_COUNT \
    -T fields \
    -e frame.time_epoch \
    -e ip.src \
    -e ip.dst \
    -e ip.proto \
    -e frame.len \
    -E header=y -E separator=, -E quote=d -E occurrence=f > $OUTPUT_FILE

if [ -f "$OUTPUT_FILE" ]; then
    echo "✅ Capture complete. Data saved to $OUTPUT_FILE"
else
    echo "❌ Error: Failed to save captured data."
fi
