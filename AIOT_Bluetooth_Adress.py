import asyncio
from bleak import BleakScanner

async def find_arduino():
    print("Searching for Arduino: LEDCallback...")

    devices = await BleakScanner.discover(timeout=10)

    found = False

    for device in devices:
        if device.name == "LEDCallback":
            print("\nArduino found!")
            print("Name:", device.name)
            print("Address:", device.address)
            found = True

    if not found:
        print("\nArduino not found.")
        print("Check that its BLE code is uploaded and Arduino is powered on.")

asyncio.run(find_arduino())