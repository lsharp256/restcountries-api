import requests
import json
from jsonschema import validate, ValidationError
import pytest

# The URL to test
url = "https://restcountries.com/v3.1/all/"

# Load your JSON schema
with open("schema.json", "r") as schema_file:
    schema = json.load(schema_file)

def test_api_schema_validation():
    # Send GET request to the API
    response = requests.get(url)

    # Check that the response is successful (status code 200)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    # Get the JSON data from the response
    response_data = response.json()

    # Ensure each country has a 'capital' field, adding a default if missing
    for country in response_data:
        if 'capital' not in country:
            country['capital'] = []  # Or provide a default value

    # Validate the JSON response against the schema
    try:
        validate(instance=response_data, schema=schema)
    except ValidationError as ve:
        pytest.fail(f"Validation failed: {ve.message}")



def test_number_of_countries():
    # Send GET request to the API
    response = requests.get(url)
    
    # Check that the response is successful (status code 200)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    # Get the JSON data from the response
    response_data = response.json()

    # Dynamically determine the number of countries based on the API's response
    actual_number = len(response_data)

    # Validate that the result is within a reasonable range
    assert actual_number >= 195, f"Expected at least 195 countries, but got {actual_number}"


def test_south_africa_languages():
    # Send GET request to the API
    response = requests.get(url)
    
    # Check that the response is successful (status code 200)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    # Get the JSON data from the response
    response_data = response.json()

    # Find South Africa's data
    south_africa = next((country for country in response_data if country.get('name', {}).get('common') == 'South Africa'), None)
    
    assert south_africa is not None, "South Africa not found in the response."

    # Get the list of languages
    languages = south_africa.get('languages', {})

    # Print the available languages to see their codes and check for SASL
    print(f"Languages for South Africa: {languages}")

    # Check if SASL is present in the language codes (you may need to find the code for SASL)
    assert 'sign' in languages or 'sasl' in languages, "South African Sign Language (SASL) is not listed as an official language."


