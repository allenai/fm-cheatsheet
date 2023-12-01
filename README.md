# skiff-template-streamlit

Ahoy! Welcome to your new [skiff](https://github.com/allenai/skiff) template
application that includes:

* A Python, [Streamlit App](https://streamlit.io/).
* An [NGINX](https://www.nginx.com/) web server for serving static assets and
  reverse proxying requests to the app.
* Automatic deploys to shared infrastructure and other functionality provided by
  [skiff](https://skiff.allenai.org).

To start a new repository from this template, click [here](https://github.com/allenai/skiff-template-streamlit/generate).

## Prerequisites

Before following the steps below, make sure that you have the latest version
of [Docker 🐳](https://www.docker.com/get-started) installed on your local
machine.

## Getting Started

Start by opening `skiff.json` and updating the `appName`, `contact` and
`team` fields:

* The `appName` field should be a short, unique and url-safe identifier for
  your application. This value determines the url of your application, which
  will be `${appName}.apps.allenai.org`.
* The `contact` field should be the `@allenai.org` email address that is
  responsible for the demo. Don't include the `@allenai.org` bit,
  just the part before it.
* The `team` field is the name of the team at AI2 that's responsible for
  the demo.

After committing and pushing these changes make sure to submit a
[request to be onboarded](https://github.com/allenai/skiff/issues/new/choose).

To start a version of the application locally for development purposes, run
this command:

```sh
~ docker compose up --build
```

This process launches several processes. When things have finished starting,
you'll see a message from a program called `sonar` informing you of the URL your
local environment is accessible at.

It might take a minute or two for your application to start, particularly
if it's the first time you've executed this command.

As you make changes the running application will be automatically updated.

Sometimes one portion of your application will crash. When this occurs resolve
the cause and re-run `docker compose up --build` to start things back up.

## Installing Third Party Packages

You'll likely want to install third party packages at some point. To do so
follow the steps described below.

### Python Dependencies

To add new dependencies to the Python portion of the project, follow these steps:

1. Make sure your local environment is running (i.e. you've ran `docker compose up`).
1. Start a shell session in the server container:

    ```sh
    ~ docker compose exec app /bin/bash
    ```

1. Install the dependency in question:

    ```sh
    ~ python -m pip install <dependency>
    ```sh

1. Update the dependency manifest:

    ```sh
    ~ python -m pip freeze -l > requirements.txt
    ```

1. Exit the container:

    ```sh
    ~ exit
    ```

Remember to commit and push the `requirements.txt` file to apply your changes.

## Integration Tests

The template includes a small set of integration tests. These tests are executed
against a running version of your application whenever changes are pushed.

You can run these tests while developing simply by running:

```sh
~ docker compose exec it yarn test
```

When the tests run automatically, they try to simulate the way things are run
in production. To use these same settings run:

```sh
./bin/verify
```

## Deploying

Your changes will be deployed automatically after they're pushed to the `main`
branch. To see information about your application and what's deployed,
visit the [Skiff Marina](https://marina.apps.allenai.org).

If you'd like to deploy a temporary, ad hoc environment to preview your changes,
view [this documentation](https://skiff.allenai.org/marina.html#creating-a-new-environment).

## Metrics and Logs

Skiff applications capture two kinds of metrics:

* Service level metrics, which capture information about the number of requests
  made to your application, the response rate, and other operational metrics.
  There's more information about these metrics [here](https://skiff.allenai.org/marina.html#service-level-metrics).

* End user analytics, which use JavaScript to track how many end users load
  your site in a Browser. There's more information about these statistics
  [here](https://skiff.allenai.org/stats.html).

## Helpful Links

Here's a list of resources that might be helpful as you get started:

* [Skiff User Guide](https://skiff.allenai.org/)
* [Streamlit Docs](https://docs.streamlit.io/)

## Getting Help

If you're stuck don't hesitate to reach out:

* Sending an email to [reviz@allenai.org](mailto:reviz@allenai.org)
* Joining the `#skiff-users` slack channel
* Opening a [Github Issue](https://github.com/allenai/skiff/issues/new/choose)

We're eager to improve `skiff` and need your feedback to do so!

Smooth sailing ⛵️!
