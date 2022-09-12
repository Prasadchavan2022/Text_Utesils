# VIEW FILE CREATED BY @_PRASAD CHAVAN
import os
from django.http import HttpResponse

# for importing templates in django
from django.shortcuts import render

# sample demo of return request
def index(request):
    return render(request, 'index2.html')

def analyze(request):
    djText = request.POST.get('text', 'default')
    # print(djText)  #getting name from submitted text form in html
    removepunc = request.POST.get('removepunc', 'off')  #this will print on if checkbox is on
    capitalize = request.POST.get('capitalize', 'off')  #this will print on if checkbox is on
    findLen = request.POST.get('findLen', 'off')
    newLineremover = request.POST.get('newLineremover', 'off')
    #analyzing text using for loop
    analyze_text = ""
    punctuations = ''':;.,/\|{}[]()8*&^%$#@!~`+=-_<'>?"'''
    if removepunc == 'on':
        for char in djText:
            if char not in punctuations:
                analyze_text = analyze_text + char
    else:
        analyze_text = djText
    if capitalize == 'on':
        analyze_text = analyze_text.capitalize()
    if findLen == 'on':
        l = str(len(analyze_text))
    else:
        l = " Not Specified"
    if newLineremover == 'on':
        temp = analyze_text
        analyze_text = ""
        for char in temp:
            if char != "\n" and char != "\r":
                analyze_text = analyze_text + char

    param = {'analyzed_text': analyze_text, 'length': l}
    return render(request, 'analyze2.html', param)  #returns Capitalized string
