from django.urls import path
from .views import ArtikelListView, ArtikelDetailView, ArtikelKategoriListView

urlpatterns = [
	path('kategori/<str:kategori>/', ArtikelKategoriListView.as_view(), name='category'),
	path('kategori/<str:kategori>/<int:page>', ArtikelKategoriListView.as_view(), name='category'),
	path('<slug:slug>/', ArtikelDetailView.as_view(), name='detail'),
	path('page/<int:page>', ArtikelListView.as_view(), name='list'),
	path('', ArtikelListView.as_view(), name='list'),
]