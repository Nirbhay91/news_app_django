
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import News
from .forms import NewsForm

def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'news/create_news.html', {'form': form})

def news_list(request):
    news_items = News.objects.all()
    return render(request, 'news/news_list.html', {'news_items': news_items})

def edit_news(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news_item)
        if form.is_valid():
            form.save()
            return redirect('news_detail', pk=pk)
    else:
        form = NewsForm(instance=news_item)
    return render(request, 'news/edit_news.html', {'form': form})

def delete_news(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        news_item.delete()

    
    # return render(request, 'news/news_detail.html', {'news_item': news_item})


