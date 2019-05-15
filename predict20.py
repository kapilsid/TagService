from sklearn.naive_bayes import MultinomialNB

import pickle

folder_name  = 'twentytrain/'

filename = folder_name + 'twentytrain_clf.sav'
clf = pickle.load(open(filename, 'rb'))

filename = folder_name + 'twentytrain_countvec.sav'
count_vect = pickle.load(open(filename, 'rb'))

filename = folder_name + 'twentytrain_tfdif.sav'
tdif = pickle.load(open(filename, 'rb'))

filename = folder_name + 'twentytrain_target.sav'
targets = pickle.load(open(filename, 'rb'))

def predictClass(mtext):
    """Predicts the class or topic of the text using tdif
    term document inverse frequency
    Args:
      mtext: text 

    Returns:
      predicted class 

    """ 
    Z_counts = count_vect.transform([mtext])

    Z_tfidf = tdif.transform(Z_counts)

    predicted = clf.predict(Z_tfidf)
    return targets[predicted[0]]