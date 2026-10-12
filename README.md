# status-api

A lightweight FastAPI application used to practise building, testing, deploying and operating a service using DevOps tooling.

The application is intentionally simple so the focus can remain on infrastructure, automation, reliability and deployment workflows.

## API endpoints

| Endpoint      | Description                                           |
| ------------- | ----------------------------------------------------- |
| `GET /`       | Returns a welcome message                             |
| `GET /health` | Returns the application's health status               |
| `GET /info`   | Returns the application name, version and environment |

## Technology stack

- Python 3.13
- FastAPI
- uv for dependency management
- pytest for automated testing
- Poe the Poet for development commands
- GitHub Actions for continuous integration

## Local development

Install project dependencies:

```bash
uv sync --locked
```

Run the development server:

```bash
uv run poe dev
```

Run the tests:

```bash
uv run poe test
```

## Continuous integration

The GitHub Actions workflow is defined in `.github/workflows/ci.yml`.

It is configured to run on pushes and pull requests targeting `main`, and performs the following operations:

1. Checks out the repository.
2. Installs uv and Python 3.13.
3. Synchronises dependencies against the committed lockfile.
4. Runs the automated test suite.

The workflow has been successfully tested locally using `act`, with all four tests passing. GitHub-hosted execution is pending verification.

## Roadmap

- [x] Implement application endpoints
- [x] Add automated tests
- [x] Configure reproducible dependency management
- [x] Create GitHub Actions CI workflow
- [x] Validate CI locally using `act`
- [ ] Verify CI on GitHub-hosted runners
- [ ] Introduce feature branches, pull requests and CI checks
- [ ] Containerise the application with Docker
- [ ] Build and publish versioned container images
- [ ] Provision AWS infrastructure using Terraform
- [ ] Configure secure application deployment on AWS
- [ ] Automate deployments through GitHub Actions CI/CD
- [ ] Add application logging, monitoring and alerting
- [ ] Implement deployment health checks and rollback procedures
- [ ] Document infrastructure architecture, deployment and recovery

## Project status

**In development** — application and automated testing completed; infrastructure and deployment work in progress.
