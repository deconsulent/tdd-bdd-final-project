######################################################################
# Load Step Definitions
######################################################################
"""
Load Step Definitions

Steps file for loading background data for BDD scenarios.
Each scenario starts fresh with the data from the Background table.
"""

import requests
from behave import given  # pylint: disable=no-name-in-module

# HTTP Return Codes
HTTP_200_OK = 200
HTTP_201_CREATED = 201
HTTP_204_NO_CONTENT = 204


@given("the following products")
def step_impl(context):
    """Delete all Products and load new ones from the Background table"""

    # Get a list of all products and delete them (clean slate)
    rest_endpoint = f"{context.base_url}/products"
    context.resp = requests.get(rest_endpoint)
    assert context.resp.status_code == HTTP_200_OK

    for product in context.resp.json():
        resp = requests.delete(f"{rest_endpoint}/{product['id']}")
        assert resp.status_code == HTTP_204_NO_CONTENT

    # Load the table of products from the feature file Background
    for row in context.table:
        payload = {
            "name": row["name"],
            "description": row["description"],
            "price": row["price"],
            "available": row["available"] in ["True", "true", "1"],
            "category": row["category"],
        }
        context.resp = requests.post(rest_endpoint, json=payload)
        assert context.resp.status_code == HTTP_201_CREATED
