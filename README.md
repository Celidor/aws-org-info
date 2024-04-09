# aws-org-access
* enumerates AWS accounts in an org and reports on those with the default `OrganizationAccountAccessRole`

## setup
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## usage
* assume a role into the AWS org management account
* open CloudShell
* upload the file org_access.py to CloudShell
```
python org_access.py
```