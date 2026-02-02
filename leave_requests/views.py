from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import LeaveRequest
from .forms import LeaveRequestForm


from django.shortcuts import redirect
class LeaveListView(ListView):
    """Display all leave requests and handle new request submission."""
    model = LeaveRequest
    template_name = 'leave_requests/leave_list.html'
    context_object_name = 'leave_requests'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = LeaveRequestForm()
        if 'title' not in context:
            context['title'] = 'Submit New Leave Request'  # For the modal header if we made it dynamic
        return context

    def post(self, request, *args, **kwargs):
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leave_list')
        
        # If invalid, re-render the list with the invalid form
        self.object_list = self.get_queryset()
        context = self.get_context_data(object_list=self.object_list, form=form, show_modal=True)
        return self.render_to_response(context)


class LeaveUpdateView(UpdateView):
    """Edit an existing leave request."""
    model = LeaveRequest
    form_class = LeaveRequestForm
    template_name = 'leave_requests/leave_list.html'
    success_url = reverse_lazy('leave_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # We need the list of requests to render the table background
        context['leave_requests'] = LeaveRequest.objects.all()
        context['title'] = 'Edit Leave Request'
        context['button_text'] = 'Update Request'
        return context

    def form_invalid(self, form):
        # Override to show the modal with errors on the list page
        context = self.get_context_data(form=form)
        context['show_modal'] = True
        return self.render_to_response(context)
