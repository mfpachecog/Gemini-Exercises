# checking for nothing 
# the task will be to check the status of a job

job_status = None

is_job_not_assigned = job_status is None

print(f"Is the job not assigned? {is_job_not_assigned}")

job_status = "In progress"

is_job_active = job_status is not None

print(f"Is the job active? {is_job_active}")
