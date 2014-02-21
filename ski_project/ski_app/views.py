from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from ski_app.models import Category, Ski_Page
from ski_app.forms import SkiForm, SkiSearchForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from ski_app.bing_search import run_query


def index(request):
	# Request the context of the request.
    # The context contains information such as the client's machine details, for example.
	context = RequestContext(request)
	# Query the database for a list of ALL categories currently stored.
	category_list = Category.objects.all()
	# Construct a dictionary to pass to the template engine as its contextself
	context_dict = {'categories': category_list}

	for category in category_list:
		category.url = category.name.replace(' ', '_')

	if request.session.get('last_visit'):
		last_visit_time = request.session.get('last_visit')
		visits = request.session.get('visits',0)

		if (datetime.now() - datetime.strptime(last_visit_time[:-7], "%Y-%m-%d %H:%M:%S")).days > 0:
			request.session['visits'] = visits + 1
			request.session['last_visit'] = str(datetime.now())

	else:
		request.session['last_visit'] = str(datetime.now())
		request.session['visits'] = 1

	return render_to_response('ski_app/index.html', context_dict, context)



def about(request):
	context = RequestContext(request)

	if request.session.get('visits'):
		count = request.session.get('visits')
	else:
		count = 0

	context_dict =  {'visits': count}

	return render_to_response('ski_app/about.html', context_dict, context)

def category(request, category_name_url):
	context = RequestContext(request)
	category_name = category_name_url.replace('_',' ')
	context_dict = {'category_name': category_name}
	
	filter_dict ={}
	filter_dict['category'] = Category.objects.get(name=category_name)

	context_dict['form'] = form = SkiSearchForm(request.GET)
	if form.is_valid():
		for key, value in form.cleaned_data.items():
			if value:
				print value
				filter_dict[key] = value

	try:
		category = Category.objects.get(name=category_name)
		pages = Ski_Page.objects.filter(**filter_dict).order_by('brand','model_name')
		context_dict['pages'] = pages
		context_dict['category'] = category
	except Category.DoesNotExist:
		pass

	for page in pages:
			page.url = page.model_name.replace(' ','_')

	return render_to_response('ski_app/category.html',context_dict, context)

def item(request, item_name_url):
	# individual ski page entry
	context = RequestContext(request)
	item_name = item_name_url.replace('_',' ')
	context_dict = {'item_name': item_name}

	try:
		item = Ski_Page.objects.get(model_name=item_name)
		context_dict['item'] = item
	except Ski_Page.DoesNotExist:
		pass

	return render_to_response('ski_app/item.html',context_dict, context)

@login_required
def add_ski(request):
	# restricted view that allows users to add a ski
	context = RequestContext(request)

	if request.method == 'POST':
		form = CategoryForm(request.POST)

		if form.is_valid():
			form.save(commit=True)

			return index(request)
		else:
			print form.errors

	else:
		form = SkiForm()
		
	return render_to_response('ski_app/add_ski.html', {'form': form}, context)

def register(request):
	# view that allows new users to register
	context = RequestContext(request)

	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()

			registered = True

		else:
			print user_form.errors, profile_form.errors

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render_to_response('ski_app/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context )

def user_login(request):
	# view that allows existing users to login
	context = RequestContext(request)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect('/ski_app/')
			else:
				return HttpResponse("Your ski_app account is disabled.")
		else:
			print "Invalid login details: {0}, {1}". format(username, password)
			return HttpResponse("Invalid login details supplied.")

	else:
		return render_to_response('ski_app/login.html',{}, context)


@login_required
def user_logout(request):
	logout(request)

	return HttpResponseRedirect('/ski_app/')

def search(request):
	context = RequestContext(request)
	result_list = []

	if request.method =='POST':
		query = request.POST['query'].strip()

		if query:
			result_list = run_query(query)

	return render_to_response('ski_app/search.html', {'result_list':result_list}, context)
