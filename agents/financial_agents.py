import os
from google.generativeai import configure, GenerativeModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
configure(api_key=GEMINI_API_KEY)

# Initialize the model instance
try:
    model = GenerativeModel(model_name="gemini-1.5-pro")
except Exception as e:
    print(f"Error initializing Gemini model: {e}")
    raise e


def optimize_product_sales(pricing: float, units: int, demand_growth: float) -> dict:
    """
    Optimizes revenue from product sales using Gemini API.
    """
    revenue = pricing * units
    growth_projection = revenue * (1 + demand_growth)

    try:
        prompt = f"""
        A company sells a product priced at ${pricing:.2f} with {units} units sold per month. 
        Demand growth is estimated at {demand_growth*100:.1f}%. 
        Provide a 2-3 line recommendation to optimize revenue based on this data.
        """
        response = model.generate_content(prompt)
        recommendation = response.text.strip()
    except Exception as e:
        recommendation = f"Error generating content: {e}"
        print(recommendation)

    return {
        "current_revenue": revenue,
        "projected_revenue": growth_projection,
        "recommendation": recommendation
    }


def optimize_subscription_service(base_price: float, subscribers: int, churn_rate: float) -> dict:
    """
    Optimizes subscription revenue using Gemini API.
    """
    recurring_revenue = base_price * subscribers
    projected_loss = recurring_revenue * churn_rate

    try:
        prompt = f"""
        A subscription service charges ${base_price:.2f} per month with {subscribers} active subscribers. 
        The churn rate is {churn_rate*100:.1f}%. 
        Suggest strategies to reduce churn and improve recurring revenue in 2-3 lines.
        """
        response = model.generate_content(prompt)
        recommendation = response.text.strip()
    except Exception as e:
        recommendation = f"Error generating content: {e}"
        print(recommendation)

    return {
        "recurring_revenue": recurring_revenue,
        "projected_loss_due_to_churn": projected_loss,
        "recommendation": recommendation
    }


def calculate_development_cost(budget: float, features: int) -> dict:
    """
    Allocates development budget and provides recommendations using Gemini API.
    """
    cost_per_feature = budget / features

    try:
        prompt = f"""
        A company has a development budget of ${budget:.2f} allocated for {features} features. 
        The cost per feature is ${cost_per_feature:.2f}. 
        Recommend the best allocation strategy to maximize return on investment in bullets.
        """
        response = model.generate_content(prompt)
        recommendation = response.text.strip()
    except Exception as e:
        recommendation = f"Error generating content: {e}"
        print(recommendation)

    return {
        "total_budget": budget,
        "cost_per_feature": cost_per_feature,
        "recommendation": recommendation
    }


def calculate_marketing_cost(budget: float, cpa: float, customers_acquired: int) -> dict:
    """
    Optimizes marketing spend and provides recommendations using Gemini API.
    """
    total_spent = cpa * customers_acquired
    remaining_budget = budget - total_spent

    try:
        prompt = f"""
        A marketing campaign has a total budget of ${budget:.2f}. 
        The cost per acquisition (CPA) is ${cpa:.2f}, and {customers_acquired} customers have been acquired. 
        Suggest the optimal strategy to utilize the remaining budget of ${remaining_budget:.2f} in bullets.
        """
        response = model.generate_content(prompt)
        recommendation = response.text.strip()
    except Exception as e:
        recommendation = f"Error generating content: {e}"
        print(recommendation)

    return {
        "total_spent": total_spent,
        "remaining_budget": remaining_budget,
        "recommendation": recommendation
    }


def calculate_operations_cost(overhead: float, scaling_factor: float) -> dict:
    """
    Optimizes operational costs using Gemini API.
    """
    scaled_cost = overhead * scaling_factor

    try:
        prompt = f"""
        A company's operational overhead is ${overhead:.2f}, and the scaling factor is {scaling_factor:.2f}. 
        The scaled cost is estimated at ${scaled_cost:.2f}. 
        Suggest strategies to reduce operational costs and improve scalability in 2-3 lines.
        """
        response = model.generate_content(prompt)
        recommendation = response.text.strip()
    except Exception as e:
        recommendation = f"Error generating content: {e}"
        print(recommendation)

    return {
        "current_overhead": overhead,
        "scaled_cost": scaled_cost,
        "recommendation": recommendation
    }
