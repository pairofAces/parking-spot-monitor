# This file contains the Classes that will be used for the project
import json

class ParkingSpot:
    def __init__(self, spot_id):
        self.spot_id = spot_id
        self.is_occupied = False
    
    def to_dict(self):
        return {
            'spot_id': self.spot_id,
            'is_occupied': self.is_occupied
        }
    
    @classmethod
    def from_dict(cls, data):
        spot_id = data['spot_id']
        is_occupied = data['is_occupied']
        spot = cls(spot_id)
        spot.is_occupied = is_occupied
        return spot

class ParkingLot:
    def __init__(self):
        self.spots = []
    
    def add_spot(self, spot):
        self.spots.append(spot)

    def to_dict(self):
        return {
            'spots': [spot.to_dict() for spot in self.spots]
        }
    
    @classmethod
    def from_dict(cls, data):
        parkinglot = cls()
        for spot_data in data['spots']:
            spot = ParkingSpot.from_dict(spot_data)
            parkinglot.add_spot(spot)
        return parkinglot
    
    def save_to_json(self, filename):
        data = self.to_dict()
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    
    @classmethod
    def load_from_json(cls, filename):
        try:
            with open(filename, 'w') as file:
                data = json.load(file)
        except FileNotFoundError:
            return None
        return cls.from_dict(data) if data else None
    
    def get_spot_from_id(self, spot_id):
        for spot in self.spots:
            if spot_id == spot:
                return spot
        return None

    def occupy_spot(self, spot_id):
        spot = self.get_spot_from_id(spot_id)
        if spot:
            spot.is_occupied = True
        return spot
    
    def vacate_spot(self, spot_id):
        spot = self.get_spot_from_id(spot_id)
        if spot:
            spot.is_occupied = False
        return spot

class ParkingLotScanner:
    def __init__(self, parking_lot, notification_manager):
        # initialize variables and setup connections to the camera
        self.parking_lot = parking_lot
        self.notification_manager = notification_manager
        pass

    def scan_parking_lot(self):
        # Begin scanning the parking lot video feed 
        # and detecting available parking spots
        available_spots = []
        for spot in self.parking_lot.spots:
            if not spot.is_occupied:
                available_spots.append(spot.spot_id)
        return available_spots
    
    def check_and_send_notification(self):
        available_spots = self.scan_parking_lot()
        if available_spots:
            message = f"Parking spots {available_spots} are available."
            self.notification_manager.send_notifcation(message)

class NotificationManager:
    @staticmethod
    def send_notification(message):
        # Send notification to the users smartphone about the
        # availablity of a parking spot
        print("Sending notification:", message)