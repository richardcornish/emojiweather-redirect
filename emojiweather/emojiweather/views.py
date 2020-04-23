from django.views.generic import RedirectView


class HomeView(RedirectView):
	url = 'https://emojiweather.app/'
	permanent = True
	query_string = True
