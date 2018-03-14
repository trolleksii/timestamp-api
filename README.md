# Timestamp API

1) It will check to see whether that string contains either a unix timestamp or a natural language date (example: January 1, 2016)

2) If it does, it returns both the Unix timestamp and the natural language form of that date.

3) If it does not contain a date or Unix timestamp, it returns null for those properties.

Example usage:
`http://localhost:8000/December%2015,%202015`
`http://localhost:8000/1450137600`
Example output:
{ "unix": 1450137600, "natural": "December 15, 2015" }

