.. _webserver:

Webserver
=========

The webserver lets you run jobs by making HTTP requests.

Example of an HTTP request made in a Python script:

..  code-block:: python

  import requests

  requests.post(
    "https://example.com/api/v1/jobs/",
    json={
      "molecule": {
        "geometry": [
           0.0000,   0.0000,   0.0626,
          -0.7920,   0.0000,  -0.4973,
           0.7920,   0.0000 , -0.4973
        ],
        "symbols": ["O", "H", "H"]
      },
      "driver": "energy",
      "model": {
        "method": "HF",
        "basis": "STO-3G"
      },
    }
  )

Endpoints
---------

.. openapi:: ../../openapi.json
