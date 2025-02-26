# restcountries-api

This project contains tests for the RESTful API at [https://restcountries.com/v3.1/all/](https://restcountries.com/v3.1/all/). The tests are written in Python using the `requests`, `jsonschema`, and `pytest` libraries.

## Dependencies

The project dependencies are listed in the `requirements.txt` file. It includes:
- `requests` : For making HTTP requests.
- `jsonschema` : For validating JSON response schema
- `pytest` : For running the tests

## Installation

To install the dependencies, run the following command:

```sh
pip install -r requirements.txt
```

## Tests

The following tests are included in `test_api.py`:

1. **Schema Validation Test**: Validates the API response against a predefined JSON schema.
2. **Number of Countries Test**: Checks that the number of countries returned by the API is within a reasonable range.
3. **South Africa Languages Test**: Verifies that South African Sign Language (SASL) is listed as an official language for South Africa. \
    **Note**: This test currently fails because SASL is not found in the API response. It may be due to the response data not including SASL under the "languages" field.

## Running the Tests

```sh
pytest -v