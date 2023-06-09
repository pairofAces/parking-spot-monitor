from fastapi import FastAPI, HTTPException
import uvicorn
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

# updating endpoint to get the most recent parking spot status
@app.put('/parkinglot/{spot_id}')
def update_parking_spot(spot_id: int, is_occupied:bool):
    # This should take care of the logic of either case of a parking spot
    # being occupied or vacant
    spot = parking_lot.get_spot_from_id(spot_id)
    if spot:
        spot.is_occupied = is_occupied
        parking_lot.save_to_json('parking_lot.json')

        if is_occupied:
            notification_manager.send_notification(f"Parking spot {spot_id} is now occupied")
        else:
            notification_manager.send_notification(f"Parking spot {spot_id} is vacant")
        
        return {"message": f"Parking spot {spot_id} updated successfully"}
    else:
        raise HTTPException(status_code=404, detail=f"Parking spot {spot_id} not found")

'''
@app.post('/parkingspot/{spot_id}/occupy')
def occupy_parking_spot(spot_id: int):
    # Update this method!!!
    parking_lot.occupy_spot(spot_id)
    return {"message": f"Parking spot {spot_id} has been occupied"}

@app.post('/parkingspot/{spot_id}/vacate')
def vacate_parking_spot(spot_id: int):
    parking_lot.vacant_spot(spot_id)
    return {"message": f"Parking spot {spot_id} is vacant"}
'''

@app.post('/scan')
def scan_parking_lot():
    available_spots = scanner.scan_parking_lot()
    return {"message": "Parking Lot scanned.", "available spots": available_spots}

if __name__ == "__main__":
    loaded_parking_lot = ParkingLot.load_from_json('parking_lot.json')
    if loaded_parking_lot:
        parking_lot = loaded_parking_lot
    else:
        for i in range(1,26):
            spot = ParkingSpot(i)
            parking_lot.add_spot(spot)

    uvicorn.run(app, host="0.0.0.0", port=8000)