# This file contains the Classes that will be used for the project

class ParkingSpot:
    def __init__(self, spot_id):
        self.spot_id = spot_id
        self.is_occupied = False

class ParkingLot:
    def __init__(self):
        self.spots = []
    
    def add_spots(self, spot):
        self.spots.append(spot)

    def occupy_spot(self, spot_id):
        for spot in self.spots:
            if spot.spot_id == spot_id:
                spot.is_occupied = True
                break
    
    def vacate_spot(self, spot_id):
        for spot in self.spots:
            if spot.spot_id == spot_id:
                spot.is_occupied = False
                break

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