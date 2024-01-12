from temporalio.client import Client
from temporalio.worker import Worker
from api.activity import ssn_trace_activity

from api.temporal import BackgroundCheck


async def main():
    client = await Client.connect(
        "localhost:7233", namespace="backgroundcheck_namespace"
    )

    worker = Worker(
        client,
        task_queue="backgroundcheck-boilerplate-task-queue",
        workflows=[BackgroundCheck],
        activities=[ssn_trace_activity],
    )

    await worker.run()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
