











import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


csv_file = "C:\\Users\\Deckmount\\Downloads\\DATA0637.TXT"

st.title("Graph Plotter with Noise Reduction")

try:
    df = pd.read_csv(csv_file, names=["timestamp", "unknown1", "unknown2", "unknown3", "unknown4",
                                    "breath_trend", "spo2", "spo2_2", "body_position", "pulse_trend"])
    st.write("### CSV Data:")
    st.write(df)
except Exception as e:
    st.error(f"Error reading CSV file: {e}")

def moving_average(series, window_size=5):
    return series.rolling(window=window_size, min_periods=1).mean()


if not df.empty:
    fig, axes = plt.subplots(nrows=5, ncols=1, figsize=(8, 12))

    columns = ["breath_trend", "spo2", "spo2_2", "body_position", "pulse_trend"]

    for i, col in enumerate(columns):
        smooth_data = moving_average(df[col], window_size=10) 
        axes[i].plot(df["timestamp"], smooth_data, linewidth=0.2, label=f"Smoothed {col}")
        axes[i].set_xlabel("Timestamp")
        axes[i].set_ylabel(col)
        axes[i].set_title(f"Graph for {col} (Smoothed)")
        axes[i].legend()
        axes[i].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    st.pyplot(fig)
