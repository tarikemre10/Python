#Tarık Emre Gündüz 280201075
import csv
def read_genes(file_path):
    #open the file
    gene_open = open(file_path, "r")
    genes = gene_open.readlines()
    #define some variables and append the txt file in them
    keys=[]
    values=[]
    gene_dict={}
    #lines which has odd numbers are keys and others are values
    c=1
    for line in genes:
        if c%2==1:
            keys.append(line[:-1])
        else:
            values.append(line[:-1])
        c+=1

    #appended values and keys in a dict
    for i in range(115):
        gene_dict[keys[i]]=values[i]

    b=0
    #count the keys and this is the number of chrs
    for a in gene_dict.keys():
        b+=1
    print(b)
    return gene_dict


def get_fragments(gene_dict, frag_len):
    values = gene_dict.values()
    keys = gene_dict.keys()
    frag_dict={}
    frag_keys=[]
    frag_values=[]
    for value in values:   
        frag=""
        
        for letter in value:
            frag+=letter
            if len(frag)==frag_len:
                frag_values.append(frag)
                frag=""
    
    x=0
    #we should arrange the ids and for this I splitted in a propper way
    for key in keys:
        id2 = key.split("-")[1]
        id1 = key.split("-")[0].split("|")[1]
        
        chr_len=int(id2)-int(id1)
        
        frag_count = chr_len//50
        id11=int(id1)
        
        for i in range(frag_count):
            #I have arranged the ids in this loop
            
            frag_keys.append(key.split("-")[0].split("|")[0]+"|"+str(id11)+"-"+str(id11+50))
            id11+=50
            x+=1
    
    e=0
    for key in frag_keys:
        frag_dict[key]=frag_values[e]
        e+=1
      
    print(e)    
    return frag_dict


def filter_frags(frag_dict, threshold):
    #it is the function which has checked the values
    def get_similarity(s1,s2):
        
        d=0
        
        for c in range (50):
            if frag_values[s1][c]==frag_values[s2][c]:
                d+=1
        return d
    
    frag_values = []
    for i in frag_dict.values():
        frag_values.append(i)
    frag_keys = []
    for i in frag_dict.keys():
        frag_keys.append(i)
    e=0
    #this code looks all the values
    for a in range (len(frag_values)):
    #for do not check the same values I have define a+1 as initial value
        for b in range (a+1,len(frag_values)):
            
            d = get_similarity(a,b)
            if d/50>threshold:
                    
                e+=1
                del frag_values[a]
                del frag_keys[a]
                break
                
    dissimilar_frag_dict={}
    sayi=0
    for t in frag_keys:
        dissimilar_frag_dict[t]=frag_values[sayi]
        sayi+=1
    print(1293-e)
    return dissimilar_frag_dict



def get_sentences(dissimilar_frag_dict):
    dissimilar_frag_values = []
    for i in dissimilar_frag_dict.values():
        dissimilar_frag_values.append(i)
    dissimilar_frag_keys = []
    for i in dissimilar_frag_dict.keys():
        dissimilar_frag_keys.append(i)
    def generate_kmers(seq, k):
        print("a")

    sentences_dict_values=[]
    a=0
    b=4
    for item in dissimilar_frag_values:
        #We should take 4 values for finding words and it must be in a loop
        a=0
        b=4
        sentence=""  
        for i in range (len(item)-3):
            #when word has length of 4 it appended in sentence and in the and I appended all sentences in a list
            word=""
            word+=item[a:b]+" "
            a+=1
            b+=1
            sentence+=word
        sentences_dict_values.append(sentence)
        
    sentences_dict={}
    sayi=0
    for t in dissimilar_frag_keys:
        sentences_dict[t]=sentences_dict_values[sayi]
        sayi+=1 

    print(a)      
    return sentences_dict
        

def clean_dict(sentences_dict):
    
    sentences_values = []
    for i in sentences_dict.values():
        sentences_values.append(i)
    sentences_keys = []
    for i in sentences_dict.keys():
        sentences_keys.append(i)
        
    a=0
    removed_list=[]       
    sentence_list=[]

    for sentence in sentences_values:
        sentence2=[]
        word=""
        for letter in sentence:            
            #I turned the string value into a list so that I can simply check the same values
            if letter!=" ":
                word+=letter
                if len(word)==4:                    
                    sentence2.append(word)
                    word=""
        sentence_list.append(sentence2)
    
    clean_sentences_list=[]
    for list in sentence_list:
        #I checked if words are same in list I appended the new list 
        newlist=[]
        for element in list:
            if element not in newlist:
                newlist.append(element)
                
            else:
                a+=1
                continue
        clean_sentences_list.append(newlist)

    clean_sentence_dict={}

    c=0
    for item in sentences_keys:
        clean_sentence_dict[item]=clean_sentences_list[c]
        c+=1
    print(a)
    return clean_sentence_dict


def write_genes( clean_sentences_dict):
    
    clean_sentences_values = []
    for i in clean_sentences_dict.values():
        clean_sentences_values.append(i)
    clean_sentences_keys = []
    for i in clean_sentences_dict.keys():
        clean_sentences_keys.append(i)

    #I have opened a new file and added the values in it
    with open('.csv', mode='w') as yeni_dosya:
        yeni_yazici = csv.writer(yeni_dosya, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
 
        yeni_yazici.writerow(['fragment_id', 'sentence','sentence_length', 'number_of words'])
        x=0
        for i in clean_sentences_keys:
            yeni_yazici.writerow([i,clean_sentences_values[x],len(clean_sentences_values[x]),(len(clean_sentences_values[x])-1)*5])
            x+=1


def main():
    #I execute all the functions

    gene_dict = read_genes("input.txt")
    frag_dict = get_fragments(gene_dict,50)
    dissimilar_frag_dict = filter_frags(frag_dict,0.7)
    sentences_dict = get_sentences(dissimilar_frag_dict)
    clean_sentences_dict = clean_dict(sentences_dict)
    write_genes(clean_sentences_dict)
main()


