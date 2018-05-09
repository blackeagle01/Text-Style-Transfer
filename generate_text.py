
'''


>>> python3 generate_text.py

to generate text in the style of training data.


'''






from keras.models import load_model
import time
import numpy as np

file=open('kafka.txt')
string=file.read()
words=string.split()

sentences=[words[i:i+5] for i in range(25000)]
targets=[words[i+5] for i in range(25000)]


vocab=list(set(words))

words_to_code=dict((i,j) for j,i in enumerate(vocab))
code_to_words=dict((i,j) for i,j in enumerate(vocab))

def generate_test():
    sentence='His room, a proper human'
    sentence=sentence.split()
    sentence=[words_to_code[w] for w in sentence]
    sentence=np.array(sentence)
    sentence=sentence.reshape(1,5)
    
    model=load_model('newtextmodel.h5')
    
    while True:
        x=np.argmax(model.predict(sentence))
        print(code_to_words[x],end=' ')
        sentence=sentence.flatten()
        sentence=sentence.tolist()
        sentence.append(x)
        sentence=sentence[1:]
        sentence=np.array(sentence)
        sentence=sentence.reshape(1,5)
        time.sleep(1)

if __name__ == '__main__':
    generate_test()
