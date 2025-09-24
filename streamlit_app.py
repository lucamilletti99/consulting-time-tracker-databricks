import streamlit as st
import requests
import os

st.title("🕐 Consulting Time & Expense Tracker")

# API base URL
API_BASE = f"http://localhost:{os.environ.get('DATABRICKS_APP_PORT', 8000)}"

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Dashboard", "Time Entry", "Expenses", "Reports"])

if page == "Dashboard":
    st.header("📊 Dashboard")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Hours This Week", "32.5")
    with col2:
        st.metric("Active Projects", "5")
    with col3:
        st.metric("Pending Approvals", "3")

elif page == "Time Entry":
    st.header("⏰ Time Entry")
    
    with st.form("time_entry"):
        project = st.selectbox("Project", ["Project A", "Project B", "Project C"])
        task = st.selectbox("Task", ["Development", "Testing", "Documentation"])
        hours = st.number_input("Hours", min_value=0.1, max_value=24.0, step=0.1)
        description = st.text_area("Description")
        
        submitted = st.form_submit_button("Submit Time Entry")
        if submitted:
            st.success("Time entry submitted successfully!")

elif page == "Expenses":
    st.header("💰 Expense Submission")
    
    with st.form("expense_form"):
        expense_type = st.selectbox("Type", ["Travel", "Meals", "Software", "Other"])
        amount = st.number_input("Amount ($)", min_value=0.01, step=0.01)
        project = st.selectbox("Project", ["Project A", "Project B", "Project C"])
        description = st.text_area("Description")
        
        submitted = st.form_submit_button("Submit Expense")
        if submitted:
            st.success("Expense submitted for approval!")

elif page == "Reports":
    st.header("📈 Reports & Analytics")
    
    st.subheader("Time Tracking Summary")
    # Placeholder chart
    import pandas as pd
    
    data = pd.DataFrame({
        'Date': ['2025-09-20', '2025-09-21', '2025-09-22', '2025-09-23'],
        'Hours': [8, 7.5, 8, 6]
    })
    
    st.line_chart(data.set_index('Date'))
