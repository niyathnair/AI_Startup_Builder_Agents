from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from agents.input_agent import get_startup_idea
from agents.market_research_agent import analyze_market_trends
from agents.brand_identity_agent import generate_brand_name_and_tagline
from agents.business_model_agent import create_business_model
from agents.financial_agents import (
    optimize_product_sales,
    optimize_subscription_service,
    calculate_development_cost,
    calculate_marketing_cost,
    calculate_operations_cost,
)

# Request model for POST data
class StartupIdea(BaseModel):
    idea: str

# Initialize FastAPI app
app = FastAPI()

@app.post("/create_startup")
async def create_startup(idea: StartupIdea):
    """
    Main API endpoint to build a startup plan based on a user-provided idea.
    """

    try:
        # Step 1: Process the Startup Idea
        idea_response = get_startup_idea(idea.idea)

        # Step 2: Analyze Market Trends
        market_data = analyze_market_trends(idea.idea)

        # Step 3: Generate Brand Identity
        brand_identity = generate_brand_name_and_tagline(idea.idea)

        # Step 4: Create Business Model
        business_model = create_business_model(idea.idea)

        # Step 5: Financial Analysis
        product_sales = optimize_product_sales(pricing=100, units=2000, demand_growth=0.2)
        subscription_service = optimize_subscription_service(base_price=25, subscribers=800, churn_rate=0.07)
        development_cost = calculate_development_cost(budget=50000, features=10)
        marketing_cost = calculate_marketing_cost(budget=20000, cpa=50, customers_acquired=300)
        operations_cost = calculate_operations_cost(overhead=10000, scaling_factor=1.2)

        # Return final response
        return {
            "idea_processing": idea_response,
            "market_analysis": market_data,
            "brand_identity": brand_identity,
            "business_model": business_model,
            "financial_analysis": {
                "product_sales": product_sales,
                "subscription_service": subscription_service,
                "development_cost": development_cost,
                "marketing_cost": marketing_cost,
                "operations_cost": operations_cost,
            }
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")


@app.get("/")
async def root():
    """
    Health check endpoint.
    """
    return {"message": "AI Startup Builder API is running"}
