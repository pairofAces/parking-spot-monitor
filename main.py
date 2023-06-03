from fastapi import FastAPI, HTTPException
from App import ParkingSpot, ParkingLot, ParkingLotScanner, NotificationManager

app = FastAPI()

parking_lot = ParkingLot()
notification_manager = NotificationManager()
scanner = ParkingLotScanner(parking_lot, notification_manager)



@app.get("/")
def read_root():
    return {"message": "Welcome to the Parking Lot Scanner API"}

@app.get('/parkinglot')
def get_parking_lot():
    return parking_lot.to_dict()

@app.get('/parkingspot/{spot_id}')
def get_parking_spot(spot_id: int):
    spot = parking_lot.get_spot_from_id(spot_id)
    if spot:
        return {'spot_id': spot.spot_id, 'is_occupied': spot.is_occupied}
    else:
        raise HTTPException(status_code=404, detail=f"Parking spot {spot_id} is not found")

@app.post('/parkingspot/{spot_id}/occupy')
def occupy_parking_spot(spot_id: int):
    parking_lot.occupy_spot(spot_id)
    return {"message": f"Parking spot {spot_id} has been occupied"}

@app.post('/parkingspot/{spot_id}/vacate')
def vacate_parking_spot(spot_id: int):
    parking_lot.vacant_spot(spot_id)
    return {"message": f"Parking spot {spot_id} is vacant"}

@app.post('/scam')
def scan_parking_lot():
    available_spots = scanner.scan_parking_lot()
    return {"message": "Parking Lot scanned.", "available spots": available_spots}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)