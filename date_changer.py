from datetime import datetime

created_date = datetime(2024, 12, 18)
issue_date = datetime(2024, 12, 18)

temp_created_date = created_date.strftime("%d-%m")
temp_issue_date = issue_date.strftime("%d-%m")

print(f"Created Date: {temp_created_date}")
print(f"Issue Date: {temp_issue_date}")
