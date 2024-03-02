from django.shortcuts import render

def draw_menu_view(request):

    return render(request, 'treemenu/draw_menu.html')
