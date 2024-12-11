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


def create_business_model(idea: str) -> dict:
    """
    Uses Gemini API to generate a dynamic business model based on the startup idea.
    """
    try:
        # Generate a prompt for business model creation
        prompt = f"""
        Create a detailed business model for the following startup idea: "{idea}". 
        Include the following sections:
        - Revenue Streams (sources of revenue)
        - Cost Structure (main expenses)
        - Target Customers (key customer segments)
        keep it precise and concise.
        """

        # Fetch data from Gemini API
        response = model.generate_content(prompt)
        business_model_text = response.text.strip()

        # Extract details from the response
        revenue_streams = []
        cost_structure = []
        target_customers = []

        # Parse the business model text
        current_section = None
        for line in business_model_text.splitlines():
            line_cleaned = line.strip()

            # Identify sections
            if "Revenue Streams" in line_cleaned:
                current_section = "revenue_streams"
            elif "Cost Structure" in line_cleaned:
                current_section = "cost_structure"
            elif "Target Customers" in line_cleaned:
                current_section = "target_customers"

            # Append relevant data
            elif current_section == "revenue_streams" and line_cleaned:
                revenue_streams.append(line_cleaned.strip("- "))

            elif current_section == "cost_structure" and line_cleaned:
                cost_structure.append(line_cleaned.strip("- "))

            elif current_section == "target_customers" and line_cleaned:
                target_customers.append(line_cleaned.strip("- "))

        # Return the structured business model
        return {
            "idea": idea,
            "revenue_streams": revenue_streams,
            "cost_structure": cost_structure,
            "target_customers": target_customers,
        }

    except Exception as e:
        print(f"Error generating business model: {e}")
        return {
            "idea": idea,
            "revenue_streams": ["Unknown"],
            "cost_structure": ["Unknown"],
            "target_customers": ["Unknown"],
        }

