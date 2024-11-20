import traceback
import time
from typing import Sequence, Any
from slack_sdk.webhook import WebhookClient
from slack_sdk.models.blocks import Block


class SlackMessenger:
    """A class for sending messages to Slack."""

    def __init__(self, url: str) -> None:
        self._webhook = WebhookClient(url=url)

    def send(
            self,
            text: str | None = None,
            blocks: Sequence[dict[str, Any] | Block] | None = None
    ) -> None:
        """Sends a message."""

        counter = 0
        while True:
            counter += 1
            try:
                response = self._webhook.send(
                    text=text,
                    blocks=blocks,
                    unfurl_links=True,
                    unfurl_media=True
                )
                assert (
                        response.status_code == 200 and
                        response.body == 'ok'
                ), 'Invalid response or failed status.'
                break
            except Exception as e:
                print(f'Sends a message failed. Counter: {counter}')
                traceback.print_exc()
                if counter >= 5:
                    raise e
                time.sleep(10)
