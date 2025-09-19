# Processing multiple job applications
job_applications = [
    {"company": "Google", "position": "SDE-1", "status": "applied"},
    {"company": "Microsoft", "position": "Software Engineer", "status": "interview"},
    {"company": "Amazon", "position": "SDE", "status": "pending"},
    {"company": "Meta", "position": "Frontend Engineer", "status": "applied"}
]

print("📋 Job Application Status Report:")


for i, application in enumerate(job_applications, 1):
    company = application["company"]
    position = application["position"]
    status = application["status"]
    
    # Color coding based on status
    if status == "interview":
        status_icon = "🟢"
    elif status == "applied":
        status_icon = "🟡"
    else:
        status_icon = "🔵"
    
    print(f"{i}. {company} - {position} {status_icon} {status.upper()}")
    

print(f"Total applications: {len(job_applications)}")
