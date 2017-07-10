from unittest import TestCase

from protocols.tests import get_valid_empty_interpreted_genome_rd_3_0_0
from protocols.tests import get_valid_reported_somatic_structural_variant_3_0_0


class TestValidate(TestCase):

    def test_validate_debug(self):
        variant = get_valid_reported_somatic_structural_variant_3_0_0()
        variant.reportedStructuralVariantCancer.end = None

        # Check variant is not a valid ReportedSomaticStructuralVariants object
        self.assertFalse(variant.validate(jsonDict=variant.toJsonDict()))

        # Check the result of validation_result is False
        validation_result = variant.validate(jsonDict=variant.toJsonDict(), verbose=True)
        self.assertFalse(validation_result.result)

        # Check the validation returns the expected messages
        expected_message_2 = 'Class: [ReportedStructuralVariantCancer] expects field: [end] with schema type: ["int"] but received value: [None]'
        self.assertEqual(validation_result.messages[2], expected_message_2)
        expected_message_1 = '-2147483648 <= None <= 2147483647'
        self.assertEqual(validation_result.messages[1], expected_message_1)
        expected_message_0 = 'Schema: ["int"] has type: [int] but received datum: [None]'
        self.assertEqual(validation_result.messages[0], expected_message_0)

    def test_validate_debug_more_complex(self):
        ig_rd = get_valid_empty_interpreted_genome_rd_3_0_0()
        invalid_test_data = ig_rd.toJsonDict()
        invalid_test_data['analysisId'] = 42
        invalid_test_data['reportedStructuralVariants'][0]['additionalNumericVariantAnnotations'] = 'NoneAtAll'

        # Check invalid_test_data is not a valid InterpretedGenome object
        self.assertFalse(ig_rd.validate(jsonDict=invalid_test_data))

        # Check the result of validation_result is False
        validation_result = ig_rd.validate(jsonDict=invalid_test_data, verbose=True)
        self.assertFalse(validation_result.result)


