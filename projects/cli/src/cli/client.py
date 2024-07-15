import requests
from typing import Any

from cli.config import Config


class Client:
    _version: str = "v1"
    _config: Config = Config()

    def _mk_url(self, endpoint: str | None = None):
        return f"{self._server}/api/{self._version}/{endpoint}"

    def _mk_request(self, url: str, method: str, json: dict[str, Any] = {}):
        return requests.request(
            url=url,
            method=method,
            json=json,
            headers=self._mk_headers(),
        )

    def _mk_headers(self):
        headers = {}

        if self._apikey is not None:
            headers["Authorization"] = f"Bearer {self._apikey}"
        return headers

    def get_jobs(self):
        url = self._mk_url("jobs/")
        response = self._mk_request(url, "GET")

        if response.ok:
            return response.json()

    def get_job(self, job_id: str):
        url = self._mk_url(f"jobs/{job_id}/")
        response = self._mk_request(url, "GET")

        if response.ok:
            return response.json()

    def run_job(self, data):
        url = self._mk_url("jobs/")
        response = self._mk_request(url, "POST", json=data)

        if response.ok:
            return response.json()

    def get_profile(self):
        url = self._mk_url("users/me/")
        response = self._mk_request(url, "GET")

        if response.ok:
            return response.json()

    def get_version(self):
        url = self._mk_url("")
        response = self._mk_request(url, "GET")

        if response.ok:
            return response.json().get("version")

    @property
    def _server(self):
        return self._config.get_config("server")

    @property
    def _apikey(self):
        return self._config.get_config("apikey")
