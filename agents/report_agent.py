def report_agent(research_result, analysis_result, fact_results):

    # Get the research topic
    topic = research_result["topic"]

    # Get the number of sources
    total_sources = analysis_result["total_sources"]

    # Start building the report
    report = f"""
# AI RESEARCH REPORT

## Research Topic
{topic}

## 1. Executive Summary

This report presents information collected from
{total_sources} web search sources.

The research was processed using our Research,
Analysis and Fact-Checking agents.

## 2. Research Findings

"""

    # Add collected source information
    for index, source in enumerate(
        research_result["sources"], start=1
    ):

        report += f"""
### Source {index}: {source["title"]}

{source["content"]}

Source URL: {source["url"]}

"""

    # Add analysis results
    report += """
## 3. Analysis Results

"""

    for word, count in analysis_result["keyword_counts"].items():

        report += f"- **{word.title()}**: {count} occurrences\n"

    # Add fact-checking results
    report += """
## 4. Fact-Checking Results

"""

    for result in fact_results:

        report += f"""
### Claim: {result["claim"]}

- Status: {result["status"]}
- Matching percentage: {result["match_percentage"]}%
- Matched words: {", ".join(result["matched_words"])}

"""

    # Add conclusion
    report += """
## 5. Conclusion

This report summarizes the collected research,
basic keyword analysis and preliminary claim screening.

The findings should be reviewed against the original
sources before making important decisions.
"""

    # Return the completed report
    return report