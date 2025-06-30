import streamlit as st
from parser import analyze_logs
from utils.report_generator import generate_pdf_report

st.set_page_config(page_title="Log Analyzer", layout="centered")

st.title("🔍 Forensic Log Format Analyzer (NeoTraceOS)")
st.write("Upload or paste custom logs to analyze their format and download a report.")

log_input = st.text_area("Paste your log sample here:", height=300)
uploaded_file = st.file_uploader("OR Upload a log file", type=["txt", "log", "vlog"])

if st.button("Analyze Logs"):
    log_data = ""
    if uploaded_file is not None:
        log_data = uploaded_file.read().decode("utf-8")
    elif log_input.strip():
        log_data = log_input
    else:
        st.warning("Please provide logs either by pasting or uploading.")

    if log_data:
        lines = log_data.strip().split('\n')
        parsed_logs, field_stats, error_lines = analyze_logs(lines)

        if not parsed_logs:
            st.error("No valid log entries were parsed. Please check the format.")
        else:
            st.success("Log format successfully analyzed.")
            st.subheader("🧾 Field Summary")
            st.json(field_stats)

            st.subheader("🔍 Sample Parsed Logs")
            for log in parsed_logs[:5]:
                st.json(log)

            if error_lines:
                st.warning(f"{len(error_lines)} lines could not be parsed.")
                with st.expander("📄 Show malformed log lines"):
                    for i, err in enumerate(error_lines, 1):
                        st.markdown(f"**{i}.** `{err}`")

            with st.spinner("Generating PDF report..."):
                report_path = generate_pdf_report(parsed_logs, field_stats, file_name=uploaded_file.name if uploaded_file else "Pasted Logs")
                with open(report_path, "rb") as f:
                    st.download_button("📄 Download Report", f, file_name="log_analysis_report.pdf")
