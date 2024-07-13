def error(error_type: str, error_message: str):
    return {
        "success": False,
        "error": {
            "error_type": error_type,
            "error_message": error_message,
        },
    }
