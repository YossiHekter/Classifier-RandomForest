import controller
import unittest
from unittest.mock import Mock
from gui_support import destroy_window


class TestClassifier(unittest.TestCase):

    def test_empty_path(self):
        controller.askopenfilename = Mock(return_value='')
        controller.popup_msg = Mock(return_value='')
        controller.classifier_function()
        self.assertTrue(controller.popup_msg.called)

    def test_wrong_path(self):
        controller.askopenfilename = Mock(return_value='C:/wrong_path')
        controller.popup_msg = Mock(return_value='')
        controller.classifier_function()
        self.assertTrue(controller.popup_msg.called)

    def test_call_pdf_file(self):
        controller.askopenfilename = Mock(return_value='C:/school/guide_dog/resource/pdf.pdf')
        controller.popup_msg = Mock(return_value='')
        controller.classifier_function()
        self.assertTrue(controller.popup_msg.called)

    def test_over_column(self):
        controller.askopenfilename = Mock(return_value='C:/school/guide_dog/resource/Over column.csv')
        controller.popup_format_error = Mock(return_value='')
        controller.popup_msg = Mock(return_value='')
        controller.classifier_function()
        self.assertTrue(controller.popup_format_error.called)

    def test_missing_column(self):
        controller.askopenfilename = Mock(return_value='C:/school/guide_dog/resource/missing column.csv')
        controller.popup_format_error = Mock(return_value='')
        controller.model_accuracy = Mock(return_value='')
        controller.popup_msg = Mock(return_value='')
        controller.classifier_function()
        self.assertTrue(controller.popup_format_error.called)

    def test_valid_csv(self):
        controller.askopenfilename = Mock(return_value='C:/school/guide_dog/resource/Data.csv')
        controller.model_accuracy = Mock(return_value='')
        controller.bar = Mock(return_value='')
        controller.train_model()
        controller.askopenfilename = Mock(return_value='C:/school/guide_dog/resource/New dogs.csv')
        controller.model_accuracy = Mock(return_value='')
        controller.popup_output = Mock(return_value='')
        controller.classifier_function()
        self.assertTrue(controller.popup_output.called)

    def test_one_row_valid_csv(self):
        controller.askopenfilename = Mock(return_value='C:/school/guide_dog/resource/Data.csv')
        controller.model_accuracy = Mock(return_value='')
        controller.bar = Mock(return_value='')
        controller.train_model()
        controller.askopenfilename = Mock(return_value='C:/school/guide_dog/resource/One row classifier.csv')
        controller.model_accuracy = Mock(return_value='')
        controller.popup_output = Mock(return_value='')
        controller.classifier_function()
        self.assertTrue(controller.popup_output.called)

    def test_1000_record_valid_csv(self):
        controller.askopenfilename = Mock(return_value='C:/school/guide_dog/resource/Data.csv')
        controller.model_accuracy = Mock(return_value='')
        controller.bar = Mock(return_value='')
        controller.train_model()
        controller.askopenfilename = Mock(return_value='C:/school/guide_dog/resource/1000 rows classifier.csv')
        controller.model_accuracy = Mock(return_value='')
        controller.popup_output = Mock(return_value='')
        controller.classifier_function()
        self.assertTrue(controller.popup_output.called)

    def tearDown(self):
        destroy_window()



