from django.shortcuts import render, redirect
from documentation.models import Article
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError


def documentation(request):
    return render(request, "documentation/documentation.html")


def open_article(request, selectedTitle):

    try:
        article = Article.objects.get(Title=selectedTitle)
        context = {"selectedTitle":selectedTitle, "content":article.Content, "description":article.Description, "keywords":article.Keywords}
        return render(request, "documentation/article.html", context)

    except ObjectDoesNotExist:
        message = "<h1>This title not exist<h1>"
        context = {"selectedTitle":selectedTitle, "content":message, "description":"", "keywords":""}
        return render(request, "documentation/article.html", context)
    

def edit_article(request, selectedTitle):

    if request.user.is_superuser:  

        try:
            article = Article.objects.get(Title=selectedTitle)
            context = {"selectedTitle":selectedTitle, "selectedContent":article.Content, "selectedDescription":article.Description, "selectedKeywords":article.Keywords}
        
        except ObjectDoesNotExist:
            context = {"selectedTitle":selectedTitle, "selectedContent":"", "selectedDescription":"", "selectedKeywords":""}
            
        return render(request, "documentation/edit_article.html", context)
    
    else:
        return redirect("/home/")   
    

def save_change(request, selectedTitle):
    
    if request.user.is_superuser:  

        title = request.POST.get("title")
        content = request.POST.get("content")
        description = request.POST.get("description")
        keywords = request.POST.get("keywords") 

        edited_title = " ".join(title.split()).title().replace(" ", "_") 
        if edited_title[-1] == "?":
            final_edited_title = edited_title[:-1] + "_"
        else:
            final_edited_title = edited_title 

        if selectedTitle == "create":
            
            try:
                new_article = Article(Title=final_edited_title, Content=content, Description=description, Keywords=keywords)
                new_article.save()
                return redirect("/documentation/open_article/"+final_edited_title)
            
            except IntegrityError:
                error_message = "This Title selected before please select another"
                context = {"message": error_message, "title": final_edited_title}
                
                return render(request, "documentation/error_message.html", context)
        
        elif title == "delete":
            article = Article.objects.get(Title=selectedTitle)
            article.delete()
            return render(request, "documentation/documentation.html")

        elif final_edited_title == selectedTitle:
            article = Article.objects.get(Title=selectedTitle)
            article.Content = content
            article.Description = description
            article.Keywords = keywords
            article.save()
            return redirect("/documentation/open_article/"+final_edited_title)

        elif final_edited_title != selectedTitle:

            try:
                new_article = Article(Title=final_edited_title, Content=content, Description=description, Keywords=keywords)
                new_article.save()
                
                old_article = Article.objects.get(Title=selectedTitle)
                old_article.delete()
                return redirect("/documentation/open_article/"+final_edited_title)
            
            except IntegrityError:
                error_message = "This Title selected before please select another"
                context = {"message": error_message, "title": final_edited_title}
                
                return render(request, "documentation/error_message.html", context)

    else:
        return redirect("/home/")