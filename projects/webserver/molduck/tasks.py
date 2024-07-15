from typing import Any
from uuid import UUID

from celery import shared_task

from molduck import schemas
from molduck.models import Job
from molduck.runner import EnergyRunner


@shared_task
def run_job(job_id: UUID, input_data: dict[str, Any]):
    output_data: dict[str, Any] | None = None
    runner = None

    job = Job.objects.get(uuid=job_id)

    # Exit if job with given id was not found
    if job is None:
        return

    input_data = schemas.QCSchemaInput(**input_data)

    # Do the computation
    if input_data.driver == "energy":
        # output_data = energy(input_data)
        runner = EnergyRunner(input_data)

    if runner is None:
        return

    output_data = runner.run()

    if output_data.get("success"):
        job.success = True

    # Write output
    if output_data is not None:
        job.output_data = output_data
        job.save()
