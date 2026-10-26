# Python Debugging Exercise

## Scenario
This API processes purchase-order confirmations.
Some requests fail. Investigate and fix the problem.

The environment is already prepared. No installation is required.

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
