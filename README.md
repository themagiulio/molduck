# Molduck

<img align="right" width="auto" height="100" src="./public/logo.png">

Molduck is a webserver and cli for quantum chemistry calculations.

- **Webserver**: the webserver does the calculations and accepts requests written according to the [MolSSI QC Schema](https://molssi-qc-schema.readthedocs.io/en/latest/index.html).
- **CLI**: the cli works as a frontend and middleman as it lets you make requests to the webserver and use input files written in several formats.

Example of QC Schema JSON payload:
```json
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
```

The input can be passed to the server directly as a JSON body in an HTTP request or by using the cli as a wrapper:

```
$ molduck jobs run /path/to/input_file.json
```

Running or completed jobs can be listed using the following command:

```
$ molduck jobs ls
```

Please, read the [documentation](https://molduck.surge.sh) for the full list of api endpoints and cli commands.

Available methods:
- HF: RHF, UHF.
- KS: RKS, UKS.
- MP2.
- CI: CISD, FCI.

## Deploy

TO DO

## License

Molduck is licensed under the [Apache 2.0 with Commons Clause license](./LICENSE).

Duck artwork created by [Adnan_111](https://adnan-111.itch.io/duck-assets-pack).
