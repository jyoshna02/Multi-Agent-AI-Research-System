from agents.research_agent import research_agent
from agents.analysis_agent import analysis_agent
from agents.fact_check_agent import fact_check_agent
from agents.report_agent import report_agent


def orchestrator_agent(topic,claims):

    print("\n========== RESEARCH SYSTEM STARTED ==========")

    # Step 1: Run Research Agent
    print("\n1. Starting Research Agent...")

    research_result = research_agent(topic)

    print("Research completed!")


    # Step 2: Run Analysis Agent
    print("\n2. Starting Analysis Agent...")

    analysis_result = analysis_agent(research_result)

    print("Analysis completely")
    
    # Step 4: Run Fact-Checking Agent
    print("\n3. Starting Fact-Checking Agent...")

    fact_results = fact_check_agent(
        research_result,
        claims
    )

    print("Fact-checking completed!")


    # Step 5: Run Report Writing Agent
    print("\n4. Starting Report Writing Agent...")

    final_report = report_agent(
        research_result,
        analysis_result,
        fact_results
    )

    print("Report generation completed!")


    # Step 6: Save the report
    with open(
        "reports/research_report.md",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(final_report)


    print("\nReport saved successfully!")

    print("\n========== RESEARCH SYSTEM COMPLETED ==========")


    # Return all important results
    return {
        "research": research_result,
        "analysis": analysis_result,
        "fact_check": fact_results,
        "final_report": final_report
    }