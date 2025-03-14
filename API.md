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

## Example Response (GET)

```json
{
  "@context": [
    "https://w3id.org/ocsm/main-context.jsonld"
  ],
  "@graph": [
    {
      "@type": "AddRawMaterialOperation",
      "@id": "urn:farmcalendar:AddRawMaterialOperation:45dae5d5-f930-48e2-bd4d-40ef8cff25e8",
      "activityType": {
        "@type": "FarmCalendarActivityType",
        "@id": "urn:farmcalendar:FarmCalendarActivityType:00000000-0000-0000-0000-000000000007"
      },
      "title": "Add Raw Material Operation",
      "details": "some details",
      "hasStartDatetime": "2025-02-21T12:05:02Z",
      "hasEndDatetime": null,
      "responsibleAgent": null,
      "usesAgriculturalMachinery": [],
      "hasCompostMaterial": [
        {
          "@type": "CompostMaterial",
          "@id": "urn:farmcalendar:CompostMaterial:7eced1b6-b79b-4184-b688-68530e87ff1e",
          "typeName": "Straw",
          "quantityValue": {
            "@id": "urn:farmcalendar:QuantityValue:3e06dc96-0c81-5698-b37d-58a5ea781d13",
            "@type": "QuantityValue",
            "unit": "kg",
            "numericValue": 10
          }
        },
        {
          "@type": "CompostMaterial",
          "@id": "urn:farmcalendar:CompostMaterial:116b90b7-a3e5-4a6c-8a3c-f97d440f18da",
          "typeName": "hay",
          "quantityValue": {
            "@id": "urn:farmcalendar:QuantityValue:9b0c0018-c507-5836-81bb-f4ab3cf732ea",
            "@type": "QuantityValue",
            "unit": "kg",
            "numericValue": 2
          }
        }
      ]
    }
  ]
}

```

## Example Request (POST/PUT/PATCH)

```json
{
    "@type": "AddRawMaterialOperation",
    "activityType": {
        "@type": "FarmCalendarActivityType",
        "@id": "urn:farmcalendar:FarmCalendarActivityType:00000000-0000-0000-0000-000000000007"
    },
    "title": "Add Raw Material Operation",
    "details": "some details",
    "hasStartDatetime": "2025-02-21T12:05:02Z",
    "hasEndDatetime": null,
    "responsibleAgent": null,
    "usesAgriculturalMachinery": [],
    "hasCompostMaterial": [
    {
        "@type": "CompostMaterial",
        "@id": "urn:farmcalendar:CompostMaterial:7eced1b6-b79b-4184-b688-68530e87ff1e",
        "typeName": "Straw",
        "quantityValue": {
            "@id": "urn:farmcalendar:QuantityValue:3e06dc96-0c81-5698-b37d-58a5ea781d13",
            "@type": "QuantityValue",
            "unit": "kg",
            "numericValue": 10
        }
    },
    {
        "@type": "CompostMaterial",
        "@id": "urn:farmcalendar:CompostMaterial:116b90b7-a3e5-4a6c-8a3c-f97d440f18da",
        "typeName": "hay",
        "quantityValue": {
            "@id": "urn:farmcalendar:QuantityValue:9b0c0018-c507-5836-81bb-f4ab3cf732ea",
            "@type": "QuantityValue",
            "unit": "kg",
            "numericValue": 2
        }
    }
    ]
}
```


# Endpoint: /api/v1/AddRawMaterialOperations/{id}/

## GET
Endpoint operation description: Api v1 addrawmaterialoperations retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Add Raw Material Operation..

## PUT
Endpoint operation description: Api v1 addrawmaterialoperations update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Add Raw Material Operation..

## PATCH
Endpoint operation description: Api v1 addrawmaterialoperations partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Add Raw Material Operation..

## DELETE
Endpoint operation description: Api v1 addrawmaterialoperations destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Add Raw Material Operation..

## Example Response (GET)
Request/response similar to this entity's (List endpoint)[API.md/#endpoint-apiv1addrawmaterialoperations]

## Example Request (POST/PUT/PATCH)
Request/response similar to this entity's (List endpoint)[API.md/#endpoint-apiv1addrawmaterialoperations]

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

## Example Response (GET)

```json
{
    "@context": [
        "https://w3id.org/ocsm/main-context.jsonld"
    ],
    "@graph": [
        {
            "@type": "AgriculturalMachine",
            "@id": "urn:farmcalendar:AgriculturalMachine:b03d5bf5-5d34-44c2-91c6-28835b941f7a",
            "name": "Some Machine",
            "description": "a machine",
            "hasAgriParcel": {
                "@type": "Parcel",
                "@id": "urn:farmcalendar:Parcel:00000000-0000-0000-0000-000000000001"
            },
            "purchase_date": "2025-03-11",
            "manufacturer": "The manufacturer",
            "model": "some model",
            "seria_number": "s1234",
            "status": 1,
            "invalidatedAtTime": null,
            "dateCreated": "2025-03-10T16:26:12.554609Z",
            "dateModified": "2025-03-10T16:26:12.554620Z"
        }
    ]
}
```

## Example Request (POST/PUT/PATCH)

```json
{
    "@type": "AgriculturalMachine",
    "name": "Some Machine",
    "description": "a machine",
    "hasAgriParcel": {
        "@type": "Parcel",
        "@id": "urn:farmcalendar:Parcel:00000000-0000-0000-0000-000000000001"
    },
    "purchase_date": "2025-03-11",
    "manufacturer": "The manufacturer",
    "model": "some model",
    "seria_number": "s1234",
    "status": 1,
    "invalidatedAtTime": null,
    "dateCreated": "2025-03-10T16:26:12.554609Z",
    "dateModified": "2025-03-10T16:26:12.554620Z"
}
```


# Endpoint: /api/v1/AgriculturalMachines/{id}/

## GET
Endpoint operation description: Api v1 agriculturalmachines retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Farm Machine..

## PUT
Endpoint operation description: Api v1 agriculturalmachines update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Farm Machine..

## PATCH
Endpoint operation description: Api v1 agriculturalmachines partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Farm Machine..

## DELETE
Endpoint operation description: Api v1 agriculturalmachines destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Farm Machine..

## Example Response (GET)

Request/response similar to this entity's (List endpoint)[API.md/#endpoint-apiv1agriculturalmachines]

## Example Request (POST/PUT/PATCH)

Request/response similar to this entity's (List endpoint)[API.md/#endpoint-apiv1agriculturalmachines]

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

## Example Response (GET)

```json
{
    "@context": [
        "https://w3id.org/ocsm/main-context.jsonld"
    ],
    "@graph": [
        {
            "@type": "CompostOperation",
            "@id": "urn:farmcalendar:CompostOperation:99896808-da5b-4e3b-90f2-fe509a4b519c",
            "activityType": {
                "@type": "FarmCalendarActivityType",
                "@id": "urn:farmcalendar:FarmCalendarActivityType:00000000-0000-0000-0000-000000000006"
            },
            "title": "Compost Operation",
            "details": "",
            "hasStartDatetime": "2025-02-21T11:45:39Z",
            "hasEndDatetime": "2025-02-21T18:47:00Z",
            "responsibleAgent": "me",
            "usesAgriculturalMachinery": [],
            "isOperatedOn": {
                "@type": "CompostPile",
                "@id": "urn:farmcalendar:CompostPile:pile123"
            },
            "hasNestedOperation": [
                {
                    "@type": "CompostTurningOperation",
                    "@id": "urn:farmcalendar:CompostTurningOperation:1fa6b780-90bb-459d-860d-cd9840f57c40"
                },
                {
                    "@type": "IrrigationOperation",
                    "@id": "urn:farmcalendar:IrrigationOperation:7e861f97-434d-4cb7-bf9c-fcfa28f8009c"
                },
                {
                    "@type": "AddRawMaterialOperation",
                    "@id": "urn:farmcalendar:AddRawMaterialOperation:45dae5d5-f930-48e2-bd4d-40ef8cff25e8"
                }
            ],
            "hasMeasurement": [
                {
                    "@type": "Observation",
                    "@id": "urn:farmcalendar:Observation:dbd06cd4-6704-4530-9a23-2ffa235f6d8a"
                }
            ]
        }
    ]
}
```

## Example Request (POST/PUT/PATCH)
```json
{
    "activityType": {
        "@type": "FarmCalendarActivityType",
        "@id": "urn:farmcalendar:FarmCalendarActivityType:00000000-0000-0000-0000-000000000006"
    },
    "title": "Compost Operation",
    "details": "",
    "hasStartDatetime": "2025-02-21T11:45:39Z",
    "hasEndDatetime": "2025-02-21T18:47:00Z",
    "responsibleAgent": "Some Farmer",
    "usesAgriculturalMachinery": [],
    "isOperatedOn": {
        "@type": "CompostPile",
        "@id": "urn:farmcalendar:CompostPile:pile123"
    }
}
```

# Endpoint: /api/v1/CompostOperations/{id}/

## GET
Endpoint operation description: Api v1 compostoperations retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Compost Operation..

## PUT
Endpoint operation description: Api v1 compostoperations update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Compost Operation..

## PATCH
Endpoint operation description: Api v1 compostoperations partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Compost Operation..

## DELETE
Endpoint operation description: Api v1 compostoperations destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Compost Operation..

## Example Response (GET)

Request/response similar to this entity (List endpoint)[API.md/#endpoint-apiv1compostoperations]

## Example Request (POST/PUT/PATCH)
Request/response similar to this entity (List endpoint)[API.md/#endpoint-apiv1compostoperations]

# Endpoint: /api/v1/CompostOperations/{compost_operation_pk}/AddRawMaterialOperations/
This endpoint is used to manage the nested AddRawMaterialOperations on a compost operation.

## GET
Endpoint operation description: Api v1 compostoperations addrawmaterialoperations list.

### Parameters

 * activity_type (string): ID of the farm calendar activity..
 * **compost_operation_pk** (string) [Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * title (string): title of the farm calendar activity..

## POST
Endpoint operation description: Api v1 compostoperations addrawmaterialoperations create.

### Parameters

 * **compost_operation_pk** (string) [Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..

## Example Response (GET)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1addrawmaterialoperations]

## Example Request (POST/PUT/PATCH)
Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1addrawmaterialoperations]

# Endpoint: /api/v1/CompostOperations/{compost_operation_pk}/AddRawMaterialOperations/{id}/

## GET
Endpoint operation description: Api v1 compostoperations addrawmaterialoperations retrieve.

### Parameters

 * **compost_operation_pk** (string) [Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Add Raw Material Operation..

## PUT
Endpoint operation description: Api v1 compostoperations addrawmaterialoperations update.

### Parameters

 * **compost_operation_pk** (string) [Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Add Raw Material Operation..

## PATCH
Endpoint operation description: Api v1 compostoperations addrawmaterialoperations partial update.

### Parameters

 * **compost_operation_pk** (string) [Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Add Raw Material Operation..

## DELETE
Endpoint operation description: Api v1 compostoperations addrawmaterialoperations destroy.

### Parameters

 * **compost_operation_pk** (string) [Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Add Raw Material Operation..

## Example Response (GET)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1addrawmaterialoperations]

## Example Request (POST/PUT/PATCH)
Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1addrawmaterialoperations]


# Endpoint: /api/v1/CompostOperations/{compost_operation_pk}/CompostTurningOperations/
This endpoint is used to manage the nested CompostTurningOperations on a compost operation.

## GET
Endpoint operation description: Api v1 compostoperations compostturningoperations list.

### Parameters

 * activity_type (string): ID of the farm calendar activity..
 * **compost_operation_pk** (string) [Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * title (string): title of the farm calendar activity..

## POST
Endpoint operation description: Api v1 compostoperations compostturningoperations create.

### Parameters

 * **compost_operation_pk** (string) [Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..

## Example Response (GET)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1compostturningoperations]

## Example Request (POST/PUT/PATCH)
Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1compostturningoperations]


# Endpoint: /api/v1/CompostOperations/{compost_operation_pk}/CompostTurningOperations/{id}/

## GET
Endpoint operation description: Api v1 compostoperations compostturningoperations retrieve.

### Parameters

 * **compost_operation_pk** (string) [Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Compost Turning Operation..

## PUT
Endpoint operation description: Api v1 compostoperations compostturningoperations update.

### Parameters

 * **compost_operation_pk** (string) [Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Compost Turning Operation..

## PATCH
Endpoint operation description: Api v1 compostoperations compostturningoperations partial update.

### Parameters

 * **compost_operation_pk** (string) [Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Compost Turning Operation..

## DELETE
Endpoint operation description: Api v1 compostoperations compostturningoperations destroy.

### Parameters

 * **compost_operation_pk** (string) [Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Compost Turning Operation..

## Example Response (GET)
Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1compostturningoperations]

## Example Request (POST/PUT/PATCH)
Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1compostturningoperations]


# Endpoint: /api/v1/CompostOperations/{compost_operation_pk}/IrrigationOperations/
This endpoint is used to manage the nested IrrigationOperations on a compost operation.

## GET
Endpoint operation description: Api v1 compostoperations irrigationoperations list.

### Parameters

 * activity_type (string): ID of the farm calendar activity..
 * **compost_operation_pk** (string) [Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * responsible_agent (string): The responsible agent for this activity..
 * title (string): title of the farm calendar activity..

## POST
Endpoint operation description: Api v1 compostoperations irrigationoperations create.

### Parameters

 * **compost_operation_pk** (string) [Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..

## Example Response (GET)
Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1irrigationoperations]

## Example Request (POST/PUT/PATCH)
Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1irrigationoperations]


# Endpoint: /api/v1/CompostOperations/{compost_operation_pk}/IrrigationOperations/{id}/

## GET
Endpoint operation description: Api v1 compostoperations irrigationoperations retrieve.

### Parameters

 * **compost_operation_pk** (string) [Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Irrigation Operation..

## PUT
Endpoint operation description: Api v1 compostoperations irrigationoperations update.

### Parameters

 * **compost_operation_pk** (string) [Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Irrigation Operation..

## PATCH
Endpoint operation description: Api v1 compostoperations irrigationoperations partial update.

### Parameters

 * **compost_operation_pk** (string) [Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Irrigation Operation..

## DELETE
Endpoint operation description: Api v1 compostoperations irrigationoperations destroy.

### Parameters

 * **compost_operation_pk** (string) [Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Irrigation Operation..

## Example Response (GET)
Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1irrigationoperations]

## Example Request (POST/PUT/PATCH)
Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1irrigationoperations]

# Endpoint: /api/v1/CompostOperations/{compost_operation_pk}/Observations/
This endpoint is used to manage the nested Observations on a compost operation.

## GET
Endpoint operation description: Api v1 compostoperations observations list.

### Parameters

 * activity_type (string): ID of the farm calendar activity..
 * **compost_operation_pk** (string) [Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * responsible_agent (string): The responsible agent for this activity..
 * title (string): title of the farm calendar activity..

## POST
Endpoint operation description: Api v1 compostoperations observations create.

### Parameters

 * **compost_operation_pk** (string) [Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..

## Example Response (GET)
Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1observations]

## Example Request (POST/PUT/PATCH)
Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1observations]

# Endpoint: /api/v1/CompostOperations/{compost_operation_pk}/Observations/{id}/

## GET
Endpoint operation description: Api v1 compostoperations observations retrieve.

### Parameters

 * **compost_operation_pk** (string) [Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Observation..

## PUT
Endpoint operation description: Api v1 compostoperations observations update.

### Parameters

 * **compost_operation_pk** (string) [Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Observation..

## PATCH
Endpoint operation description: Api v1 compostoperations observations partial update.

### Parameters

 * **compost_operation_pk** (string) [Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Observation..

## DELETE
Endpoint operation description: Api v1 compostoperations observations destroy.

### Parameters

 * **compost_operation_pk** (string) [Required]: The compost operation pk.
 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Observation..

## Example Response (GET)
Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1observations]

## Example Request (POST/PUT/PATCH)
Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1observations]

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

## Example Response (GET)


```json
{
    "@context": [
        "https://w3id.org/ocsm/main-context.jsonld"
    ],
    "@graph": [
        {
            "@type": "CompostTurningOperation",
            "@id": "urn:farmcalendar:CompostTurningOperation:1fa6b780-90bb-459d-860d-cd9840f57c40",
            "activityType": {
                "@type": "FarmCalendarActivityType",
                "@id": "urn:farmcalendar:FarmCalendarActivityType:00000000-0000-0000-0000-000000000008"
            },
            "title": "Compost Turning Operation",
            "details": "",
            "hasStartDatetime": "2025-02-21T11:45:57Z",
            "hasEndDatetime": null,
            "responsibleAgent": "Farmer",
            "usesAgriculturalMachinery": []
        },
        {
            "@type": "CompostTurningOperation",
            "@id": "urn:farmcalendar:CompostTurningOperation:afa6b780-92bb-459d-860f-cd9840f57d55",
            "activityType": {
                "@type": "FarmCalendarActivityType",
                "@id": "urn:farmcalendar:FarmCalendarActivityType:00000000-0000-0000-0000-000000000008"
            },
            "title": "Compost Turning Operation",
            "details": "",
            "hasStartDatetime": "2025-02-25T10:45:57Z",
            "hasEndDatetime": null,
            "responsibleAgent": "Farmer",
            "usesAgriculturalMachinery": []
        },
    ]
}

```

## Example Request (POST/PUT/PATCH)

```json

{
    "@type": "CompostTurningOperation",
    "activityType": {
        "@type": "FarmCalendarActivityType",
        "@id": "urn:farmcalendar:FarmCalendarActivityType:00000000-0000-0000-0000-000000000008"
    },
    "title": "Compost Turning Operation",
    "details": "",
    "hasStartDatetime": "2025-02-21T11:45:57Z",
    "hasEndDatetime": null,
    "responsibleAgent": "Farmer",
    "usesAgriculturalMachinery": []
}
```

# Endpoint: /api/v1/CompostTurningOperations/{id}/

## GET
Endpoint operation description: Api v1 compostturningoperations retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Compost Turning Operation..

## PUT
Endpoint operation description: Api v1 compostturningoperations update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Compost Turning Operation..

## PATCH
Endpoint operation description: Api v1 compostturningoperations partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Compost Turning Operation..

## DELETE
Endpoint operation description: Api v1 compostturningoperations destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Compost Turning Operation..

## Example Response (GET)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1compostturningoperations]

## Example Request (POST/PUT/PATCH)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1compostturningoperations]


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

## Example Response (GET)

```json
{
    "@context": [
        "https://w3id.org/ocsm/main-context.jsonld"
    ],
    "@graph": [
        {
            "@type": "CropGrowthStageObservation",
            "@id": "urn:farmcalendar:CropGrowthStageObservation:0cc526f6-ae17-41ef-86a4-e5541932c482",
            "activityType": {
                "@type": "FarmCalendarActivityType",
                "@id": "urn:farmcalendar:FarmCalendarActivityType:00000000-0000-0000-0000-000000000005"
            },
            "title": "Crop Growth Stage Observation",
            "details": "",
            "phenomenonTime": "2025-03-14T13:10:00Z",
            "madeBySensor": {},
            "hasAgriCrop": {
                "@type": "FarmCrop",
                "@id": "urn:farmcalendar:FarmCrop:0159de17-1c67-4ebd-92a5-51bc3b8d5c84"
            },
            "hasResult": {
                "@id": "urn:farmcalendar:QuantityValue:5a4474e6-a86b-5d64-b517-da2f4eebe5a0",
                "@type": "QuantityValue",
                "unit": null,
                "hasValue": "Sprouting"
            },
            "observedProperty": "growthStage"
        }
    ]
}

```

## Example Request (POST/PUT/PATCH)

```json
{
    "@type": "CropGrowthStageObservation",
    "activityType": {
        "@type": "FarmCalendarActivityType",
        "@id": "urn:farmcalendar:FarmCalendarActivityType:00000000-0000-0000-0000-000000000005"
    },
    "title": "Crop Growth Stage Observation",
    "details": "",
    "phenomenonTime": "2025-03-14T13:10:00Z",
    "madeBySensor": {},
    "hasAgriCrop": {
        "@type": "FarmCrop",
        "@id": "urn:farmcalendar:FarmCrop:0159de17-1c67-4ebd-92a5-51bc3b8d5c84"
    },
    "hasResult": {
        "@type": "QuantityValue",
        "unit": null,
        "hasValue": "Sprouting"
    },
    "observedProperty": "growthStage"

}
```

# Endpoint: /api/v1/CropGrowthStageObservations/{id}/

## GET
Endpoint operation description: Api v1 cropgrowthstageobservations retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Crop Growth Stage Observation..

## PUT
Endpoint operation description: Api v1 cropgrowthstageobservations update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Crop Growth Stage Observation..

## PATCH
Endpoint operation description: Api v1 cropgrowthstageobservations partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Crop Growth Stage Observation..

## DELETE
Endpoint operation description: Api v1 cropgrowthstageobservations destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Crop Growth Stage Observation..

## Example Response (GET)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1cropgrowthstageobservations]


## Example Request (POST/PUT/PATCH)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1cropgrowthstageobservations]


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

## Example Response (GET)

```json
{
    "@context": [
        "https://w3id.org/ocsm/main-context.jsonld"
    ],
    "@graph": [
        {
            "@type": "CropProtectionOperation",
            "@id": "urn:farmcalendar:CropProtectionOperation:aa62956c-9ac8-4ce5-a6e1-68e1ce223513",
            "activityType": {
                "@type": "FarmCalendarActivityType",
                "@id": "urn:farmcalendar:FarmCalendarActivityType:00000000-0000-0000-0000-000000000003"
            },
            "title": "Pesticides",
            "details": "",
            "hasStartDatetime": "2025-03-14T13:20:00Z",
            "hasEndDatetime": "2025-03-15T13:20:00Z",
            "responsibleAgent": "Farmer",
            "usesAgriculturalMachinery": [],
            "hasAppliedAmount": {
                "@id": "urn:farmcalendar:QuantityValue:e4e66fc3-e2cd-53e7-80ea-ef8960e060f6",
                "@type": "QuantityValue",
                "unit": "litres",
                "numericValue": 10.0
            },
            "usesPesticide": {
                "@type": "Pesticide",
                "@id": "urn:farmcalendar:Pesticide:00975c81-f923-45b1-b421-d4e9f2812545"
            },
            "operatedOn": {
                "@type": "Parcel",
                "@id": "urn:farmcalendar:Parcel:00000000-0000-0000-0000-000000000001"
            }
        }
    ]
}
```

## Example Request (POST/PUT/PATCH)

```json
{
    "@type": "CropProtectionOperation",
    "activityType": {
        "@type": "FarmCalendarActivityType",
        "@id": "urn:farmcalendar:FarmCalendarActivityType:00000000-0000-0000-0000-000000000003"
    },
    "title": "Pesticides",
    "details": "",
    "hasStartDatetime": "2025-03-14T13:20:00Z",
    "hasEndDatetime": "2025-03-15T13:20:00Z",
    "responsibleAgent": "Farmer",
    "usesAgriculturalMachinery": [],
    "hasAppliedAmount": {
        "@type": "QuantityValue",
        "unit": "litres",
        "numericValue": 10.0
    },
    "usesPesticide": {
        "@type": "Pesticide",
        "@id": "urn:farmcalendar:Pesticide:00975c81-f923-45b1-b421-d4e9f2812545"
    },
    "operatedOn": {
        "@type": "Parcel",
        "@id": "urn:farmcalendar:Parcel:00000000-0000-0000-0000-000000000001"
    }
}
```

# Endpoint: /api/v1/CropProtectionOperations/{id}/

## GET
Endpoint operation description: Api v1 cropprotectionoperations retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Crop Protection Operation..

## PUT
Endpoint operation description: Api v1 cropprotectionoperations update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Crop Protection Operation..

## PATCH
Endpoint operation description: Api v1 cropprotectionoperations partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Crop Protection Operation..

## DELETE
Endpoint operation description: Api v1 cropprotectionoperations destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Crop Protection Operation..

## Example Response (GET)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1cropprotectionoperations]

## Example Request (POST/PUT/PATCH)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1cropprotectionoperations]


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

## Example Response (GET)

```json
{
    "@context": [
        "https://w3id.org/ocsm/main-context.jsonld"
    ],
    "@graph": [
        {
            "@type": "CropStressIndicatorObservation",
            "@id": "urn:farmcalendar:CropStressIndicatorObservation:7e67dc08-5e00-4927-8788-38de06c2c8e3",
            "activityType": {
                "@type": "FarmCalendarActivityType",
                "@id": "urn:farmcalendar:FarmCalendarActivityType:00000000-0000-0000-0000-000000000004"
            },
            "title": "Crop Stress Indicator",
            "details": "",
            "phenomenonTime": "2025-03-13T13:25:00Z",
            "madeBySensor": {
                "@id": "urn:farmcalendar:Sensor:15786cae-f3a0-5712-a183-ce3a2fd24475",
                "@type": "Sensor",
                "name": "XYZ Sensor"
            },
            "hasAgriCrop": {
                "@type": "FarmCrop",
                "@id": "urn:farmcalendar:FarmCrop:0159de17-1c67-4ebd-92a5-51bc3b8d5c84"
            },
            "hasResult": {
                "@id": "urn:farmcalendar:QuantityValue:8ee0824e-471e-5f2f-bf4a-115c5b03c99b",
                "@type": "QuantityValue",
                "unit": "percent",
                "hasValue": "10"
            },
            "observedProperty": "cropStressLevel"
        }
    ]
}
```

## Example Request (POST/PUT/PATCH)

```json
{
    "@type": "CropStressIndicatorObservation",
    "activityType": {
        "@type": "FarmCalendarActivityType",
        "@id": "urn:farmcalendar:FarmCalendarActivityType:00000000-0000-0000-0000-000000000004"
    },
    "title": "Crop Stress Indicator",
    "details": "",
    "phenomenonTime": "2025-03-13T13:25:00Z",
    "madeBySensor": {
        "@type": "Sensor",
        "name": "XYZ Sensor"
    },
    "hasAgriCrop": {
        "@type": "FarmCrop",
        "@id": "urn:farmcalendar:FarmCrop:0159de17-1c67-4ebd-92a5-51bc3b8d5c84"
    },
    "hasResult": {
        "@type": "QuantityValue",
        "unit": "percent",
        "hasValue": "10"
    },
    "observedProperty": "cropStressLevel"
}
```

# Endpoint: /api/v1/CropStressIndicatorObservations/{id}/

## GET
Endpoint operation description: Api v1 cropstressindicatorobservations retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Crop Stress Indicator Observation..

## PUT
Endpoint operation description: Api v1 cropstressindicatorobservations update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Crop Stress Indicator Observation..

## PATCH
Endpoint operation description: Api v1 cropstressindicatorobservations partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Crop Stress Indicator Observation..

## DELETE
Endpoint operation description: Api v1 cropstressindicatorobservations destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Crop Stress Indicator Observation..

## Example Response (GET)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1cropstressindicatorobservations]

## Example Request (POST/PUT/PATCH)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1cropstressindicatorobservations]

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

## Example Response (GET)

```json
{
    "@context": [
        "https://w3id.org/ocsm/main-context.jsonld"
    ],
    "@graph": [
        {
            "status": 1,
            "deleted_at": null,
            "created_at": "2024-11-04T12:45:19.254000Z",
            "updated_at": "2024-11-04T12:45:19.254000Z",
            "name": "SIP X Farm",
            "description": "Potato fields for SIP X",
            "administrator": "Admin",
            "telephone": "0000",
            "vatID": "1111",
            "hasAgriParcel": [
                {
                    "@type": "Parcel",
                    "@id": "urn:farmcalendar:Parcel:00000000-0000-0000-0000-000000000001"
                },
                {
                    "@type": "Parcel",
                    "@id": "urn:farmcalendar:Parcel:00000000-0000-0000-0000-000000000002"
                },
                {
                    "@type": "Parcel",
                    "@id": "urn:farmcalendar:Parcel:00000000-0000-0000-0000-000000000003"
                }
            ],
            "contactPerson": {
                "firstname": "SIP",
                "lastname": "X",
                "@id": "urn:farmcalendar:ContactPerson:4aa2f898-6091-5be9-bd91-a0ada73a4a9c",
                "@type": "Person"
            },
            "address": {
                "@id": "urn:farmcalendar:Address:9be9bf30-f93e-54a2-9afb-2a48cab8060d",
                "@type": "Address",
                "adminUnitL1": "Belgium",
                "adminUnitL2": "Merelbeke",
                "addressArea": "District A",
                "municipality": "Municipality B",
                "community": "Community C",
                "locatorName": "SIPX Farms LTD"
            },
            "@id": "urn:farmcalendar:Farm:00000000-0000-0000-0000-000000000001",
            "@type": "Farm"
        }
    ]
}
```

## Example Request (POST/PUT/PATCH)

```json
{
    "status": 1,
    "deleted_at": null,
    "created_at": "2024-11-04T12:45:19.254000Z",
    "updated_at": "2024-11-04T12:45:19.254000Z",
    "name": "SIP X Farm",
    "description": "Potato fields for SIP X",
    "administrator": "Admin",
    "telephone": "0000",
    "vatID": "1111",
    "hasAgriParcel": [
        {
            "@type": "Parcel",
            "@id": "urn:farmcalendar:Parcel:00000000-0000-0000-0000-000000000001"
        },
        {
            "@type": "Parcel",
            "@id": "urn:farmcalendar:Parcel:00000000-0000-0000-0000-000000000002"
        },
        {
            "@type": "Parcel",
            "@id": "urn:farmcalendar:Parcel:00000000-0000-0000-0000-000000000003"
        }
    ],
    "contactPerson": {
        "firstname": "SIP",
        "lastname": "X",
        "@type": "Person"
    },
    "address": {
        "@type": "Address",
        "adminUnitL1": "Belgium",
        "adminUnitL2": "Merelbeke",
        "addressArea": "District A",
        "municipality": "Municipality B",
        "community": "Community C",
        "locatorName": "SIPX Farms LTD"
    },
    "@type": "Farm"
}
```

# Endpoint: /api/v1/Farm/{id}/

## GET
Endpoint operation description: Api v1 farm retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Farm..

## PUT
Endpoint operation description: Api v1 farm update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Farm..

## PATCH
Endpoint operation description: Api v1 farm partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Farm..

## DELETE
Endpoint operation description: Api v1 farm destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Farm..

## Example Response (GET)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1farm]

## Example Request (POST/PUT/PATCH)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1farm]

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

## Example Response (GET)

```json
{
    "@context": [
        "https://w3id.org/ocsm/main-context.jsonld"
    ],
    "@graph": [
        {
            "@type": "Animal",
            "@id": "urn:farmcalendar:FarmAnimal:99daeecc-bbdb-4851-89ab-682105f9ac1c",
            "nationalID": "NL 123",
            "name": "Spotty",
            "description": "A cow.",
            "hasAgriParcel": {
                "@type": "Parcel",
                "@id": "urn:farmcalendar:Parcel:00000000-0000-0000-0000-000000000001"
            },
            "sex": 1,
            "isCastrated": true,
            "species": "Cow",
            "breed": "Brown spotted",
            "birthdate": "2025-03-13T13:32:00Z",
            "isMemberOfAnimalGroup": {
                "@id": "urn:farmcalendar:AnimalGroup:7c74acb2-ffa0-5c67-9cfa-d5b1953a5472",
                "@type": "AnimalGroup",
                "hasName": "Some group"
            },
            "status": 1,
            "invalidatedAtTime": null,
            "dateCreated": "2025-03-14T12:32:18.808790Z",
            "dateModified": "2025-03-14T12:32:18.808797Z"
        }
    ]
}
```

## Example Request (POST/PUT/PATCH)

```json
{
    "@type": "Animal",
    "nationalID": "NL 123",
    "name": "Spotty",
    "description": "A cow.",
    "hasAgriParcel": {
        "@type": "Parcel",
        "@id": "urn:farmcalendar:Parcel:00000000-0000-0000-0000-000000000001"
    },
    "sex": 1,
    "isCastrated": true,
    "species": "Cow",
    "breed": "Brown spotted",
    "birthdate": "2025-03-13T13:32:00Z",
    "isMemberOfAnimalGroup": {
        "@type": "AnimalGroup",
        "hasName": "Some group"
    },
    "status": 1,
    "invalidatedAtTime": null,
    "dateCreated": "2025-03-14T12:32:18.808790Z",
    "dateModified": "2025-03-14T12:32:18.808797Z"
}
```

# Endpoint: /api/v1/FarmAnimals/{id}/

## GET
Endpoint operation description: Api v1 farmanimals retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Farm Animal..

## PUT
Endpoint operation description: Api v1 farmanimals update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Farm Animal..

## PATCH
Endpoint operation description: Api v1 farmanimals partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Farm Animal..

## DELETE
Endpoint operation description: Api v1 farmanimals destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Farm Animal..

## Example Response (GET)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1farmanimals]

## Example Request (POST/PUT/PATCH)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1farmanimals]

# Endpoint: /api/v1/FarmCalendarActivities/
This endpoint returns all farm calendar activities, this includes operations, observations and etc. However, throught this endpoint only the basic information regarding the calendar representation is shown, so any specific fields for the activities in question won't be available through here.
And therefore the POST/PUT/PATCH methods are discouraged, and it is not recomended the use of the GET for end-points, unless specifically looking for basic representation of the different calendar activities (operation, observations, etc...).

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

## Example Response (GET)

```json
{
    "@context": [
        "https://w3id.org/ocsm/main-context.jsonld"
    ],
    "@graph": [
        {
            "@type": "Operation",
            "@id": "urn:farmcalendar:FarmCalendarActivity:aa62956c-9ac8-4ce5-a6e1-68e1ce223513",
            "activityType": {
                "@type": "FarmCalendarActivityType",
                "@id": "urn:farmcalendar:FarmCalendarActivityType:00000000-0000-0000-0000-000000000003"
            },
            "title": "Pesticides",
            "details": "",
            "hasStartDatetime": "2025-03-14T13:20:00Z",
            "hasEndDatetime": "2025-03-15T13:20:00Z",
            "responsibleAgent": "Farmer",
            "usesAgriculturalMachinery": []
        },
        {
            "@type": "Operation",
            "@id": "urn:farmcalendar:FarmCalendarActivity:0cc526f6-ae17-41ef-86a4-e5541932c482",
            "activityType": {
                "@type": "FarmCalendarActivityType",
                "@id": "urn:farmcalendar:FarmCalendarActivityType:00000000-0000-0000-0000-000000000005"
            },
            "title": "Crop Growth Stage Observation",
            "details": "",
            "hasStartDatetime": "2025-03-14T13:10:00Z",
            "hasEndDatetime": null,
            "responsibleAgent": null,
            "usesAgriculturalMachinery": []
        },
        ....
    ]
}
```

## Example Request (POST/PUT/PATCH)

```json
{
    "@type": "Operation",
    "activityType": {
        "@type": "FarmCalendarActivityType",
        "@id": "urn:farmcalendar:FarmCalendarActivityType:00000000-0000-0000-0000-000000000003"
    },
    "title": "Pesticides",
    "details": "Spraying at parcel.",
    "hasStartDatetime": "2025-03-14T13:20:00Z",
    "hasEndDatetime": "2025-03-15T13:20:00Z",
    "responsibleAgent": "Farmer",
    "usesAgriculturalMachinery": []
}
```

# Endpoint: /api/v1/FarmCalendarActivities/{id}/

## GET
Endpoint operation description: Api v1 farmcalendaractivities retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Farm Activity..

## PUT
Endpoint operation description: Api v1 farmcalendaractivities update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Farm Activity..

## PATCH
Endpoint operation description: Api v1 farmcalendaractivities partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Farm Activity..

## DELETE
Endpoint operation description: Api v1 farmcalendaractivities destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Farm Activity..

## Example Response (GET)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1farmcalendaractivities]

## Example Request (POST/PUT/PATCH)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1farmcalendaractivities]

# Endpoint: /api/v1/FarmCalendarActivityTypes/
Built-in Farm Activtiy Types will mostly be represented by low sequential UUID such as: `00000000-0000-0000-0000-000000000001`, `00000000-0000-0000-0000-000000000002`, etc. Meanwhile, user-created activity types use UUID4 such as: `55cf0568-a998-43e8-9b4d-c49e74e853e7`.

The color fields (background, border, and text_color) refers to the colors used in the WebUI calendar page for the activitities of this type.

## GET
Endpoint operation description: Api v1 farmcalendaractivitytypes list.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * name (string): name of the asset..

## POST
Endpoint operation description: Api v1 farmcalendaractivitytypes create.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..

## Example Response (GET)

```json
{
    "@context": [
        "https://w3id.org/ocsm/main-context.jsonld"
    ],
    "@graph": [
        {
            "@type": "FarmActivityType",
            "@id": "urn:farmcalendar:FarmActivityType:55cf0568-a998-43e8-9b4d-c49e74e853e7",
            "name": "THI Observation",
            "description": null,
            "background_color": "#5E910A",
            "border_color": "#FFE800",
            "text_color": "#000000"
        },
        {
            "@type": "FarmActivityType",
            "@id": "urn:farmcalendar:FarmActivityType:00000000-0000-0000-0000-000000000003",
            "name": "Pesticides",
            "description": "Pesticide application",
            "background_color": "#C5E1A5",
            "border_color": "#8E7F2F",
            "text_color": "#4E342E"
        },
        {
            "@type": "FarmActivityType",
            "@id": "urn:farmcalendar:FarmActivityType:3e0ceecf-7aea-45b9-8e50-525dd5fa3775",
            "name": "Compost pH Observation",
            "description": null,
            "background_color": "#007bff",
            "border_color": "#007bff",
            "text_color": "#000000"
        },
        {
            "@type": "FarmActivityType",
            "@id": "urn:farmcalendar:FarmActivityType:00000000-0000-0000-0000-000000000006",
            "name": "Compost Operation",
            "description": "Compost Operation",
            "background_color": "#A3C585",
            "border_color": "#6B4226",
            "text_color": "#3E4A34"
        }
        ....
    ]
}
```

## Example Request (POST/PUT/PATCH)

```json
{
    "@type": "FarmActivityType",
    "name": "Irrigation",
    "description": "Irrigation operation",
    "background_color": "#B3E5FC",
    "border_color": "#0288D1",
    "text_color": "#01579B"
}
```

# Endpoint: /api/v1/FarmCalendarActivityTypes/{id}/

## GET
Endpoint operation description: Api v1 farmcalendaractivitytypes retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this farm calendar activity type..

## PUT
Endpoint operation description: Api v1 farmcalendaractivitytypes update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this farm calendar activity type..

## PATCH
Endpoint operation description: Api v1 farmcalendaractivitytypes partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this farm calendar activity type..

## DELETE
Endpoint operation description: Api v1 farmcalendaractivitytypes destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this farm calendar activity type..

## Example Response (GET)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1farmcalendaractivitytypes]

## Example Request (POST/PUT/PATCH)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1farmcalendaractivitytypes]

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

## Example Response (GET)
## Example Response (GET)

```json
{
    "@context": [
        "https://w3id.org/ocsm/main-context.jsonld"
    ],
    "@graph": [
        {
            "@type": "Crop",
            "@id": "urn:farmcalendar:FarmCrop:0159de17-1c67-4ebd-92a5-51bc3b8d5c84",
            "status": 1,
            "invalidatedAtTime": null,
            "dateCreated": "2025-03-14T12:06:20.902444Z",
            "dateModified": "2025-03-14T12:06:20.902453Z",
            "name": "Some Crop",
            "description": "Important crop for the fields",
            "hasAgriParcel": {
                "@type": "Parcel",
                "@id": "urn:farmcalendar:Parcel:00000000-0000-0000-0000-000000000001"
            },
            "cropSpecies": {
                "@id": "urn:farmcalendar:CropType:8c6dcfa7-2792-53bd-ae27-86d4bf3b832c",
                "@type": "CropType",
                "name": "A Species",
                "variety": "A Species"
            },
            "growth_stage": "seedling"
        }
    ]
}
```

## Example Request (POST/PUT/PATCH)

```json
{
    "@type": "Crop",
    "status": 1,
    "invalidatedAtTime": null,
    "dateCreated": "2025-03-14T12:06:20.902444Z",
    "dateModified": "2025-03-14T12:06:20.902453Z",
    "name": "Some Crop",
    "description": "Important crop for the fields",
    "hasAgriParcel": {
        "@type": "Parcel",
        "@id": "urn:farmcalendar:Parcel:00000000-0000-0000-0000-000000000001"
    },
    "cropSpecies": {
        "@type": "CropType",
        "name": "A Species",
        "variety": "A Species"
    },
    "growth_stage": "seedling"
}
```

# Endpoint: /api/v1/FarmCrops/{id}/

## GET
Endpoint operation description: Api v1 farmcrops retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Farm Crop..

## PUT
Endpoint operation description: Api v1 farmcrops update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Farm Crop..

## PATCH
Endpoint operation description: Api v1 farmcrops partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Farm Crop..

## DELETE
Endpoint operation description: Api v1 farmcrops destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Farm Crop..

## Example Response (GET)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1farmcrops]


## Example Request (POST/PUT/PATCH)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1farmcrops]

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

## Example Response (GET)

```json
{
    "@context": [
        "https://w3id.org/ocsm/main-context.jsonld"
    ],
    "@graph": [
        {
            "@type": "Parcel",
            "@id": "urn:farmcalendar:FarmParcel:00000000-0000-0000-0000-000000000001",
            "status": 1,
            "deleted_at": null,
            "created_at": "2024-11-04T12:51:14.074000Z",
            "updated_at": "2025-03-14T12:54:27.094123Z",
            "identifier": "T1 A (1)",
            "description": "Farm parcel T1 A (1) in Merelbeke",
            "validFrom": null,
            "validTo": null,
            "area": "0.94",
            "hasIrrigationFlow": "100.00",
            "category": "Potato Field",
            "inRegion": "Merelbeke, Belgium",
            "hasToponym": "Aardappelveld",
            "isNitroArea": false,
            "isNatura2000Area": false,
            "isPdopgArea": false,
            "isIrrigated": false,
            "isCultivatedInLevels": false,
            "isGroundSlope": false,
            "depiction": "",
            "hasGeometry": {
                "@id": "urn:farmcalendar:Geometry:81d1db67-aed2-506d-b9f6-d1608429adbf",
                "@type": "Geometry",
                "asWKT": "GEOMETRYCOLLECTION(MULTIPOLYGON (((3.763138334299517 50.975673175018, 3.763821317532035 50.97576496966823, 3.764007697455795 50.975827472797, 3.764006632347743 50.97582871324892, 3.764061000468175 50.9758461006125, 3.764983170535003 50.97477770613214, 3.764931997399592 50.97475797797846, 3.764928926944344 50.97476152071972, 3.764940502424819 50.97476599758799, 3.764940211693563 50.97476635077933, 3.764209885998442 50.97448417231766, 3.764207009669899 50.97448666161281, 3.764170843495563 50.97447300579999, 3.763825380011593 50.97487130998596, 3.763678129950689 50.97504326413318, 3.763683152468031 50.97504500731477, 3.763388822137993 50.97538408195327, 3.763386827486241 50.97538341110485, 3.763138843391756 50.97567296222812, 3.763138549682591 50.97567293098999, 3.763138334299517 50.975673175018))))"
            },
            "location": {
                "@id": "81d1db67-aed2-506d-b9f6-d1608429adbf",
                "@type": "Point",
                "lat": 50.975673175018,
                "long": 3.76313833429952
            },
            "hasAgriCrop": [
                {
                    "@type": "Crop",
                    "@id": "urn:farmcalendar:Crop:0159de17-1c67-4ebd-92a5-51bc3b8d5c84"
                }
            ],
            "farm": {
                "@type": "Farm",
                "@id": "urn:farmcalendar:Farm:00000000-0000-0000-0000-000000000001"
            }
        }
    ...
]
```

## Example Request (POST/PUT/PATCH)

```json
{
    "@type": "Parcel",
    "status": 1,
    "deleted_at": null,
    "created_at": "2024-11-04T12:51:14.074000Z",
    "updated_at": "2025-03-14T12:54:27.094123Z",
    "identifier": "T1 A (1)",
    "description": "Farm parcel T1 A (1) in Merelbeke",
    "validFrom": null,
    "validTo": null,
    "area": "0.94",
    "hasIrrigationFlow": "100.00",
    "category": "Potato Field",
    "inRegion": "Merelbeke, Belgium",
    "hasToponym": "Aardappelveld",
    "isNitroArea": false,
    "isNatura2000Area": false,
    "isPdopgArea": false,
    "isIrrigated": false,
    "isCultivatedInLevels": false,
    "isGroundSlope": false,
    "depiction": "",
    "hasGeometry": {
        "@type": "Geometry",
        "asWKT": "GEOMETRYCOLLECTION(MULTIPOLYGON (((3.763138334299517 50.975673175018, 3.763821317532035 50.97576496966823, 3.764007697455795 50.975827472797, 3.764006632347743 50.97582871324892, 3.764061000468175 50.9758461006125, 3.764983170535003 50.97477770613214, 3.764931997399592 50.97475797797846, 3.764928926944344 50.97476152071972, 3.764940502424819 50.97476599758799, 3.764940211693563 50.97476635077933, 3.764209885998442 50.97448417231766, 3.764207009669899 50.97448666161281, 3.764170843495563 50.97447300579999, 3.763825380011593 50.97487130998596, 3.763678129950689 50.97504326413318, 3.763683152468031 50.97504500731477, 3.763388822137993 50.97538408195327, 3.763386827486241 50.97538341110485, 3.763138843391756 50.97567296222812, 3.763138549682591 50.97567293098999, 3.763138334299517 50.975673175018))))"
    },
    "location": {
        "@type": "Point",
        "lat": 50.975673175018,
        "long": 3.76313833429952
    },
    "hasAgriCrop": [
        {
            "@type": "Crop",
            "@id": "urn:farmcalendar:Crop:0159de17-1c67-4ebd-92a5-51bc3b8d5c84"
        }
    ],
    "farm": {
        "@type": "Farm",
        "@id": "urn:farmcalendar:Farm:00000000-0000-0000-0000-000000000001"
    }
}
```

# Endpoint: /api/v1/FarmParcels/{id}/

## GET
Endpoint operation description: Api v1 farmparcels retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Farm Parcel..

## PUT
Endpoint operation description: Api v1 farmparcels update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Farm Parcel..

## PATCH
Endpoint operation description: Api v1 farmparcels partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Farm Parcel..

## DELETE
Endpoint operation description: Api v1 farmparcels destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Farm Parcel..

## Example Response (GET)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1farmparcels]


## Example Request (POST/PUT/PATCH)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1farmparcels]

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

## Example Response (GET)

```json
{
    "@context": [
        "https://w3id.org/ocsm/main-context.jsonld"
    ],
    "@graph": [
        {
            "@type": "FertilizationOperation",
            "@id": "urn:farmcalendar:FertilizationOperation:3aa2e704-cd36-4198-9721-e98848ce7337",
            "activityType": {
                "@type": "FarmCalendarActivityType",
                "@id": "urn:farmcalendar:FarmCalendarActivityType:00000000-0000-0000-0000-000000000001"
            },
            "title": "Fertilization",
            "details": "",
            "hasStartDatetime": "2025-03-14T18:04:00Z",
            "hasEndDatetime": "2025-03-14T19:04:00Z",
            "responsibleAgent": "Farmer",
            "usesAgriculturalMachinery": [
                {
                    "@type": "AgriculturalMachine",
                    "@id": "urn:farmcalendar:AgriculturalMachine:b03d5bf5-5d34-44c2-91c6-28835b941f7a"
                }
            ],
            "hasAppliedAmount": {
                "@id": "urn:farmcalendar:QuantityValue:88299eed-a51a-5516-9e90-3beebb759f5c",
                "@type": "QuantityValue",
                "unit": "Kg",
                "numericValue": 23.0
            },
            "hasApplicationMethod": "Dispersion",
            "usesFertilizer": {
                "@type": "Fertilizer",
                "@id": "urn:farmcalendar:Fertilizer:2da60656-6b58-4470-a0b3-710a7e75f3b2"
            },
            "operatedOn": {
                "@type": "Parcel",
                "@id": "urn:farmcalendar:Parcel:00000000-0000-0000-0000-000000000002"
            }
        }
    ]
}
```

## Example Request (POST/PUT/PATCH)

```json
{
    "@type": "FertilizationOperation",
    "activityType": {
        "@type": "FarmCalendarActivityType",
        "@id": "urn:farmcalendar:FarmCalendarActivityType:00000000-0000-0000-0000-000000000001"
    },
    "title": "Fertilization",
    "details": "",
    "hasStartDatetime": "2025-03-14T18:04:00Z",
    "hasEndDatetime": "2025-03-14T19:04:00Z",
    "responsibleAgent": "Farmer",
    "usesAgriculturalMachinery": [
        {
            "@type": "AgriculturalMachine",
            "@id": "urn:farmcalendar:AgriculturalMachine:b03d5bf5-5d34-44c2-91c6-28835b941f7a"
        }
    ],
    "hasAppliedAmount": {
        "@type": "QuantityValue",
        "unit": "Kg",
        "numericValue": 23.0
    },
    "hasApplicationMethod": "Dispersion",
    "usesFertilizer": {
        "@type": "Fertilizer",
        "@id": "urn:farmcalendar:Fertilizer:2da60656-6b58-4470-a0b3-710a7e75f3b2"
    },
    "operatedOn": {
        "@type": "Parcel",
        "@id": "urn:farmcalendar:Parcel:00000000-0000-0000-0000-000000000002"
    }
}
```

# Endpoint: /api/v1/FertilizationOperations/{id}/

## GET
Endpoint operation description: Api v1 fertilizationoperations retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Fertilization Operation..

## PUT
Endpoint operation description: Api v1 fertilizationoperations update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Fertilization Operation..

## PATCH
Endpoint operation description: Api v1 fertilizationoperations partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Fertilization Operation..

## DELETE
Endpoint operation description: Api v1 fertilizationoperations destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Fertilization Operation..

## Example Response (GET)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1fertilizationoperations]


## Example Request (POST/PUT/PATCH)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1fertilizationoperations]

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

## Example Response (GET)

```json
{
    "@context": [
        "https://w3id.org/ocsm/main-context.jsonld"
    ],
    "@graph": [
        {
            "@id": "urn:farmcalendar:Fertilizer:2da60656-6b58-4470-a0b3-710a7e75f3b2",
            "hasCommercialName": "ENTEC 20-8-10",
            "description": "Complex NPK fertilizer that combines the excellent properties of nitrophoska fertilizers (perfect granulation, no dust, low cadmium content, no N in ureic form and high solubility), with one of the most efficient fertilizer technologies to improve the absorption of nutrients, especially nitrogen.",
            "hasCost": "10.00",
            "isPricePer": "EUR",
            "hasActiveSubstance": "+2Mgo+3S",
            "isTargetedTowards": "Olive trees or citrus fruits",
            "hasNutrientConcentration": "20.00",
            "status": 1,
            "dateCreated": "2025-03-14T13:04:09.524024Z",
            "dateModified": "2025-03-14T13:04:09.524034Z",
            "invalidatedAtTime": null,
            "@type": "Fertilizer"
        }
    ]
}
```

## Example Request (POST/PUT/PATCH)

```json
{
    "hasCommercialName": "ENTEC 20-8-10",
    "description": "Complex NPK fertilizer that combines the excellent properties of nitrophoska fertilizers (perfect granulation, no dust, low cadmium content, no N in ureic form and high solubility), with one of the most efficient fertilizer technologies to improve the absorption of nutrients, especially nitrogen.",
    "hasCost": "10.00",
    "isPricePer": "EUR",
    "hasActiveSubstance": "+2Mgo+3S",
    "isTargetedTowards": "Olive trees or citrus fruits",
    "hasNutrientConcentration": "20.00",
    "status": 1,
    "dateCreated": "2025-03-14T13:04:09.524024Z",
    "dateModified": "2025-03-14T13:04:09.524034Z",
    "invalidatedAtTime": null,
    "@type": "Fertilizer"
}
```

# Endpoint: /api/v1/Fertilizers/{id}/

## GET
Endpoint operation description: Api v1 fertilizers retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Fertilizer..

## PUT
Endpoint operation description: Api v1 fertilizers update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Fertilizer..

## PATCH
Endpoint operation description: Api v1 fertilizers partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Fertilizer..

## DELETE
Endpoint operation description: Api v1 fertilizers destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Fertilizer..

## Example Response (GET)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1fertilizers]

## Example Request (POST/PUT/PATCH)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1fertilizers]

# Endpoint: /api/v1/IrrigationOperations/
The field for `operatedOn` can be left blank, in case the irrigation operation is not applied to a specific FarmParcel (i.e., irrigation operation from a composting operation).

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

## Example Response (GET)

```json
{
    "@context": [
        "https://w3id.org/ocsm/main-context.jsonld"
    ],
    "@graph": [
        {
            "@type": "IrrigationOperation",
            "@id": "urn:farmcalendar:IrrigationOperation:711f24f8-c058-4bcc-9462-5ba33b5253d2",
            "activityType": {
                "@type": "FarmCalendarActivityType",
                "@id": "urn:farmcalendar:FarmCalendarActivityType:00000000-0000-0000-0000-000000000002"
            },
            "title": "Irrigation",
            "details": "",
            "hasStartDatetime": "2025-03-14T13:17:11Z",
            "hasEndDatetime": null,
            "responsibleAgent": "Farmer",
            "usesAgriculturalMachinery": [],
            "hasAppliedAmount": {
                "@id": "urn:farmcalendar:QuantityValue:e4e66fc3-e2cd-53e7-80ea-ef8960e060f6",
                "@type": "QuantityValue",
                "unit": "litres",
                "numericValue": 10.0
            },
            "usesIrrigationSystem": "sprinkler",
            "operatedOn": {
                "@type": "Parcel",
                "@id": "urn:farmcalendar:Parcel:00000000-0000-0000-0000-000000000002"
            }
        },
        ...
    ]
}
```

## Example Request (POST/PUT/PATCH)

```json
{
    "@type": "IrrigationOperation",
    "activityType": {
        "@type": "FarmCalendarActivityType",
        "@id": "urn:farmcalendar:FarmCalendarActivityType:00000000-0000-0000-0000-000000000002"
    },
    "title": "Irrigation",
    "details": "",
    "hasStartDatetime": "2025-03-14T13:17:11Z",
    "hasEndDatetime": null,
    "responsibleAgent": "Farmer",
    "usesAgriculturalMachinery": [],
    "hasAppliedAmount": {
        "@type": "QuantityValue",
        "unit": "litres",
        "numericValue": 10.0
    },
    "usesIrrigationSystem": "sprinkler",
    "operatedOn": {
        "@type": "Parcel",
        "@id": "urn:farmcalendar:Parcel:00000000-0000-0000-0000-000000000002"
    }
}
```

# Endpoint: /api/v1/IrrigationOperations/{id}/

## GET
Endpoint operation description: Api v1 irrigationoperations retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Irrigation Operation..

## PUT
Endpoint operation description: Api v1 irrigationoperations update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Irrigation Operation..

## PATCH
Endpoint operation description: Api v1 irrigationoperations partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Irrigation Operation..

## DELETE
Endpoint operation description: Api v1 irrigationoperations destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Irrigation Operation..

## Example Response (GET)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1irrigationoperations]

## Example Request (POST/PUT/PATCH)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1irrigationoperations]

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

## Example Response (GET)

```json
{
    "@context": [
        "https://w3id.org/ocsm/main-context.jsonld"
    ],
    "@graph": [
        {
            "@type": "Observation",
            "@id": "urn:farmcalendar:Observation:7e67dc08-5e00-4927-8788-38de06c2c8e3",
            "activityType": {
                "@type": "FarmCalendarActivityType",
                "@id": "urn:farmcalendar:FarmCalendarActivityType:00000000-0000-0000-0000-000000000004"
            },
            "title": "Crop Stress Indicator",
            "details": "",
            "phenomenonTime": "2025-03-13T13:25:00Z",
            "madeBySensor": {
                "@id": "urn:farmcalendar:Sensor:15786cae-f3a0-5712-a183-ce3a2fd24475",
                "@type": "Sensor",
                "name": "XYZ Sensor"
            },
            "hasResult": {
                "@id": "urn:farmcalendar:QuantityValue:8ee0824e-471e-5f2f-bf4a-115c5b03c99b",
                "@type": "QuantityValue",
                "unit": "percent",
                "hasValue": "10"
            },
            "observedProperty": "cropStressLevel"
        },
        {
            "@type": "Observation",
            "@id": "urn:farmcalendar:Observation:0614051b-ee38-4718-a1a1-c4e5b72d68f2",
            "activityType": {
                "@type": "FarmCalendarActivityType",
                "@id": "urn:farmcalendar:FarmCalendarActivityType:55cf0568-a998-43e8-9b4d-c49e74e853e7"
            },
            "title": "THI Observation",
            "details": "",
            "phenomenonTime": "2025-02-27T15:15:02Z",
            "madeBySensor": {
                "@id": "urn:farmcalendar:Sensor:e2152083-8bad-5a5b-976e-8af3a45ecb92",
                "@type": "Sensor",
                "name": "some sensor"
            },
            "hasResult": {
                "@id": "urn:farmcalendar:QuantityValue:37b4cbab-1fa1-56c7-b72e-44464d52c21e",
                "@type": "QuantityValue",
                "unit": null,
                "hasValue": "37.16"
            },
            "observedProperty": "temperature_humidity_index"
        },
    ...
    ]
}
```

## Example Request (POST/PUT/PATCH)

```json
{
    "@type": "Observation",
    "activityType": {
        "@type": "FarmCalendarActivityType",
        "@id": "urn:farmcalendar:FarmCalendarActivityType:55cf0568-a998-43e8-9b4d-c49e74e853e7"
    },
    "title": "THI Observation",
    "details": "",
    "phenomenonTime": "2025-02-27T15:15:02Z",
    "madeBySensor": {
        "@type": "Sensor",
        "name": "some sensor"
    },
    "hasResult": {
        "@type": "QuantityValue",
        "unit": null,
        "hasValue": "37.16"
    },
    "observedProperty": "temperature_humidity_index"
}
```

# Endpoint: /api/v1/Observations/{id}/

## GET
Endpoint operation description: Api v1 observations retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Observation..

## PUT
Endpoint operation description: Api v1 observations update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Observation..

## PATCH
Endpoint operation description: Api v1 observations partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Observation..

## DELETE
Endpoint operation description: Api v1 observations destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Observation..

## Example Response (GET)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1observations]


## Example Request (POST/PUT/PATCH)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1observations]

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

## Example Response (GET)

```json
{
    "@context": [
        "https://w3id.org/ocsm/main-context.jsonld"
    ],
    "@graph": [
        {
            "@id": "urn:farmcalendar:Pesticide:00975c81-f923-45b1-b421-d4e9f2812545",
            "hasCommercialName": "BORDELESA 20 WP",
            "description": "Short description.",
            "hasCost": "20.00",
            "isPricePer": "EUR",
            "hasActiveSubstance": "Bordeaux mixture",
            "isTargetedTowards": "Powdery mildew",
            "hasPreharvestInterval": 1,
            "status": 1,
            "dateCreated": "2025-03-14T12:19:51.268292Z",
            "dateModified": "2025-03-14T12:19:51.268311Z",
            "invalidatedAtTime": null,
            "@type": "Pesticide"
        }
    ]
}
```

## Example Request (POST/PUT/PATCH)

```json
{
    "hasCommercialName": "BORDELESA 20 WP",
    "description": "Short description.",
    "hasCost": "20.00",
    "isPricePer": "EUR",
    "hasActiveSubstance": "Bordeaux mixture",
    "isTargetedTowards": "Powdery mildew",
    "hasPreharvestInterval": 1,
    "status": 1,
    "dateCreated": "2025-03-14T12:19:51.268292Z",
    "dateModified": "2025-03-14T12:19:51.268311Z",
    "invalidatedAtTime": null,
    "@type": "Pesticide"
}
```

# Endpoint: /api/v1/Pesticides/{id}/

## GET
Endpoint operation description: Api v1 pesticides retrieve.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Pesticide..

## PUT
Endpoint operation description: Api v1 pesticides update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Pesticide..

## PATCH
Endpoint operation description: Api v1 pesticides partial update.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Pesticide..

## DELETE
Endpoint operation description: Api v1 pesticides destroy.

### Parameters

 * format (string): Forces a response format (i.e., Json or JsonLD)..
 * **id** (string) [Required]: A UUID string identifying this Pesticide..

## Example Response (GET)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1pesticides]

## Example Request (POST/PUT/PATCH)

Request/response similar to this general entity (List endpoint)[API.md/#endpoint-apiv1pesticides]
