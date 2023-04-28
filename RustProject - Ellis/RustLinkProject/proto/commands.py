from rustplus import RustSocket, CommandOptions, Command
import time, asyncio

options = CommandOptions(prefix="!") # Use whatever prefix you want here
rust_socket = RustSocket("64.40.9.46", "28037", 76561198096181161, -1178426492, command_options=options)

async def main():
    await rust_socket.connect()

    await rust_socket.hang()

    await rust_socket.disconnect()

@rust_socket.command
async def hi(command : Command): 
    time.sleep(3)
    await rust_socket.send_team_message(f"[Thing]: Hi, {command.sender_name}")


asyncio.run(main())