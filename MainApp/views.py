from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound

countries=[
{"страна" : "Аруба", "языки" : ["Голландский","Английский", "Папиаменто", "Испанский"]},
{"страна" : "Афганистан", "языки" : ["Белуджи", "Дари", "Пушту", "Туркменский", "Узбек"]},
{"страна" : "Ангола", "языки" : ["Амбо" , "Чокве" , "Конго" , "Лучази" , "Луимбенгангела" , "Лювале" ,"Мбунду" ,"Ньянека-нхумби","Овимбунду"]},
{"страна" : "Ангилья", "языки" : ["Английский"]},
{"страна" : "Албания" , "языки" : ["Албана" ,"Греческий" ,"Македонский"]},
{"страна" : "Андорра" , "языки" : ["Каталонский" ,"Француз" ,"Португальский"]},
{"страна" : "Нидерландские Антильские острова" , "языки" : ["Голландский","Английский", "Папиаменто"]},
{"страна" : "Объединенные Арабские Эмираты" , "языки" : ["Арабский" , "Хинди"]}
]




# Create your views here.
def hello(request):
    return render(request, 'index.html')

def count_page(request, count):
    for i in countries:
        if i['страна'] == count:
            page =f"<h1> {i['страна']} </h1><ul>"
            for j in i['языки']:
                page+=f"<li>{j.title()}</li>"
            page+=f"""
            </ul>
            <a href='/countries-list'>К списку стран</a>
            """
            return HttpResponse(page)
    return HttpResponseNotFound(f"Такой страны {count} в списке нет")


def countries_list(request):
    context={
        "countries":countries
    }
    return render(request,"countries_list.html", context)


def languages(request):
    page = "<h1>Языки</h1><ol>"
    res=[]
    for i in countries:
        for j in i['языки']:
            res.append(j)
    set_res=list(set(res))
    set_res.sort()
    for i in set_res:
        page += f"<li><a href='l/{i}'>{i}</a></li>"
    page+=f"""
    </ol>
    <a href='/'> На главную страницу</a>
    """
    return HttpResponse(page)

def lang_count(request, lang):
    page="<h1> Список стран</h1><ol>"
    for i in countries:
        for j in i['языки']:
            if j == lang:
                page += f"<li>{i['страна']}</li>"
    page+=f"""
    </ol>
    <a href='/'> На главную страницу</a>
    """
    return HttpResponse(page)
