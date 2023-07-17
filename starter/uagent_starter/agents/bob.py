from uagents.setup import fund_agent_if_low
from uagents.resolver import get_agent_address
from uagents import Agent, Context

from messages.basic import Message


bob = Agent(
    name="agent bob",
    port=8001,
    seed="agent bob secret phrase",
    endpoint=["http://127.0.0.1:8001/submit"],
)

fund_agent_if_low(bob.wallet.address())


@bob.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")

    # send the response
    await ctx.send(sender, Message(message="Hello there alice."))


if __name__ == "__main__":
    bob.run()