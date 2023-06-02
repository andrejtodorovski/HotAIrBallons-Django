from django.shortcuts import render
from .models import Flight
# Create your views here.
from django.http import HttpResponse
from .forms import FlightForm


def index(request):
    form = FlightForm()

    if request.method == 'POST':
        form = FlightForm(request.POST, request.FILES)
        if form.is_valid():
            flight = form.save(commit=False)  # Save the form data but don't commit to the database yet
            flight.user = request.user  # Assign the current user to the flight object
            flight.save()  # Save the flight object with the user assigned
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    print(f"Error in {field}: {error}")
            return HttpResponse("Form is not valid")
    queryset = Flight.objects.all()
    context = {"flights": queryset, "form": form}
    return render(request, "index.html", context=context)


def home(request):
    return render(request, "home.html")
