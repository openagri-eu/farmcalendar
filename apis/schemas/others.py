from calamus import fields
from calamus.schema import JsonLDSchema



qudt_schema = fields.Namespace("http://qudt.org/schema/qudt/")

class QuantityValueModel:
    def __init__(self, numeric_value, unit):
        self.numeric_value = numeric_value
        self.unit = unit


class QuantityValueSchema(JsonLDSchema):
    id = fields.Id()
    unit = fields.IRI(qudt_schema.unit)
    numeric_value = fields.Float(qudt_schema.numericValue)

    class Meta:
        rdf_type = qudt_schema.QuantityValue
        model = QuantityValueModel


