from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .forms import Add_subject
from subject.models import subjects
from django.http import HttpResponse
from django.contrib import messages

class Add_subject_view(View):

    template = 'administrator/add_subject.html'
    def get(self,request):
        return render(request,self.template)

    def post(self,request):
        print(request.POST)
        form = Add_subject(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'subject added')
            return render(request,self.template)
        else :
            return render(request,self.template,{'form':form})


def Subject_view(request):
    subject = subjects.objects.all()
    return render(request,'administrator/sub.html',{'subject':subject})

class Subject_edit_view(View):

    template = 'administrator/edit_subject.html'
    def get(self,request,code):
        print(code)
        subject = get_object_or_404(subjects,code=code)
        form = Add_subject(instance=subject)
        return render(request,self.template,{'form':form,'subject':subject})

    def post(self,request,code):
        subject = get_object_or_404(subjects,code=code)
        form = Add_subject(request.POST,instance=subject)
        if form.is_valid():
            form.save()
            return redirect('/admin/subjects')
        else:
            return render(request, self.template, {'form': form})