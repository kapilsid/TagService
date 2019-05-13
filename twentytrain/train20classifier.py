from sklearn.datasets import fetch_20newsgroups

twenty_train = fetch_20newsgroups(subset='train', shuffle=True)

print(twenty_train.target_names) #prints all the categories
#print("\n".join(twenty_train.data[0].split("\n")[:3])) #prints first line of the first data file

#print(twenty_train.data[0])

from sklearn.feature_extraction.text import CountVectorizer

count_vect = CountVectorizer()

X_train_counts = count_vect.fit_transform(twenty_train.data)

print(len(twenty_train.data))

print(X_train_counts.shape)  #(samples,features)

from sklearn.feature_extraction.text import TfidfTransformer

tdif = TfidfTransformer(use_idf=True)

X_train_tfidf = tdif.fit_transform(X_train_counts)
print(X_train_tfidf.shape)


from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)

import pickle
filename = 'twentytrain_clf.sav'
pickle.dump(clf, open(filename, 'wb'))

filename = 'twentytrain_countvec.sav'
pickle.dump(count_vect, open(filename, 'wb'))

filename = 'twentytrain_tfdif.sav'
pickle.dump(tdif, open(filename, 'wb'))

filename = 'twentytrain_target.sav'
pickle.dump(twenty_train.target_names, open(filename, 'wb'))

# Z_counts = count_vect.transform([mtext])

# Z_tfidf = tdif.transform(Z_counts)

# predicted = clf.predict(Z_tfidf)

#     print(predicted)
# print(twenty_train.target_names[predicted[0]])