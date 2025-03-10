# Farm Calendar API Documentation

# Endpoint: /api/v1/AddRawMaterialOperations/

## GET
Endpoint operation description: Api v1 addrawmaterialoperations list.

### Parameters

 * activity_type (string): ID of the farm calendar activity..
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * title (string): title of the farm calendar activity..

## POST
Endpoint operation description: Api v1 addrawmaterialoperations create.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/AddRawMaterialOperations/{id}/

## GET
Endpoint operation description: Api v1 addrawmaterialoperations retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Add Raw Material Operation..

## PUT
Endpoint operation description: Api v1 addrawmaterialoperations update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Add Raw Material Operation..

## PATCH
Endpoint operation description: Api v1 addrawmaterialoperations partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Add Raw Material Operation..

## DELETE
Endpoint operation description: Api v1 addrawmaterialoperations destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Add Raw Material Operation..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/AgriculturalMachines/

## GET
Endpoint operation description: Api v1 agriculturalmachines list.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * name (string): name of the asset..
 * parcel (string): The parcel.
 * status (integer): * `0` - Inactive * `1` - Active * `2` - Deleted.

## POST
Endpoint operation description: Api v1 agriculturalmachines create.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/AgriculturalMachines/{id}/

## GET
Endpoint operation description: Api v1 agriculturalmachines retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Farm Machine..

## PUT
Endpoint operation description: Api v1 agriculturalmachines update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Farm Machine..

## PATCH
Endpoint operation description: Api v1 agriculturalmachines partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Farm Machine..

## DELETE
Endpoint operation description: Api v1 agriculturalmachines destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Farm Machine..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/CompostOperations/

## GET
Endpoint operation description: Api v1 compostoperations list.

### Parameters

 * activity_type (string): ID of the farm calendar activity..
 * compost_pile_id (string): The compost pile id.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * title (string): title of the farm calendar activity..

## POST
Endpoint operation description: Api v1 compostoperations create.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/CompostOperations/{compost_operation_pk}/AddRawMaterialOperations/

## GET
Endpoint operation description: Api v1 compostoperations addrawmaterialoperations list.

### Parameters

 * activity_type (string): ID of the farm calendar activity..
 * **compost_operation_pk** (string)[Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * title (string): title of the farm calendar activity..

## POST
Endpoint operation description: Api v1 compostoperations addrawmaterialoperations create.

### Parameters

 * **compost_operation_pk** (string)[Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/CompostOperations/{compost_operation_pk}/AddRawMaterialOperations/{id}/

## GET
Endpoint operation description: Api v1 compostoperations addrawmaterialoperations retrieve.

### Parameters

 * **compost_operation_pk** (string)[Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Add Raw Material Operation..

## PUT
Endpoint operation description: Api v1 compostoperations addrawmaterialoperations update.

### Parameters

 * **compost_operation_pk** (string)[Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Add Raw Material Operation..

## PATCH
Endpoint operation description: Api v1 compostoperations addrawmaterialoperations partial update.

### Parameters

 * **compost_operation_pk** (string)[Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Add Raw Material Operation..

## DELETE
Endpoint operation description: Api v1 compostoperations addrawmaterialoperations destroy.

### Parameters

 * **compost_operation_pk** (string)[Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Add Raw Material Operation..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/CompostOperations/{compost_operation_pk}/CompostTurningOperations/

## GET
Endpoint operation description: Api v1 compostoperations compostturningoperations list.

### Parameters

 * activity_type (string): ID of the farm calendar activity..
 * **compost_operation_pk** (string)[Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * title (string): title of the farm calendar activity..

## POST
Endpoint operation description: Api v1 compostoperations compostturningoperations create.

### Parameters

 * **compost_operation_pk** (string)[Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/CompostOperations/{compost_operation_pk}/CompostTurningOperations/{id}/

## GET
Endpoint operation description: Api v1 compostoperations compostturningoperations retrieve.

### Parameters

 * **compost_operation_pk** (string)[Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Compost Turning Operation..

## PUT
Endpoint operation description: Api v1 compostoperations compostturningoperations update.

### Parameters

 * **compost_operation_pk** (string)[Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Compost Turning Operation..

## PATCH
Endpoint operation description: Api v1 compostoperations compostturningoperations partial update.

### Parameters

 * **compost_operation_pk** (string)[Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Compost Turning Operation..

## DELETE
Endpoint operation description: Api v1 compostoperations compostturningoperations destroy.

### Parameters

 * **compost_operation_pk** (string)[Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Compost Turning Operation..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/CompostOperations/{compost_operation_pk}/IrrigationOperations/

## GET
Endpoint operation description: Api v1 compostoperations irrigationoperations list.

### Parameters

 * activity_type (string): ID of the farm calendar activity..
 * **compost_operation_pk** (string)[Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * responsible_agent (string): The responsible agent for this activity..
 * title (string): title of the farm calendar activity..

## POST
Endpoint operation description: Api v1 compostoperations irrigationoperations create.

### Parameters

 * **compost_operation_pk** (string)[Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/CompostOperations/{compost_operation_pk}/IrrigationOperations/{id}/

## GET
Endpoint operation description: Api v1 compostoperations irrigationoperations retrieve.

### Parameters

 * **compost_operation_pk** (string)[Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Irrigation Operation..

## PUT
Endpoint operation description: Api v1 compostoperations irrigationoperations update.

### Parameters

 * **compost_operation_pk** (string)[Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Irrigation Operation..

## PATCH
Endpoint operation description: Api v1 compostoperations irrigationoperations partial update.

### Parameters

 * **compost_operation_pk** (string)[Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Irrigation Operation..

## DELETE
Endpoint operation description: Api v1 compostoperations irrigationoperations destroy.

### Parameters

 * **compost_operation_pk** (string)[Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Irrigation Operation..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/CompostOperations/{compost_operation_pk}/Observations/

## GET
Endpoint operation description: Api v1 compostoperations observations list.

### Parameters

 * activity_type (string): ID of the farm calendar activity..
 * **compost_operation_pk** (string)[Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * responsible_agent (string): The responsible agent for this activity..
 * title (string): title of the farm calendar activity..

## POST
Endpoint operation description: Api v1 compostoperations observations create.

### Parameters

 * **compost_operation_pk** (string)[Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/CompostOperations/{compost_operation_pk}/Observations/{id}/

## GET
Endpoint operation description: Api v1 compostoperations observations retrieve.

### Parameters

 * **compost_operation_pk** (string)[Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Observation..

## PUT
Endpoint operation description: Api v1 compostoperations observations update.

### Parameters

 * **compost_operation_pk** (string)[Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Observation..

## PATCH
Endpoint operation description: Api v1 compostoperations observations partial update.

### Parameters

 * **compost_operation_pk** (string)[Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Observation..

## DELETE
Endpoint operation description: Api v1 compostoperations observations destroy.

### Parameters

 * **compost_operation_pk** (string)[Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Observation..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/CompostOperations/{id}/

## GET
Endpoint operation description: Api v1 compostoperations retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Compost Operation..

## PUT
Endpoint operation description: Api v1 compostoperations update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Compost Operation..

## PATCH
Endpoint operation description: Api v1 compostoperations partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Compost Operation..

## DELETE
Endpoint operation description: Api v1 compostoperations destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Compost Operation..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/CompostTurningOperations/

## GET
Endpoint operation description: Api v1 compostturningoperations list.

### Parameters

 * activity_type (string): ID of the farm calendar activity..
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * title (string): title of the farm calendar activity..

## POST
Endpoint operation description: Api v1 compostturningoperations create.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/CompostTurningOperations/{id}/

## GET
Endpoint operation description: Api v1 compostturningoperations retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Compost Turning Operation..

## PUT
Endpoint operation description: Api v1 compostturningoperations update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Compost Turning Operation..

## PATCH
Endpoint operation description: Api v1 compostturningoperations partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Compost Turning Operation..

## DELETE
Endpoint operation description: Api v1 compostturningoperations destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Compost Turning Operation..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/CropGrowthStageObservations/

## GET
Endpoint operation description: Api v1 cropgrowthstageobservations list.

### Parameters

 * activity_type (string): ID of the farm calendar activity..
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * responsible_agent (string): The responsible agent for this activity..
 * title (string): title of the farm calendar activity..

## POST
Endpoint operation description: Api v1 cropgrowthstageobservations create.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/CropGrowthStageObservations/{id}/

## GET
Endpoint operation description: Api v1 cropgrowthstageobservations retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Crop Growth Stage Observation..

## PUT
Endpoint operation description: Api v1 cropgrowthstageobservations update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Crop Growth Stage Observation..

## PATCH
Endpoint operation description: Api v1 cropgrowthstageobservations partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Crop Growth Stage Observation..

## DELETE
Endpoint operation description: Api v1 cropgrowthstageobservations destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Crop Growth Stage Observation..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/CropProtectionOperations/

## GET
Endpoint operation description: Api v1 cropprotectionoperations list.

### Parameters

 * activity_type (string): ID of the farm calendar activity..
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * responsible_agent (string): The responsible agent for this activity..
 * title (string): title of the farm calendar activity..

## POST
Endpoint operation description: Api v1 cropprotectionoperations create.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/CropProtectionOperations/{id}/

## GET
Endpoint operation description: Api v1 cropprotectionoperations retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Crop Protection Operation..

## PUT
Endpoint operation description: Api v1 cropprotectionoperations update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Crop Protection Operation..

## PATCH
Endpoint operation description: Api v1 cropprotectionoperations partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Crop Protection Operation..

## DELETE
Endpoint operation description: Api v1 cropprotectionoperations destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Crop Protection Operation..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/CropStressIndicatorObservations/

## GET
Endpoint operation description: Api v1 cropstressindicatorobservations list.

### Parameters

 * activity_type (string): ID of the farm calendar activity..
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * responsible_agent (string): The responsible agent for this activity..
 * title (string): title of the farm calendar activity..

## POST
Endpoint operation description: Api v1 cropstressindicatorobservations create.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/CropStressIndicatorObservations/{id}/

## GET
Endpoint operation description: Api v1 cropstressindicatorobservations retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Crop Stress Indicator Observation..

## PUT
Endpoint operation description: Api v1 cropstressindicatorobservations update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Crop Stress Indicator Observation..

## PATCH
Endpoint operation description: Api v1 cropstressindicatorobservations partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Crop Stress Indicator Observation..

## DELETE
Endpoint operation description: Api v1 cropstressindicatorobservations destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Crop Stress Indicator Observation..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/Farm/

## GET
Endpoint operation description: Api v1 farm list.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * name (string): name of the asset..
 * status (integer): * `0` - Inactive * `1` - Active * `2` - Deleted.

## POST
Endpoint operation description: Api v1 farm create.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/Farm/{id}/

## GET
Endpoint operation description: Api v1 farm retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Farm..

## PUT
Endpoint operation description: Api v1 farm update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Farm..

## PATCH
Endpoint operation description: Api v1 farm partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Farm..

## DELETE
Endpoint operation description: Api v1 farm destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Farm..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/FarmAnimals/

## GET
Endpoint operation description: Api v1 farmanimals list.

### Parameters

 * animal_group (string): The animal group.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * name (string): name of the asset..
 * parcel (string): The parcel.
 * status (integer): * `0` - Inactive * `1` - Active * `2` - Deleted.

## POST
Endpoint operation description: Api v1 farmanimals create.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/FarmAnimals/{id}/

## GET
Endpoint operation description: Api v1 farmanimals retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Farm Animal..

## PUT
Endpoint operation description: Api v1 farmanimals update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Farm Animal..

## PATCH
Endpoint operation description: Api v1 farmanimals partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Farm Animal..

## DELETE
Endpoint operation description: Api v1 farmanimals destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Farm Animal..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/FarmCalendarActivities/

## GET
Endpoint operation description: Api v1 farmcalendaractivities list.

### Parameters

 * activity_type (string): ID of the farm calendar activity..
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * responsible_agent (string): The responsible agent for this activity..
 * title (string): title of the farm calendar activity..

## POST
Endpoint operation description: Api v1 farmcalendaractivities create.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/FarmCalendarActivities/{id}/

## GET
Endpoint operation description: Api v1 farmcalendaractivities retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Farm Activity..

## PUT
Endpoint operation description: Api v1 farmcalendaractivities update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Farm Activity..

## PATCH
Endpoint operation description: Api v1 farmcalendaractivities partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Farm Activity..

## DELETE
Endpoint operation description: Api v1 farmcalendaractivities destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Farm Activity..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/FarmCalendarActivityTypes/

## GET
Endpoint operation description: Api v1 farmcalendaractivitytypes list.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * name (string): name of the asset..

## POST
Endpoint operation description: Api v1 farmcalendaractivitytypes create.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/FarmCalendarActivityTypes/{id}/

## GET
Endpoint operation description: Api v1 farmcalendaractivitytypes retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this farm calendar activity type..

## PUT
Endpoint operation description: Api v1 farmcalendaractivitytypes update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this farm calendar activity type..

## PATCH
Endpoint operation description: Api v1 farmcalendaractivitytypes partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this farm calendar activity type..

## DELETE
Endpoint operation description: Api v1 farmcalendaractivitytypes destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this farm calendar activity type..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/FarmCrops/

## GET
Endpoint operation description: Api v1 farmcrops list.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * growth_stage (string): The growth stage.
 * name (string): name of the asset..
 * parcel (string): The parcel.
 * species (string): The species.
 * status (integer): * `0` - Inactive * `1` - Active * `2` - Deleted.
 * variety (string): The variety.

## POST
Endpoint operation description: Api v1 farmcrops create.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/FarmCrops/{id}/

## GET
Endpoint operation description: Api v1 farmcrops retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Farm Crop..

## PUT
Endpoint operation description: Api v1 farmcrops update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Farm Crop..

## PATCH
Endpoint operation description: Api v1 farmcrops partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Farm Crop..

## DELETE
Endpoint operation description: Api v1 farmcrops destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Farm Crop..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/FarmParcels/

## GET
Endpoint operation description: Api v1 farmparcels list.

### Parameters

 * farm (string): The farm.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * geo_id (string): The geo id.
 * identifier (string): The identifier.
 * parcel_type (string): The parcel type.
 * status (integer): * `0` - Inactive * `1` - Active * `2` - Deleted.

## POST
Endpoint operation description: Api v1 farmparcels create.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/FarmParcels/{id}/

## GET
Endpoint operation description: Api v1 farmparcels retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Farm Parcel..

## PUT
Endpoint operation description: Api v1 farmparcels update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Farm Parcel..

## PATCH
Endpoint operation description: Api v1 farmparcels partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Farm Parcel..

## DELETE
Endpoint operation description: Api v1 farmparcels destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Farm Parcel..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/FertilizationOperations/

## GET
Endpoint operation description: Api v1 fertilizationoperations list.

### Parameters

 * activity_type (string): ID of the farm calendar activity..
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * responsible_agent (string): The responsible agent for this activity..
 * title (string): title of the farm calendar activity..

## POST
Endpoint operation description: Api v1 fertilizationoperations create.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/FertilizationOperations/{id}/

## GET
Endpoint operation description: Api v1 fertilizationoperations retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Fertilization Operation..

## PUT
Endpoint operation description: Api v1 fertilizationoperations update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Fertilization Operation..

## PATCH
Endpoint operation description: Api v1 fertilizationoperations partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Fertilization Operation..

## DELETE
Endpoint operation description: Api v1 fertilizationoperations destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Fertilization Operation..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/Fertilizers/

## GET
Endpoint operation description: Api v1 fertilizers list.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * name (string): name of the asset..
 * status (integer): * `0` - Inactive * `1` - Active * `2` - Deleted.

## POST
Endpoint operation description: Api v1 fertilizers create.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/Fertilizers/{id}/

## GET
Endpoint operation description: Api v1 fertilizers retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Fertilizer..

## PUT
Endpoint operation description: Api v1 fertilizers update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Fertilizer..

## PATCH
Endpoint operation description: Api v1 fertilizers partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Fertilizer..

## DELETE
Endpoint operation description: Api v1 fertilizers destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Fertilizer..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/IrrigationOperations/

## GET
Endpoint operation description: Api v1 irrigationoperations list.

### Parameters

 * activity_type (string): ID of the farm calendar activity..
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * responsible_agent (string): The responsible agent for this activity..
 * title (string): title of the farm calendar activity..

## POST
Endpoint operation description: Api v1 irrigationoperations create.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/IrrigationOperations/{id}/

## GET
Endpoint operation description: Api v1 irrigationoperations retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Irrigation Operation..

## PUT
Endpoint operation description: Api v1 irrigationoperations update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Irrigation Operation..

## PATCH
Endpoint operation description: Api v1 irrigationoperations partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Irrigation Operation..

## DELETE
Endpoint operation description: Api v1 irrigationoperations destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Irrigation Operation..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/Observations/

## GET
Endpoint operation description: Api v1 observations list.

### Parameters

 * activity_type (string): ID of the farm calendar activity..
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * responsible_agent (string): The responsible agent for this activity..
 * title (string): title of the farm calendar activity..

## POST
Endpoint operation description: Api v1 observations create.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/Observations/{id}/

## GET
Endpoint operation description: Api v1 observations retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Observation..

## PUT
Endpoint operation description: Api v1 observations update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Observation..

## PATCH
Endpoint operation description: Api v1 observations partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Observation..

## DELETE
Endpoint operation description: Api v1 observations destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Observation..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/Pesticides/

## GET
Endpoint operation description: Api v1 pesticides list.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * name (string): name of the asset..
 * status (integer): * `0` - Inactive * `1` - Active * `2` - Deleted.

## POST
Endpoint operation description: Api v1 pesticides create.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```

# Endpoint: /api/v1/Pesticides/{id}/

## GET
Endpoint operation description: Api v1 pesticides retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Pesticide..

## PUT
Endpoint operation description: Api v1 pesticides update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Pesticide..

## PATCH
Endpoint operation description: Api v1 pesticides partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Pesticide..

## DELETE
Endpoint operation description: Api v1 pesticides destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string)[Required]: A UUID string identifying this Pesticide..

## Example Response (GET/DELETE)

```json

```

## Example Request/Response (POST/PUT/PATCH)

```json

```
