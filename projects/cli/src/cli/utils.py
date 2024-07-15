def get_status(status_code: int) -> str:
    match status_code:
        case 1:
            return "Awaiting"
        case 2:
            return "Running"
        case 3:
            return "Failed"
        case 4:
            return "Succeded"
