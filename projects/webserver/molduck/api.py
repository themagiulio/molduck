import importlib.metadata
from uuid import UUID

from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from molduck import schemas
from molduck.models import Job
from molduck.tasks import run_job

api = NinjaAPI(version="1.0.0")


@api.get("/")
def version(request):
    """Retrieve webserver version."""
    return {"version": importlib.metadata.version("webserver")}


@api.get("/jobs/", response=list[schemas.Job], exclude_none=True)
def list_jobs(request):
    """List all jobs."""
    return Job.objects.all()


@api.post("/jobs/", response=schemas.Job)
def create_job(request, data: schemas.QCSchemaInput):
    """Create a new job."""
    job = Job.objects.create(input_data=data.dict())
    run_job.delay(job.uuid, data.dict())
    return job


@api.get("/jobs/{job_id}/", response=schemas.Job, exclude_none=True)
def retrieve_job(request, job_id: UUID):
    """Retrieve a job."""
    return get_object_or_404(Job, uuid=job_id)


@api.get("/jobs/{job_id}/qcschema/")
def retrieve_job_as_qcschema(request, job_id: UUID):
    """Retrieve a job input and output as QC Schema."""
    job = get_object_or_404(Job, uuid=job_id)
    return {**job.input_data, **job.output_data}
