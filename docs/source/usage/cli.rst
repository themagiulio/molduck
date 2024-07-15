.. _cli:

Command Line Interface
======================

Installation
------------

TO DO

Verify your installation with the following command:

.. code-block:: console

   $ molduck version

Information about the installed CLI and server should appear.

Get Started with Molduck CLI
----------------------------

Connect to a webserver
~~~~~~~~~~~~~~~~~~~~~~

After you install the CLI, run ``molduck connect`` to connect to a webserver.

.. code-block:: console

   $ molduck connect
   Enter webserver url: http://localhost:8000

The CLI saves your webserver address in a configuration file for future use.

.. seealso::

   to setup a webserver on your machine take a look at the :ref:`relevant documentation <webserver>`.

Run your first job
~~~~~~~~~~~~~~~~~~

Create a new file named ```my_first_job.json`` with the following content:

.. code-block:: json

   {
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
      "method": "RHF",
      "basis": "STO-3G"
    }
  }

This JSON file specifies the computation that should be made by the webserver in the MolSSI QCS chema.

Create your first job:

.. code-block:: console

   $ molduck jobs run ./my_first_job.json
   Created job with ID: 258ecd36-f682-4797-9a5b-19634018eb66

You can see all jobs (running, executed and awaiting to be executed) with the following command:

.. code-block:: console

   $ molduck jobs ls
   ID                                    Status   Success
   ------------------------------------  -------- -------
   258ecd36-f682-4797-9a5b-19634018eb66  Executed True

To display the result of an executed job run:

.. code-block:: console
   
   $ molduck jobs info 258ecd36-f682-4797-9a5b-19634018eb66
   {
    "molecule": {
      "molecular_charge": null,
      "molecular_multiplicity": null,
      "geometry": [
        0,
        0,
        0.0626,
        -0.792,
        0,
        -0.4973,
        0.792,
        0,
        -0.4973
      ],
      "symbols": [
        "O",
        "H",
        "H"
      ]
    },
    "model": {
      "method": "RHF",
      "basis": "STO-3G"
    },
    "driver": "energy",
    "keywords": null,
    "success": true,
    "return_result": -74.9616272936897,
    "properties": {
      "calcinfo_nbasis": 5,
      "calcinfo_nmo": 7,
      "calcinfo_natom": 3,
      "calcinfo_nalpha": 5,
      "calcinfo_nbeta": 5,
      "return_energy": -74.9616272936897,
      "scf_one_electron_energy": -84.02508660833695,
      "scf_two_electron_energy": 38.15333870717342,
      "nuclear_repulsion_energy": 9.063459314647254,
      "scf_dipole_moment": [
        1.1287621574073828e-15,
        -1.22631023096877e-16,
        -1.676879822486307
      ],
      "scf_total_energy": -74.9616272936897
    }
  }

The returned result is written, as the input, according to the QC Schema. As such, it contains input and output of the calculation.
