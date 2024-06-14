# aws-org-info

## organization access role
* enumerates AWS accounts in an org and reports on those with the default `OrganizationAccountAccessRole`

## IAM users
* enumerates AWS accounts in an org and reports on number of IAM users

## setup
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## usage
* assume a role into the AWS org management account
* open CloudShell
* upload the file, e.g. org_access.py to CloudShell
```
python org_access.py
```