from uagents import Bureau

from agents.alice import alice
from agents.bob import bob


if __name__ == "__main__":
    bureau = Bureau(endpoint="http://127.0.0.1:8000/submit", port=8000)
    bureau.add(alice)
    bureau.add(bob)
    bureau.run()