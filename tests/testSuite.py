import unittest
from tests import trainTests
from tests import classifierTets
from tests import integrationTests

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()

    # Test the train module
    train_suite = unittest.TestSuite()
    train_suite.addTests(loader.loadTestsFromModule(trainTests))
    runner.run(train_suite)

    # Test the train module
    classifier_suit = unittest.TestSuite()
    classifier_suit.addTests(loader.loadTestsFromModule(classifierTets))
    runner.run(classifier_suit)

    # Integration test between the train and the classifier
    integration_suit = unittest.TestSuite()
    integration_suit.addTests(loader.loadTestsFromModule(integrationTests))
    runner.run(integration_suit)
