# This file contains the Classes that will be used for the project

class ParkingSpot:
    def __init__(self, spot_id):
        self.spot_id = spot_id
        self.is_occupied = False



class ParkingLotScanner:
    def __init__(self):
        # initialize variables and setup connections to the camera
        pass

    def start_scanning(self):
        # Begin scanning the parking lot video feed 
        # and detecting available parking spots
        pass

    def stop_scanning(self):
        # Stop the scanning process
        pass

    def detect_available_spots(self, frame):
        # Perform image processing on the provided video feed
        # to detect available parking spots
        pass

class NotificationManager:
    @staticmethod
    def send_notification(message):
        # Send notification to the users smartphone about the
        # availablity of a parking spot
        print("Sending notification:", message)