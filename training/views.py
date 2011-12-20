# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
def main_page(request):
	# get template
	template = get_template('main_page.html')
	# set variables
	variables = Context({
		     'head_title': '===Django Training 20090724 ===',
			      'page_title': 'Welcome to Django Training!',
				       'page_body': 'Where you can open your eyes!'
					     })
	# render variables to template
	output = template.render(variables)
	# return output
	return HttpResponse(output)

# add index page
def index_page(request):
	# get template
	template = get_template('index.html')
	# set variables
	variables = Context({
		     'page_title': '===Django Training 20090724 ===',
					     })
	# render variables to template
	output = template.render(variables)
	# return output
	return HttpResponse(output)

from training.models import *
def employee_page(request,name1):
  try:
     employee = Employee.objects.get(name=name1)
  except:
     raise Http404('Requested employee not found.')

  template = get_template('employee_page.html')
  variables = Context({
     'name': employee.name,
     'mobile': employee.mobile,
     'computer': employee.computers
  })
  output = template.render(variables)
  return HttpResponse(output)

def book_list_page(request):
    title = 'Book List'
    template = get_template('books.html')
    books = Book.objects.all()
    variables = Context({
	'title':title,
	'books':books
	})
    output = template.render(variables)
    return HttpResponse(output)
