from django.views.generic.edit import CreateView,FormView
from accounts.models import User
from vendors.models import Manager,Operator
from vendors.forms import OwnerCreationForm, ManagerCreationForm, OperatorCreationForm


class OwnerCreateView(CreateView):
    template_name = "signup.html"
    form_class = OwnerCreationForm
    success_url = "/"


class ManagerCreateView(FormView):
    template_name = "signup.html"
    model = Manager
    form_class = ManagerCreationForm
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        return context
    
    def form_valid(self, form):
        cd = form.cleaned_data
        user = User.objects.create(email = cd.get("email"),password=cd.get("password"))
        staff = Manager.objects.create(user=user)
        user.save()
        staff.save()
        return super().form_valid(form)
    


class OperatorCreateView(FormView):
    template_name = "signup.html"
    form_class = OperatorCreationForm
    success_url = "/"

