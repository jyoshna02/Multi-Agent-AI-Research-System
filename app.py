import streamlit as st

from agents.orchestrator_agent import orchestrator_agent

from tools.pdf_generator import generate_pdf

from tools.research_history import (
    create_table,
    save_research,
    get_all_reports,
    get_report_by_id
)


# ----------------------------------
# PAGE CONFIGURATION
# ----------------------------------

st.set_page_config(
    page_title="Multi-Agent AI Research System",
    page_icon="🔍",
    layout="wide"
)


# ----------------------------------
# DATABASE INITIALIZATION
# ----------------------------------

create_table()


# ----------------------------------
# CUSTOM DASHBOARD STYLING
# ----------------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #172B3A, #203B50);
    color: #EAF4FF;
}

h1 {
    color: #65C7E8;
    font-weight: 700;
}

h2, h3 {
    color: #EAF4FF;
}

.stTextInput input,
.stTextArea textarea {
    background-color: #243B4D;
    color: white;
    border-radius: 8px;
}

.stButton button {
    background-color: #2589BD;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 10px 24px;
    font-weight: bold;
}

.stButton button:hover {
    background-color: #35C6B4;
    color: #172B3A;
}

[data-testid="stMetric"] {
    background-color: #243B4D;
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #426176;
}

</style>
""", unsafe_allow_html=True)


# ----------------------------------
# MAIN HEADING
# ----------------------------------

st.title("🔍 Multi-Agent AI Research System")

st.write(
    "An AI-powered system that researches, analyses "
    "and prepares structured research reports."
)

st.divider()


# ----------------------------------
# RESEARCH TOPIC INPUT
# ----------------------------------

st.subheader("Enter Your Research Topic")

topic = st.text_input(
    "What would you like to research?",
    placeholder="Example: How is AI changing Data Analytics?"
)


# ----------------------------------
# CUSTOM CLAIM INPUT
# ----------------------------------

st.subheader("Enter Claims for Fact-Checking")

st.write(
    "Enter one or more claims below. "
    "Write each claim on a separate line."
)

claims_input = st.text_area(
    "Claims to verify",
    placeholder=(
        "Example:\n"
        "AI helps automate data analysis\n"
        "Machine learning improves predictions\n"
        "AI completely replaces data analysts"
    ),
    height=120
)


# ----------------------------------
# START RESEARCH
# ----------------------------------

if st.button("Start Research"):

    if not topic.strip():

        st.warning("Please enter a research topic.")

    else:

        # Convert user claims into a Python list
        claims = [
            claim.strip()
            for claim in claims_input.splitlines()
            if claim.strip()
        ]

        try:

            with st.spinner("Research agents are working..."):

                result = orchestrator_agent(topic, claims)

            if not isinstance(result, dict):

                st.error(
                    "Invalid response from Orchestrator Agent."
                )

            else:

                final_report = result.get("final_report")

                analysis = result.get("analysis", {})

                research_data = result.get("research", {})

                fact_check_results = result.get("fact_check", [])

                if not final_report:

                    st.error(
                        "Final research report was not generated."
                    )

                else:

                    # Save research in database
                    save_research(topic, final_report)

                    st.success(
                        "Research completed successfully!"
                    )

                    # ----------------------------------
                    # DASHBOARD METRICS
                    # ----------------------------------

                    sources = (
                        research_data.get("sources", [])
                        if isinstance(research_data, dict)
                        else []
                    )

                    keyword_counts = (
                        analysis.get("keyword_counts", {})
                        if isinstance(analysis, dict)
                        else {}
                    )

                    st.subheader("Research Dashboard")

                    col1, col2, col3 = st.columns(3)

                    with col1:

                        st.metric(
                            "Sources Found",
                            len(sources)
                        )

                    with col2:

                        st.metric(
                            "Keywords Analyzed",
                            len(keyword_counts)
                        )

                    with col3:

                        st.metric(
                            "Total Keyword Matches",
                            sum(keyword_counts.values())
                        )

                    # ----------------------------------
                    # AGENT EXECUTION STATUS
                    # ----------------------------------

                    st.subheader("AI Agent Execution Status")

                    agent_col1, agent_col2, agent_col3, agent_col4 = (
                        st.columns(4)
                    )

                    with agent_col1:
                        st.success("Research Agent ✓")

                    with agent_col2:
                        st.success("Analysis Agent ✓")

                    with agent_col3:
                        st.success("Fact-Checking Agent ✓")

                    with agent_col4:
                        st.success("Report Agent ✓")

                    # ----------------------------------
                    # FINAL RESEARCH REPORT
                    # ----------------------------------

                    st.subheader("Final Research Report")

                    st.markdown(final_report)

                    # ----------------------------------
                    # FACT-CHECKING RESULTS
                    # ----------------------------------

                    st.subheader("Fact-Checking Results")

                    if fact_check_results:

                        for index, item in enumerate(
                            fact_check_results,
                            start=1
                        ):

                            with st.expander(
                                f"Claim {index}: {item['claim']}"
                            ):

                                st.write(
                                    "**Status:**",
                                    item["status"]
                                )

                                st.write(
                                    "**Keyword Match:**",
                                    f"{item['match_percentage']}%"
                                )

                                st.write(
                                    "**Matched Words:**",
                                    ", ".join(item["matched_words"])
                                    if item["matched_words"]
                                    else "No matching words"
                                )

                                st.write(
                                    "**Matching Source Numbers:**",
                                    ", ".join(
                                        map(
                                            str,
                                            item.get("matched_sources", [])
                                        )
                                    )
                                    if item.get("matched_sources")
                                    else "No matching sources"
                                )

                    else:

                        st.info(
                            "No claims were entered for fact-checking."
                        )

                    # ----------------------------------
                    # ANALYSIS RESULTS
                    # ----------------------------------

                    st.subheader("Analysis Results")

                    if keyword_counts:

                        for word, count in keyword_counts.items():

                            st.write(
                                f"**{word.title()}**: "
                                f"{count} occurrences"
                            )

                    else:

                        st.info(
                            "No keyword analysis results available."
                        )

                    # ----------------------------------
                    # MARKDOWN DOWNLOAD
                    # ----------------------------------

                    st.download_button(
                        label="Download Research Report",
                        data=final_report,
                        file_name="research_report.md",
                        mime="text/markdown"
                    )

                    # ----------------------------------
                    # PDF DOWNLOAD
                    # ----------------------------------

                    pdf_file = generate_pdf(
                        final_report,
                        topic
                    )

                    st.download_button(
                        label="Download PDF Report",
                        data=pdf_file,
                        file_name="research_report.pdf",
                        mime="application/pdf"
                    )

        except Exception as e:

            st.error(
                "Something went wrong during research."
            )

            st.write("Error details:", str(e))


# ----------------------------------
# RESEARCH HISTORY SIDEBAR
# ----------------------------------

st.sidebar.title("📚 Research History")

reports = get_all_reports()

if reports:

    report_ids = [
        report[0]
        for report in reports
    ]

    selected_id = st.sidebar.selectbox(
        "Select Previous Research",
        report_ids,
        format_func=lambda report_id: next(
            f"{r[1]} ({r[2]})"
            for r in reports
            if r[0] == report_id
        )
    )

    selected_report = get_report_by_id(selected_id)

    if selected_report:

        with st.sidebar.expander("View Saved Report"):

            st.write("Topic:", selected_report[1])

            st.write("Date:", selected_report[2])

            st.markdown(selected_report[3])

else:

    st.sidebar.info(
        "No previous research reports found."
    )