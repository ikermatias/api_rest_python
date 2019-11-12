"""This module will encode and parse the query string params."""

from urllib.parse import parse_qs, urlparse


def parse_query_params(query_string):
    """
        Function to parse the query parameter string.
        """
    # Parse the query param string
    # Get the value from the list
    parsed_url= urlparse(query_string)
    query_params = dict(parse_qs(parsed_url.query))

    query_params = {k: v[0] for k, v in query_params.items()}
    return query_params