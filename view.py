# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def count(request):
    user_text = request.GET['text']
    total_count = len(user_text)
    word_dict = {}
    for word in user_text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    sort_dict = sorted(word_dict.items(), key=lambda w: w[1], reverse=True)

    return render(request, 'count.html',
                  {'count': total_count, 'text': user_text,
                   'worddict': word_dict, 'sorted': sort_dict})
