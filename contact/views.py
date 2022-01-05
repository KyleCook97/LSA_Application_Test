from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Contact

# Create your views here.

#@login_required will not allow a user to access the index page without being logged in
@login_required
def index(request):
    contacts = Contact.objects.all()

    #input from the search bar is stored then used to sort through the list of contacts
    search_input = request.GET.get('search-area')

    #display all contacts that contain the searched string
    if search_input:
        contacts = Contact.objects.filter(full_name__icontains = search_input)

    #if the search bar is empty, display all contacts
    else:
        contacts = Contact.objects.all()
        search_input = ''
    return render(request, 'index.html', {'contacts': contacts, 'search_input': search_input})

#creates new contact then redirects user back to index page
def addContact(request):
    if request.method == 'POST':
        new_contact = Contact(
            full_name = request.POST['fullname'],
            relationship = request.POST['relationship'],
            email = request.POST['email'],
            phone_number = request.POST['phone-number'],
            address = request.POST['address']
        )
        new_contact.save()
        return redirect('/')
    return render(request, 'new.html')

#loads the contact page for the id of pk, where pk is an int
def contactProfile(request, pk):
    contact = Contact.objects.get(id=pk)
    return render(request, 'contact-profile.html', {'contact': contact})

#user can edit a preexisting contact or delete a contact with an id = pk
def editContact(request, pk):
    contact = Contact.objects.get(id=pk)

    #once the new information is added in, redirect the user back to the contact profile page
    if request.method == 'POST':
        contact.full_name = request.POST['fullname']
        contact.relationship = request.POST['relationship']
        contact.email = request.POST['email']
        contact.phone_number = request.POST['phone-number']
        contact.address = request.POST['address']
        contact.save()

        return redirect('/profile/' + str(contact.id))
    return render(request, 'edit.html', {'contact': contact})

#takes the user to the delete page to confirm if the contact should be deleted 
def deleteContact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('/')
    return render(request, 'delete.html', {'contact': contact})