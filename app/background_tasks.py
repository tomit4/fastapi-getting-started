from typing import Annotated, Any

from fastapi import BackgroundTasks, Depends, FastAPI

app = FastAPI()


def write_notification(email: str, message: str = "") -> None:
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)


def write_log(message: str) -> None:
    with open("log.txt", mode="a") as log:
        log.write(message)


def get_query(background_tasks: BackgroundTasks, q: str | None = None) -> str | None:
    if q:
        message = f"found query: {q}\n"
        background_tasks.add_task(write_log, message)
    return q


@app.post("/send-notification/{email}")
async def send_notification(
    email: str, background_tasks: BackgroundTasks, q: Annotated[str, Depends(get_query)]
) -> dict[str, Any]:
    message = f"message to {email}"
    # Note that when adding tasks, that you provide the function,
    # then it's parameters as arguments to the add_task() method
    background_tasks.add_task(write_log, message)
    return {"message": "Notification sent in the background"}
