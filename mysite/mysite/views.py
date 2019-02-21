from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html')


def count(request):
    data = request.GET['fullmessage']
    #print(data)
    # Total words Count for this operation
    word_list = data.split()
    word_length = len(word_list)
    #Count each words length
    worddictonary = {}

    for word in word_list:
        if word in worddictonary:
            # Increase value by 1 if word already in dictionary
            worddictonary[word] += 1
        else:
            # if word not in dictionary then set the new word in the dictionary
            worddictonary[word]=1
    sorted_list = sorted(worddictonary.items(), key = operator.itemgetter(1),reverse=True) # reverse = True means here we perform decending order sorting
    return render(request,'count.html', {'fullmessage': data, 'words': word_length,'worddictionary': sorted_list})