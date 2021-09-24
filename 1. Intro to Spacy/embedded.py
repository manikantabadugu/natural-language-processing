def preprocess(path):
    with open(path, 'r') as f:
        lines= f.readlines()
        for i in range(len(lines)):
            lines[i]=lines[i].replace('.','').replace('\'','').replace('?','').replace(';','').replace(',','').replace(':','').replace('!','').replace('_','').replace('.','').replace('\"','').replace('-','').replace('[','').replace(']','')
        with open(r'C:\Users\User\Documents\GitHub\practice folders\natural-language-processing\1. Intro to Spacy\preprocessed.txt',"w") as p:
            p.writelines(lines)

preprocess(r'C:\Users\User\Documents\GitHub\practice folders\natural-language-processing\1. Intro to Spacy\blake_poems.txt')


def get_sentences(path):
    f = open(path, 'r')
    lines= f.readlines()
    sentences= [line.lower().split() for line in lines]
    f.close
    return sentences
def clean_sentences(sentences):
    i=0
    while i< len(sentences):
        if sentences[i]==[]:
          sentences.pop(i)
        else:
          i+=1
    return sentences
sentences = get_sentences(r'C:\Users\User\Documents\GitHub\practice folders\natural-language-processing\1. Intro to Spacy\blake_poems.txt')
clean_sents= clean_sentences(sentences)
print(len(sentences))
print(len(clean_sents))

def get_dicts(clean_sentences):
    vocab= []
    for sentence in sentences:
        for token in sentence:
            if token not in vocab:
                vocab.append(token)
    
    w2i = {w:i for (i,w) in enumerate(vocab)}
    i2w =  {i:w for (i,w) in enumerate(vocab)}

    return w2i, i2w, len(vocab)
w2i, i2w, len_vocab = get_dicts(clean_sentences)
print(w2i['william'])
print(i2w[2])
print(len_vocab)




