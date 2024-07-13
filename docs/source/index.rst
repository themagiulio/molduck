=====================
Molduck documentation
=====================

.. attention::
  Molduck is in early stages, it is not completely documented and bugs can occur.

Molduck is a webserver and cli for quantum chemistry calculations.

- **Webserver**: the webserver does the calculations and accepts requests written according to the `MolSSI QC Schema`_.
- **CLI**: the cli works as a frontend and middleman as it lets you make requests to the webserver and use input files written in several formats.

Example of QC Schema JSON payload:

..  code-block:: json
  
  {
    "molecule": {
      "molecular_charge": 0,
      "molecular_multiplicity": 1,
      "geometry": [
         0.0000,   0.0000,   0.0626,
        -0.7920,   0.0000,  -0.4973,
         0.7920,   0.0000 , -0.4973
      ],
      "symbols": ["O", "H", "H"]
    },
    "driver": "energy",
    "model": {
      "method": "KS",
      "basis": "STO-3G"
    },
    "keywords": {
      "xc": "lda,vwn"
    }
  }

Contact
=======

* You can reach me by email: `hello@giuliodematte.is`_.

* To report bugs or request features, please use the `issue tracker`_. Before you
  do so, make sure you are running the `latest version`_, and please do a
  quick search to see if the issue has already been reported.

Table of Contents
=================

.. toctree::
   :maxdepth: 2
   :includehidden:

   intro/index
   usage/index


.. _`MolSSI QC Schema`: https://molssi-qc-schema.readthedocs.io/en/latest/index.html
.. _`hello@giuliodematte.is`: hello@giuliodematte.is
.. _`issue tracker`: https://github.com/themagiulio/molduck/issues
.. _`latest version`: https://github.com/themagiulio/molduck/releases/latest
