from utils.core.telegram import Accounts
from utils.starter import start
import asyncio


async def main():
    action = 1
    if action == 1:
        accounts = await Accounts().get_accounts()

        tasks = []

        for thread, account in enumerate(accounts):
            session_name, phone_number, proxy = account.values()
            tasks.append(asyncio.create_task(start(session_name=session_name, phone_number=phone_number, thread=thread, proxy=proxy)))

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
