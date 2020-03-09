from django.shortcuts import redirect, render, get_object_or_404, Http404
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils import timezone
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from .models import Journal 
from .forms import JournalForm
from Comments.models import Comment 
from Comments.forms import CommentForm


def journal_edit(request, id):
	journal = get_object_or_404(Journal, id=id) 
	form = JournalForm(request.POST or None, instance=journal)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Journal edited successfully")
		return redirect(instance.get_absolute_url())

	context = {
				"title": "Edit",
				"form": form
			  }
	return render(request, "journal_edit.html", context)

def journal_new(request):
	form = JournalForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		# print(form.cleaned_data)
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()	
		messages.success(request, "Journal Saved successfully")
		return redirect(instance.get_absolute_url())



	context = {
				"title": "New Journal", 
				"form": form,
			  }
	return render(request, "journal_new.html", context)

def fetch_by_slug(request, inp_slug):
	journal = get_object_or_404(Journal, slug=inp_slug)
	if "j_del" in request.POST:
		return redirect("Journals:del", inp_slug=inp_slug)
		
	# extracting comments
	comments = Comment.objects.filter_by_instance(journal)

	# feature to add the comments
	initial_data = {
					 "content_type": journal.get_content_type,
					 "object_id": journal.id
				   }
	form = CommentForm(request.POST or None, initial=initial_data)
	if form.is_valid():
		print(form.cleaned_data)
		ctype = form.cleaned_data.get('content_type')
		content_type = ContentType.objects.get(model=ctype)
		object_id = form.cleaned_data.get("object_id")
		comment_data = form.cleaned_data.get("content")
		# adding the comment
		new_comment, is_success = Comment.objects.get_or_create(user=request.user,
																content_type=content_type,
																object_id=object_id,
																content=comment_data)

		return redirect(journal.get_absolute_url())

	context = {
				"title": "Journal",
				"journal": journal,
				"comments": comments,
				"comment_form": form
			  }
	return render(request, "journal_slug.html", context)



def fetch_by_id(request, id):
	journal = get_object_or_404(Journal, id=id) 

	context = {
				"title": journal.id,
				"journal": journal,
			  }
	return render(request, "journal_id.html", context)



def journals_all(request):
	if not request.user.is_authenticated:
		raise Http404("LOGIN REQUIRED!!!")
	# j_all = Journal.objects.all().order_by("-last_updated") # retrieves all the objects
	j_all = Journal.objects.filter(user=request.user).order_by("-last_updated")
	j_all = j_all.filter(publish__lte=timezone.now())

	search_q = request.GET.get("search")
	if search_q:
		j_all = j_all.filter(title__icontains=search_q)

	data_per_page = 4
	j_paginator = Paginator(j_all, data_per_page)
	page = request.GET.get('page')
	j_all = j_paginator.get_page(page)

	context = {
				"title": "All journals",
				"journals_all": j_all,
			  }

	return render(request, "journals_all.html", context)

def journal_delete(request,inp_slug):
	journal = get_object_or_404(Journal, slug=inp_slug)
	context = {
				"title" : "delete",
				"journal" : journal,
	          }
	if 'conf_del' in request.POST:
		journal.delete()
		return redirect("Journals:all")
	elif 'No' in request.POST:
		return redirect("Journals:all")
			
	return render(request, "journal_delete.html", context)

	# journal.delete()
	
