import json
from rest_framework.parsers import BaseParser
from rest_framework.exceptions import ParseError

class CustomJSONParser(BaseParser):
    """
    Custom JSON parser to handle incoming JSON data.
    """
    media_type = 'application/json'

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Parse the incoming JSON data.
        """
        try:
            # Read the incoming request data (stream), and decode it into a Python dictionary
            data = json.loads(stream.read().decode('utf-8'))
        except ValueError as e:
            # If there's a JSON decode error, raise a ParseError
            raise ParseError("JSON parse error: %s" % str(e))
        
        return data
