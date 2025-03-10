import streamlit as st
import json
import pandas as pd
from io import BytesIO

st.title("HAR File Parser and CSV Exporter")

# File uploader
uploaded_file = st.file_uploader("Upload a HAR file", type=["har"])

if uploaded_file is not None:
    try:
        # Load HAR file
        har_data = json.load(uploaded_file)
        
        # Extract network requests
        entries = har_data.get("log", {}).get("entries", [])

        if not entries:
            st.warning("No network request entries found in the HAR file.")
        else:
            # Extract relevant data
            extracted_data = []
            for entry in entries:
                request = entry.get("request", {})
                response = entry.get("response", {})
                timings = entry.get("timings", {})

                extracted_data.append({
                    "URL": request.get("url", "N/A"),
                    "Method": request.get("method", "N/A"),
                    "Status Code": response.get("status", "N/A"),
                    "Status Text": response.get("statusText", "N/A"),
                    "Request Headers": json.dumps(request.get("headers", [])),
                    "Response Headers": json.dumps(response.get("headers", [])),
                    "Response Time (ms)": timings.get("wait", "N/A"),
                })

            # Convert to DataFrame
            df = pd.DataFrame(extracted_data)

            # Display the data
            st.write("### Parsed HAR Data:")
            st.dataframe(df)

            # Convert to CSV
            csv_buffer = BytesIO()
            df.to_csv(csv_buffer, index=False)
            csv_buffer.seek(0)

            # Provide download button
            st.download_button(
                label="Download CSV",
                data=csv_buffer,
                file_name="parsed_har_data.csv",
                mime="text/csv"
            )
    except Exception as e:
        st.error(f"Error parsing HAR file: {e}")
