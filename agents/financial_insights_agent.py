def derive_business_insights_from_financial_data(financial_data: dict) -> dict:
    """
    Analyzes aggregated financial data from existing financial agents
    and provides deeper insights without reusing the Gemini API.
    """

    # Extract data from financial agents
    product_sales = financial_data.get("product_sales", {})
    subscription_service = financial_data.get("subscription_service", {})
    development_cost = financial_data.get("development_cost", {})
    marketing_cost = financial_data.get("marketing_cost", {})
    operations_cost = financial_data.get("operations_cost", {})

    # Calculate key metrics
    total_revenue = (
        product_sales.get("projected_revenue", 0)
        + subscription_service.get("recurring_revenue", 0)
    )
    total_cost = (
        development_cost.get("total_budget", 0)
        + marketing_cost.get("total_spent", 0)
        + operations_cost.get("scaled_cost", 0)
    )
    profit = total_revenue - total_cost

    # Generate insights based on derived metrics
    insights = {
        "profit_margin": round((profit / total_revenue) * 100, 2) if total_revenue > 0 else 0,
        "breakeven_analysis": "Breakeven achieved" if profit > 0 else "Breakeven not achieved",
        "marketing_efficiency": round(
            marketing_cost.get("total_spent", 0) / total_revenue * 100, 2
        )
        if total_revenue > 0
        else "N/A",
        "scalability_factor": round(
            (total_revenue / operations_cost.get("scaled_cost", 1)), 2
        )
        if operations_cost.get("scaled_cost", 0) > 0
        else "N/A",
    }

    # Provide Recommendations
    recommendations = []

    if insights["profit_margin"] < 20:
        recommendations.append("Consider revising product pricing or reducing costs.")
    if insights["marketing_efficiency"] > 30:
        recommendations.append("Optimize marketing strategy to reduce CPA.")
    if insights["breakeven_analysis"] == "Breakeven not achieved":
        recommendations.append("Focus on increasing revenue streams or cutting expenses.")
    if insights["scalability_factor"] < 1.5:
        recommendations.append("Evaluate operational scalability for long-term growth.")

    return {
        "financial_overview": {
            "total_revenue": total_revenue,
            "total_cost": total_cost,
            "profit": profit,
            "insights": insights,
        },
        "recommendations": recommendations,
    }
