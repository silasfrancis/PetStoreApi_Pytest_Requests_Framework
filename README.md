## API Automation Testing on PestStore API
This project involves performing automation testing on PestStore API using Python Requests module.

## Features 
- HTML Reports
- Automation logs
- Parallel Testing
- Json Feedbacks

## Test Scenarios
1). User Module: 
  - Post User
  - Get User by Username
  - Update user
  - Delete User by Username

2). Pet Module:
  - Create pet
  - Get pet
  - Update pet data
  - Delete pet
 
3). Store Module:
    - Create order
    - Get oder
    - Delete order
   
## Languages and  tools used
- Python
- Pytest
- Requests module

## Test Execution
pytest -s -v  --html=./Reports/report.html tests/ 
