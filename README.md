# Driver Car Park App

With this API you can easily register new drivers / vehicles and manage them.

## Setup
[Here is detailed guide](SETUP.md) on how to setup the app

## Overview
Made with Pure django (no django rest framework, no forms, no templates)


You should always use JSON (application/json) in your requests to receive or send data. Response data also uses JSON format for repsentation.



####common_functional is folder that consist of helpers and handlers:

* helpers.py - common serving functions for data formatting and making response.
* handlers.py - Class based fucntions to serve all the basic CRUD operations. (you should override this class in specific view if you have some app-view-specific logic that differs from common)



## Authentication
There is no authentication for endpoints.

## Error Codes
* ('Bad request', 400)
* ('Not found', 404)
* ('Created successfully', 201)
* ('Updated successfully', 200)
* ('Deleted successfully', 200)

###View specific codes (Vehicles):
* ('Driver successfully set', 200)
* ('Driver successfully unset', 200)
* ('Driver unavailable', 404)


## API usage and examples:

### GET /vehicles/vehicle/

get list of all vehicles
```
localhost:8090/vehicles/vehicle/

curl --location --request GET 'localhost:8090/vehicles/vehicle/'
```

### GET /drivers/driver/

get list of all drivers
```
localhost:8090/drivers/driver/

curl --location --request GET 'localhost:8090/drivers/driver/'
```

### GET /vehicles/vehicle/<id:int\>/

get info for specific vehicle
```
localhost:8090/vehicles/vehicle/11/

curl --location --request GET 'localhost:8090/vehicles/vehicle/11/'
```

### GET /drivers/driver/<id:int\>/

get info for specific driver
```
localhost:8090/drivers/driver/36/

curl --location --request GET 'localhost:8090/drivers/driver/36/'
```

### GET /vehicles/vehicle/?with_drivers=yes

get all the vehicles with drivers

```
localhost:8090/vehicles/vehicle/?with_drivers=yes

curl --location --request GET 'localhost:8090/vehicles/vehicle/?with_drivers=yes'
```

### GET /vehicles/vehicle/?with_drivers=no

get all the vehicles without drivers

```
localhost:8090/vehicles/vehicle/?with_drivers=no

curl --location --request GET 'localhost:8090/vehicles/vehicle/?with_drivers=no'
```

### GET /drivers/driver/?created_at__lte=<date:dd-mm-yyyy\>

show all the drivers created before the date specified

```
localhost:8090/drivers/driver/?created_at__lte=14-12-2021

curl --location --request GET 'localhost:8090/drivers/driver/?created_at__lte=14-12-2021'
```

### GET /drivers/driver/?created_at__gte=<date:dd-mm-yyyy\>

show all the drivers created after the date specified

```
localhost:8090/drivers/driver/?created_at__gte=14-12-2021

curl --location --request GET 'localhost:8090/drivers/driver/?created_at__gte=14-12-2021'
```

### POST /vehicles/vehicle/

create a new vehicle

```
localhost:8090/vehicles/vehicle/

curl --location --request POST 'localhost:8090/vehicles/vehicle/' \
--header 'Content-Type: application/json' \
--data-raw '{
"make":"2017",
"model": "Mersedes Benz G5",
"plate_number": "AH 7255 OK"
}'
```

### POST /drivers/driver/

create a new driver

```
localhost:8090/drivers/driver/

curl --location --request POST 'localhost:8090/drivers/driver/' \
--header 'Content-Type: application/json' \
--data-raw '{
"first_name":"Sergii",
"last_name": "Klochko"
}'
```

### POST /vehicles/set_driver/<id:int\>/

set or unset driver for specified vehicle

```
localhost:8090/vehicles/set_driver/11/

curl --location --request POST 'localhost:8090/vehicles/set_driver/11/' \
--header 'Content-Type: application/json' \
--data-raw '{
"first_name":"Sergii",
"last_name": "Klochko"
}'
```

### PUT /vehicles/vehicle/<id:int\>/

edit or create if not exist a new vehicle


```
localhost:8090/vehicles/vehicle/11/

curl --location --request PUT 'localhost:8090/vehicles/vehicle/11/' \
--header 'Content-Type: application/json' \
--data-raw '{
"plate_number":"AO 1122 IK"
}'
```

### PUT /drivers/driver/<id:int\>/

edit or create if not exist a new driver


```
localhost:8090/drivers/driver/36/

curl --location --request PUT 'localhost:8090/drivers/driver/36/' \
--header 'Content-Type: application/json' \
--data-raw '{
"first_name":"Sergii",
"last_name": "Klochko"
}'
```

### DEL /vehicles/vehicle/<id:int\>/

delete specified vehicle

```
localhost:8090/vehicles/vehicle/12/

curl --location --request DELETE 'localhost:8090/vehicles/vehicle/12/'
```

### DEL /drivers/driver/<id:int\>/

delete specified driver

```
localhost:8090/drivers/driver/36/

curl --location --request DELETE 'localhost:8090/drivers/driver/36/'
```