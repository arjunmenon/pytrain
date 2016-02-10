#
# Dev test for pytrain library
#
# @ author becxer
# @ email becxer87@gmail.com#
# --------------------------------------------

from test_lib import *
from test_KNN import *
from test_DecisionTree import *
from test_Bayes import *
from test_Regression import *
from test_Apriori import *

# test fs lib
test_fs(logging = False).process()

# test normalize lib
test_normalize(logging = False).process()

# test batch lib
test_batch(logging = False).process()

# test nlp lib
test_nlp(logging = False).process()

# test KNN
test_KNN(logging = False).process()
# test_KNN_digit(logging = False).process()

# test DecisionTree
test_DecisionTreeID3(logging = False).process()
test_DecisionTreeID3_store(logging = False).process()
test_DecisionTreeID3_lense(logging = False).process()

# Test NaiveBayes
test_NaiveBayes(logging = False).process()
test_NaiveBayes_email(logging = False).process()

# Test GaussianNaiveBayes
test_GaussianNaiveBayes(logging = False).process()
test_GaussianNaiveBayes_rssi(logging = False).process()

# Test Apriori
test_Apriori(logging = False).process()
# test_Apriori_mushroom(logging = False).process()

# Test LinearRegression
test_LinearRegression(logging = False).process()
test_LinearRegression_horse(logging = False).process()
