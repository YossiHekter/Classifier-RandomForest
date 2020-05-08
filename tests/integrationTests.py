import controller
import unittest
from unittest.mock import Mock
from gui_support import destroy_window
from model import Model


class TestTrain(unittest.TestCase):

    def tearDown(self):
        Model.del_model()
        destroy_window()

    def test_classifier_without_module(self):
        controller.askopenfilename = Mock(return_value='C:/school/guide_dog/resource/Data.csv')
        controller.popup_format_error = Mock(return_value='')
        controller.popup_msg = Mock(return_value='')
        controller.classifier_function()
        self.assertTrue(controller.popup_msg.called)

    def test_classifier_with_module(self):
        controller.askopenfilename = Mock(return_value='C:/school/guide_dog/resource/Data.csv')
        controller.model_accuracy = Mock(return_value='')
        controller.popup_output = Mock(return_value='')

        # popup that called after the classifier finished successfully
        controller.popup_output = Mock(return_value='')

        # First train the module
        controller.train_model()

        # Then run the classifier
        controller.askopenfilename = Mock(return_value='C:/school/guide_dog/resource/New dogs.csv')
        controller.classifier_function()
        self.assertTrue(controller.popup_output.called)




