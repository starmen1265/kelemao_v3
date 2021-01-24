from django.shortcuts import render

def index(request):
    index_var = "第一次欢迎你"
    index2_var ="第二次欢迎你"
    return render(request,'index.html',{"index":index_var,"index2":index2_var})