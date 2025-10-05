import logging
from pathlib import Path

import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from inference import predict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

BASE_DIR = Path(__file__).parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/classify")
async def classify_email(email_data: dict):
    try:
        logger.info("Received classification request")

        if not email_data or "email" not in email_data:
            raise HTTPException(status_code=400, detail="No email data provided")

        try:
            proba, pred = predict(email_data["email"])

            confidence = proba / 100.0
            is_spam = pred[0] == 1

            logger.info(
                f"Prediction result - is_spam: {is_spam}, confidence: {confidence:.2f}"
            )

            if not is_spam:
                confidence = 1 - confidence
                
            return {"is_spam": bool(is_spam), "probability": confidence}

        except Exception as e:
            logger.error(f"Prediction error: {str(e)}", exc_info=True)
            raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unexpected error in classify_email: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )


if __name__ == "__main__":
    uvicorn.run("app:app", port=8000, reload=True)
