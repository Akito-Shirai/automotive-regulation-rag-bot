
import os
import sys

import streamlit as st

from rag.rag_pipeline import run_pipeline

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
st.title("RAG-based FAQ Bot for Automotive Regulations")
query = st.text_input("Enter part name and symptom (e.g., 'brake pedal soft')")

if st.button("Ask"):
    if query:
        with st.spinner("Generating answer..."):
            answer = run_pipeline(query, "data/example_regulation.pdf")
            st.markdown("### Answer")
            st.write(answer)
    else:
        st.warning("Please enter a question.")
