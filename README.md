# Parking Spot Monitor

The Parking Lot Monitor is a Python program designed to connect to an external camera, scan a parking lot, and notify you via text message whenever a vacant parking spot is detected. This repository provides the source code for the program along with a FastAPI implementation for building a RESTful API to interact with the parking lot data

## Features

- Connects to external camera to scan the parking lot video feed
- Detects available parking spots by analyzing occupancy status
- Notifies you via text message when a vacant spot is found
- Provides a RESTful API for accessing and updating parking lot data


## Requirements

Before running the Parking Lot Scanner Program, ensure that you have the following dependencies installed:

- Python 3.x
- FastAPI
- uvicorn

## Installation

1. Clone this repository to your local machine using the following command:


git clone https://github.com/your-username/parking-lot-scanner.git


2. Navigate to the project Directory

cd parking-lot-scanner


3. Install required Python dependencies

pip install -r requirements.txt

## Usage

1. Make sure your camera is properly connected to your system
2. Run the FastAPI server using the following command:

uvicorn main:app --reload

3. Access API endpoints in your browser or using API testing tools like Postman.
- API base URL: 'https://localhost:8000'

### API Endpoints

- `Get /`: Get a welcome message.
- `Get /parking_lot`: Get current parking lot data.
- `Get /parking_lot/{spot_id}`: Get information about a specific parking spot.
- `Put /parking_lot/{spot_id}`: Update the occupancy status of a parking spot.
- `Post /parking_lot/scan`: Scan the parking lot and get a list of available spots.

4. Customize the 'NotificationManager' class to integrate with your preferred method of sending text messages. 

5. Modify the code as needed to fit your specific parking lot setup and requirements. 