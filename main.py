from fastapi import FastAPI
from App import ParkingSpot, ParkingLot, ParkingLotScanner, NotificationManager

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}