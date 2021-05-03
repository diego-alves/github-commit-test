""" Main Module """

from os import getenv
from sys import argv
from logging import info, warning, error, basicConfig, INFO

from boto3 import resource, client
from botocore.config import Config

from github_commit_test.consume import process


PROXY = getenv("PROXY")
CONFIG = Config(
    retries={
        "max_attempts": 10,
        "mode": "standard",
    },
    proxies={
        "http": PROXY,
        "https": PROXY,
    }
    if PROXY
    else None,
)

basicConfig(level=INFO)
sqs = resource("sqs", config=CONFIG)

def main():
    queue_url = argv[1] if len(argv) > 1 else None
    if queue_url is None:
        print(f"Invalid argument {queue_url}")
        exit(1)
    info("Start Consuming Queue " + queue_url)
    queue = sqs.Queue(queue_url)
    while True:
        for message in queue.receive_messages():
            try:
                process(message)
            except Exception as e:
                error(e)
            finally:
                message.delete()


if __name__ == "__main__":
    main()
