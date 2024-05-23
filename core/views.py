from django.shortcuts import render,get_object_or_404
from .form import Cv
from .models import Image
# Create your views here.
def main(request):
    if request.method=='POST':
        form=Cv(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form=Cv()
    candidates=Image.objects.all()
    return render(request,'forms.html',{'form':form,'candidates':candidates})
def candidate_detail(request,candidate_id):
    candidate=get_object_or_404(Image,id=candidate_id)
    return render(request,'person.html',{'candidate':candidate})
