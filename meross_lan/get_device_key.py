import asyncio
import aiohttp
import getpass
import os

import cloudapi

async def main():

    email = input("Enter Meross cloud email:")
    password = getpass.getpass(prompt="Enter Meross cloud password:")

    async with aiohttp.ClientSession() as session:
        key = await cloudapi.async_get_cloud_key(email, password, session)

    print("\n=====================DEVICE_KEY========================")
    print(key)
    print("=======================================================\n")

    input("Press Enter to continue...")

if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.stop()