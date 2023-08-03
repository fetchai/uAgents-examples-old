# 🚗 uAgent Mobility Integrations Examples 🚴

This repository contains examples of mobility integrations using two agents: `ev_charger` and `geoapi_car_parking`.

1. `ev_charger`: This agent takes latitude, longitude, and a miles radius as input and returns available EV chargers in that region within the given radius. It utilizes the [OpenChargeMap](https://openchargemap.org/site/develop/api) API to retrieve the desired results.

2. `geoapi_car_parking`: This agent takes latitude, longitude, and a miles radius as input and returns available parking spaces within that radius. The agent leverages [Geoapify](https://www.geoapify.com/) to fetch the desired results.

## Getting Started 🚀

To use these agents, follow the steps below:

### Step 1: Obtain API Keys 🔑

Before running the agents, you need to obtain the required API keys:

#### OPENCHARGEMAP_API_KEY 🔌

1. Visit the OpenChargeMap API website: https://openchargemap.org/site/develop/api.
2. If you don't have an account, create one by signing up.
3. Once you are logged in, navigate to the API access section.
4. Find a form to request an API key in the API access section.
5. Fill out the required information in the form, including the purpose of using the API, and submit the request.
6. Once approved, you will receive your `OPENCHARGEMAP_API_KEY` via email.

#### GEOAPI_API_KEY 🗺️

1. Go to the Geoapify website: https://www.geoapify.com/.
2. Sign in to your Google account or create a new one if you don't have an existing account.
3. Once you are logged in, create a new project by clicking on the "Add a new project" button under the Projects section.
4. Give your project a name and click "OK" to create the new project.
5. Your `GEOAPI_API_KEY` will be generated. Copy this key and keep it secure, as it will be used to access Geoapify Projects and other services.

### Step 2: Set Environment Variables 🌐

Create a `.env` file in the `mobility-integrations` directory and export the obtained API keys as environment variables:

```bash
export OPENCHARGEMAP_API_KEY="{GET THE API KEY}"
export GEOAPI_API_KEY="{GET THE API KEY}"
```

### Step 3: Install Dependencies ⚙️

To use the environment variables from the `.env` file and install the project dependencies:

```bash
source .env
poetry install
```

### Step 4: Run the Project 🏃

To run the project and its agents:

```bash
cd src
poetry shell
python main.py
```

Now you have the agents up and running to perform mobility integrations using the provided APIs. Happy integrating! 🎉
