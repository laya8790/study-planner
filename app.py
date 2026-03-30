import streamlit as st
import pandas as pd

st.set_page_config(page_title="Study Planner", layout="centered")

st.title("📚 Student Study Planner & Productivity Tracker")

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Add Task
st.subheader("➕ Add New Task")
task = st.text_input("Enter task")
priority = st.selectbox("Select Priority", ["High", "Medium", "Low"])

if st.button("Add Task"):
    if task != "":
        st.session_state.tasks.append(
            {"Task": task, "Priority": priority, "Status": "Pending"}
        )
        st.success("Task Added Successfully!")

# Display Tasks
st.subheader("📋 Your Tasks")

if len(st.session_state.tasks) > 0:
    df = pd.DataFrame(st.session_state.tasks)

    for i, row in df.iterrows():
        col1, col2, col3 = st.columns([4,2,2])

        col1.write(f"**{row['Task']}** ({row['Priority']})")
        
        if col2.button("Complete", key=f"complete_{i}"):
            st.session_state.tasks[i]["Status"] = "Completed"

        if col3.button("Delete", key=f"delete_{i}"):
            st.session_state.tasks.pop(i)
            st.experimental_rerun()

    # Progress Chart
    st.subheader("📊 Productivity Overview")
    completed = df[df["Status"] == "Completed"].shape[0]
    pending = df[df["Status"] == "Pending"].shape[0]

    chart_data = pd.DataFrame({
        "Status": ["Completed", "Pending"],
        "Count": [completed, pending]
    })

    st.bar_chart(chart_data.set_index("Status"))

else:
    st.info("No tasks added yet!")