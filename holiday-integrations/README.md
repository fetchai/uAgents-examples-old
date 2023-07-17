#  uAgent Holiday integrations Examples

This is a basic template with three agents `top_activities`, `top_destinations` and `flights`.

First get the `RAPIDAPI_API_KEY` and `OPENAI_API_KEY` API keys and create a .env file in `holiday-integrations` directory where you export these environment variables:
```bash
export RAPIDAPI_API_KEY="{GET THE API KEY}"
export OPENAI_API_KEY="{GET THE API KEY}"
```

To use the environment variables from .env and install the project:
```bash
source .env
poetry install
```

To run the project and its agents:
```bash
cd src
poetry shell
python main.py
```
