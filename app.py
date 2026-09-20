import streamlit as st
import time
import pandas as pd

st.set_page_config(page_title="Student MLOps Portal", layout="wide")

st.title("🎓 Student MLOps Evaluation & Portal (v2.1)")
st.caption("Legacy System Architecture Archive - Class Activity Portal")

# Hidden Admin Panel in Sidebar to simulate failures
st.sidebar.markdown("---")
st.sidebar.subheader("⚙️ System Control (Hidden Admin)")
simulate_alert = st.sidebar.checkbox("Simulate Data Drift / Pipeline Failure")

# Sidebar navigation
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Model Evaluation & Deployment", "Student Run Leaderboard"])

if simulate_alert:
    st.sidebar.error("⚠️ CRITICAL ALERT: Data Drift Detected in Production API Cluster!")

if page == "Dashboard":
    st.subheader("System Architecture Status")
    
    col1, col2, col3 = st.columns(3)
    
    if simulate_alert:
        col1.metric("Active Student Models", "42", "Cluster Degraded", delta_color="inverse")
        col2.metric("Total Automated Deploys", "128", "Deployment Paused", delta_color="inverse")
        col3.metric("System Uptime", "94.2%", "-5.6% Latency Drop", delta_color="inverse")
        
        st.error("🚨 **Data Drift Alert (Production Pipeline)**: The feature distribution for incoming inference data has shifted significantly from the training baseline (P-value < 0.01). Automated fallback to baseline weights has been triggered.")
        
        # Add a quick technical log to show off your MLOps knowledge
        st.code("""
        [WARNING] 2026-09-20 12:55:04 - Drift detector 'KSTest-01' triggered on input features.
        [ACTION]  2026-09-20 12:55:05 - Rolling back live API endpoint traffic to 'student_abrar_final' safe-checkpoint.
        """, language="bash")
    else:
        col1.metric("Active Student Models", "42", "Semester 1 & 2")
        col2.metric("Total Automated Deploys", "128", "Successful CI/CD")
        col3.metric("System Uptime", "99.8%", "Local Cluster")
        
        st.write("### Active Pipelines")
        st.info("💡 Note: The underlying university cluster is archived. Running on local evaluation mode.")

elif page == "Model Evaluation & Deployment":
    st.subheader("Upload and Serve Student Model")
    
    student_name = st.text_input("Enter Student Name / Group ID", placeholder="e.g. Group_3_SecA")
    uploaded_file = st.file_uploader("Upload Trained Model File (.pkl or .h5)", type=["pkl", "h5"])
    
    if st.button("Deploy to Staging Environment"):
        if simulate_alert:
            st.error("❌ CI/CD Pipeline Blocked: Deployment safety constraints failed. System is currently in automated safety lockdown due to active production drift metrics.")
        elif student_name and uploaded_file:
            with st.spinner("Executing GitHub Actions CI/CD Pipeline... Building Docker Image..."):
                time.sleep(2)
                st.success(f"🚀 Success! Model for '{student_name}' containerised via Docker and deployed to evaluation api.")
                st.code(f"Endpoint live at: https://university.edu{student_name.lower()}/predict", language="bash")
        else:
            st.error("Please enter a student identifier and upload a model file.")

elif page == "Student Run Leaderboard":
    st.subheader("Experiment Tracking History (MLflow Logs)")
    
    data = {
        "Run ID": ["run_8a1f", "run_4b9c", "run_2c7e", "run_9d2b", "run_1e6a"],
        "User/Student": ["student_rahul_baseline", "group_4_random_forest", "student_siri_v2", "group_1_logistic", "student_abrar_final"],
        "Framework": ["Scikit-Learn", "Scikit-Learn", "TensorFlow", "Scikit-Learn", "PyTorch"],
        "Accuracy Metric": [0.892, 0.945, 0.912, 0.865, 0.951],
        "Status": ["Finished", "Finished", "Finished", "Finished", "Finished"]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
