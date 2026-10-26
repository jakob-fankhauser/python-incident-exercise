"""Small order-confirmation API. Data is synthetic and stored in memory."""
import logging
from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

log = logging.getLogger("confirmations")
app = FastAPI(title="Order Confirmation Service")
ORDERS = {"4500012345": {"status": "OPEN", "delivery_date": None}}

class Confirmation(BaseModel):
    po_number: str = Field(min_length=1)
    delivery_date: str = Field(min_length=1)

@app.post("/confirmations")
def confirm(payload: Confirmation):
    # Payload comes from an upstream document-extraction service.
    # This exercise does not call an LLM or any external system.
    if payload.po_number not in ORDERS:
        raise HTTPException(status_code=404, detail="Unknown purchase order")
    try:
        delivery = datetime.strptime(payload.delivery_date, "%Y-%m-%d").date()
    except ValueError:
        log.exception("Date processing failed po=%s", payload.po_number)
        raise HTTPException(status_code=500, detail="Confirmation processing failed")
    order = ORDERS[payload.po_number]
    order.update(status="CONFIRMED", delivery_date=delivery.isoformat())
    log.info("Confirmation processed po=%s", payload.po_number)
    return {"po_number": payload.po_number, **order}
