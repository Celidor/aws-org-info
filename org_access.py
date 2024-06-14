from botocove import cove


@cove()
def get_aws_account_id(session):
    sts = session.client("sts")
    return sts.get_caller_identity()["Account"]


def main():
    # No session passed as the decorator injects it
    all_results = get_aws_account_id()

    # Returns a Dict with keys Results, Exceptions and FailedAssumeRole
    print("Accounts with org access role: ", len(all_results["Results"]))
    # print("Total exceptions: ", len(all_results["Exceptions"]))
    print("Accounts without org access roles: ", len(all_results["FailedAssumeRole"]))
    print(
        "Total accounts:",
        len(all_results["Results"]) + len(all_results["FailedAssumeRole"]) + 1,
    )


if __name__ == "__main__":
    main()
