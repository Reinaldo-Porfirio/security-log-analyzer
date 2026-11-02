# Security Log Analyzer

A small Python tool that parses Linux SSH authentication logs (`auth.log`) and flags IP addresses with repeated failed login attempts, a common sign of brute-force attacks.

## Features

- Parses `Failed password` entries from `auth.log`
- Flags IPs whose failed attempts reach a configurable threshold
- Prints a formatted table in the terminal (Rich)
- Exports each run to a timestamped CSV report in `reports/`
- Configurable through environment variables or a `.env` file
- Runs locally or in Docker

## Tech stack

Python 3.12 · Rich · python-dotenv · pytest · Docker

## Project structure

```
analyzer/
  parser.py     # reads the log and counts failed attempts per IP
  detector.py   # applies the brute-force threshold
  report.py     # writes the CSV report
logs/auth.log   # sample log for testing
tests/          # unit tests (pytest)
main.py         # entry point
```

## Configuration

Copy `.env.example` to `.env` and adjust:

| Variable | Default | Description |
| --- | --- | --- |
| `LOG_FILE` | `logs/auth.log` | Path to the log file to analyze |
| `BRUTEFORCE_THRESHOLD` | `3` | Failed attempts needed to flag an IP |

## How to run

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

With Docker:

```bash
docker build -t security-log-analyzer .
docker run --rm security-log-analyzer
```

To analyze a real server log, mount it into the container:

```bash
docker run --rm -v /var/log/auth.log:/data/auth.log:ro -e LOG_FILE=/data/auth.log security-log-analyzer
```

## Tests

```bash
pip install pytest
python -m pytest
```

## Roadmap

- Detect more attack patterns (invalid users, `sudo` failures, port scans)
- Time-window based detection (N failures in M minutes)
- GitHub Actions pipeline running the tests on every push
- Export alerts to a dashboard (Grafana/Loki)
