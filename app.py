# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt


# csv_file = "C:\\Users\\Deckmount\\Downloads\\DATA0637.TXT"


# st.title(" graph plotter")


# try:
#     df = pd.read_csv(csv_file, names=["timestamp", "unknown1", "unknown2", "unknown3", "unknown4",
#                                     "breath_trend", "spo2", "spo2_2", "body_position", "pulse_trend"])
#     st.write("###  CSV Data:")
#     st.write(df)  
# except Exception as e:
#     st.error(f"Error reading CSV file: {e}")


# if not df.empty:
#     fig, axes = plt.subplots(nrows=5, ncols=1, figsize=(8, 12))

#     columns = ["breath_trend", "spo2", "spo2_2", "body_position", "pulse_trend"]

#     for i, col in enumerate(columns):
#         axes[i].plot(df["timestamp"], df[col], marker='o', linestyle='-', linewidth=0.8, label=col)  
#         axes[i].set_xlabel("Timestamp")
#         axes[i].set_ylabel(col)
#         axes[i].set_title(f"Graph for {col}")
#         axes[i].legend()
#         axes[i].tick_params(axis='x', rotation=45)

#     plt.tight_layout()
#     st.pyplot(fig)




















# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# data = []
# for i in range(4): 
#     data.append([100, 200, 100, 200, 100, 200, 100, 200, 100,200])


# df = pd.DataFrame(data)


# values = df.values.flatten()




# fig, ax = plt.subplots(figsize=(10, 5))


# ax.plot(range(len(values)), values, marker='o', markersize=6, linestyle='-', linewidth=2, color='r', label="Zig-Zag Pattern")


# ax.set_xlabel("Index", fontsize=12)
# ax.set_ylabel("Value", fontsize=12)
# ax.set_title("Zig-Zag Graph for 100-200 Data", fontsize=14, fontweight='bold')


# ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)


# ax.set_xticks(range(0, len(values), 2))
# ax.set_xticklabels(range(0, len(values), 2), rotation=45)


# fig.patch.set_facecolor('whitesmoke')
# ax.set_facecolor('white')


# ax.legend(loc="upper right", fontsize=10)


# st.pyplot(fig)















import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# import streamlit_authenticator as stauth




# credentials = {
#     "user1": {"name": "User One", "password": "$2b$12$eImiTXuWVxfM37uY4JANjQ=="},
#     "user2": {"name": "User Two", "password": "$2b$12$BnPZ5z/PcBv/CkZ0FNMoZ.=="},
# }


# authenticator = stauth.Authenticate(
#     credentials, "streamlit_auth", "abcdef", cookie_expiry_days=30
# )


# name, authentication_status, username = authenticator.login("Login", "main")

# if authentication_status:
#     st.sidebar.success(f"Welcome {name}!")







csv_file = "C:\\Users\\Deckmount\\Downloads\\DATA0637.TXT"

st.title("Graph Plotter ")

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





#     authenticator.logout("Logout", "sidebar")

# elif authentication_status == False:
#     st.error("Incorrect Username/Password")
# elif authentication_status == None:
#     st.warning("Please enter your login details")