import json
from botocove import cove


@cove()
def iam_users(session):
    iam = session.client("iam")

    # List IAM users
    users = []
    paginator = iam.get_paginator("list_users")
    for page in paginator.paginate():
        users.extend(page["Users"])

    return users


def main():
    # No session passed as the decorator injects it
    all_results = iam_users()
    number_of_accounts = len(all_results)
    total_iam_users = 0

    summary = []

    for result in all_results["Results"]:
        iam_user_report = result["Result"]
        number_of_users = len(iam_user_report)
        summary.append(
            {
                "AccountId": result["Id"],
                "IAMUsers": number_of_users,
            }
        )
        total_iam_users += number_of_users

    print("AWS Accounts in org: ", number_of_accounts)
    print("Total IAM users: ", total_iam_users)
    print(json.dumps(summary, indent=4))

    # write JSON object to file
    with open("iam_user_report.json", "w") as outfile:
        json.dump(summary, outfile, indent=4)


if __name__ == "__main__":
    main()
