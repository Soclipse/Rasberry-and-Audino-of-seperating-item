import asyncio
from bleak import BleakScanner

async def scan():
    print("Scanning for Bluetooth devices...")
    devices = await BleakScanner.discover()

    for device in devices:
        print("Name:", device.name)
        print("Address:", device.address)
        print("----------------------")

asyncio.run(scan())