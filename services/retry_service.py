MAX_RETRIES = 3


def can_retry(state):

    return (
        state["retry_count"]
        < MAX_RETRIES
    )