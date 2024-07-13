.. _webserver:

Webserver
=========

Start a calculation
-------------------

..  code-block:: python

  import requests

  requests.get(
    "https://example.com/api/",
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

TO DO
