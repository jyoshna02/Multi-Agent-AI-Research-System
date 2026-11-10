def analysis_agent(research_result):

    topic = research_result["topic"]
    sources = research_result["sources"]

    # Collect content from all sources
    all_content = []

    for source in sources:
        content = source.get("content", "")

        if content:
            all_content.append(content)

    # Combine all source content
    combined_content = " ".join(all_content)

    total_sources = len(sources)

    # Define individual keywords
    keywords = [
        "artificial intelligence",
        "machine learning",
        "automation",
        "data analytics",
        "business"
    ]

    # Count each keyword
    keyword_counts = {}

    for word in keywords:
        count = combined_content.lower().count(word.lower())
        keyword_counts[word] = count

    # Prepare analysis result
    analysis_result = {
        "topic": topic,
        "total_sources": total_sources,
        "keyword_counts": keyword_counts,
        "source_content": combined_content
    }

    return analysis_result