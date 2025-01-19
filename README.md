# Deploy FastAPI WhatsApp Weebhook on Render

Use this repo as a template to deploy a Python [FastAPI](https://fastapi.tiangolo.com) [WhatsApp Weebhook](https://developers.facebook.com/docs/whatsapp/cloud-api/overview#webhooks) service on Render.

This repository implements the [WhatsApp Platform Quick Start](https://glitch.com/edit/#!/whatsapp-cloud-api-echo-bot) which uses JavaScript and It is deployed on [Glitch](https://glitch.com) to a Python [FastAPI](https://fastapi.tiangolo.com) service which is deployed on [Render](https://render.com).

## Deployment on Render

1. Follow the instructions [WhatsApp Business - Cloud API Getting Started](https://developers.facebook.com/docs/whatsapp/cloud-api/get-started/).
2. Once you get **[Step 4: Clone our test app and set up weebhooks](https://developers.facebook.com/docs/whatsapp/cloud-api/get-started/#clone-sample-app)** using [Glitch](https://glitch.com), you can use this repository to deploy the webhook on Render.
3. You may use this repository directly or [create your own repository from this template](https://github.com/jcarranz97/whatsapp-weebhook-fastapi/generate) if you'd like to customize the code.
4. Create a new Web Service on Render.
5. Specify the URL to your new repository or this repository.
6. Specify the following as the `Build Command`.

    ```shell
    pip install uv
    ```
7. Specify the following as the `Start Command`.

    ```shell
    uv run fastapi run --port $PORT
    ```
8. Add the following environment variables (which where created as part of the [WhatsApp Business - Cloud API Getting Started](https://developers.facebook.com/docs/whatsapp/cloud-api/get-started/)) in your Render Web Service:

    ```shell
    WEBHOOK_VERIFY_TOKEN = verify_token
    GRAPH_API_TOKEN = api_token
    ```
9. Click on `Create Web Service` to deploy the FastAPI WhatsApp Weebhook on Render.

## Technologies Used

### uv

This template uses [uv](https://astral.sh/blog/uv), An extremely fast Python package and project manager, written in Rust.

## FastAPI

This template uses [FastAPI](https://fastapi.tiangolo.com), a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.

## ruff

This template uses [ruff](https://docs.astral.sh/ruff/), An extremely fast Python linter and code formatter, written in Rust.

## Thanks

Thanks to [Render](https://render.com) for providing the example [Deploy a FastAPI App](https://render.com/docs/deploy-fastapi) which was used as a reference to deploy this template.

Thanks to [WhatsApp Business - Cloud API Getting Started](https://developers.facebook.com/docs/whatsapp/cloud-api/get-started/) for providing the example [WhatsApp Platform Quick Start](https://glitch.com/edit/#!/whatsapp-cloud-api-echo-bot) which was used as a reference to create this template.
