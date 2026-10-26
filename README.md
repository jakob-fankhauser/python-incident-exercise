# Python Debugging Exercise

## Scenario
This API processes purchase-order confirmations.
Some requests fail. Investigate and fix the problem.

## Setup

**Option A – Browser (recommended, no installation):**
Open https://codespaces.new/jakob-fankhauser/python-incident-exercise,
click **Create codespace** and wait until the setup has finished.

**Option B – Local (Python 3.10+):**

```bash
git clone https://github.com/jakob-fankhauser/python-incident-exercise.git
cd python-incident-exercise
```

Without Git: use **Code → Download ZIP** and unzip it.

Windows (PowerShell):
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Ubuntu/WSL you may first need: `sudo apt install python3-venv`

**Check:** `python -m pytest -v` must show **2 passed**.

## Start
Run the existing tests:

```bash
python -m pytest -v
```

Then inspect `incident.log` and `app.py`.

## Expected behaviour
- Accept delivery dates in `YYYY-MM-DD` and `DD.MM.YYYY`.
- Return successful dates as `YYYY-MM-DD`.
- Return HTTP 422 for invalid dates without changing the order.
- Keep HTTP 404 for unknown purchase orders.

Example request body:

```json
{
  "po_number": "4500012345",
  "delivery_date": "15.11.2026"
}
```

Other example dates: `2026-11-15` and `31.02.2026`.

## Your task
1. Reproduce and explain the failure.
2. Implement a small fix.
3. Add tests for a German date and an invalid date.

Please think aloud. No major refactoring is needed.

Timebox: 15–20 minutes.
If time permits, explain how you would safely release the fix.
