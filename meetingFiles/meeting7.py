from nltk.corpus import wordnet as wn


d = wn.synset('dog.n.01')
print(d.hypernym_paths())
print("*" * 80)
r = wn.synset('cat.n.01')
print(r.hypernym_paths())

print(d.lowest_common_hypernyms(r))

quit()
print(f"Hypernyms: \n {d.hypernyms()}")
while True:
    if d == wn.synset('entity.n.01'):
        print(d)
        break
    else:
        d = d.hypernyms()[0]
        print(d)

quit() ######################################################

d1 = wn.synset('frump.n.01')
frumps = wn.synets('frump')
for lemmas in frumps:
    print(lemmas.lemmas())

#'dog' is lemma of 'frump.n.01'

quit() ##############################################
#Synset def and examples
d = wn.synsets('bat')
for value in d:
    print(value, value.definition())
    for ex in value.examples():
        print("\t" + ex)
    print()
   