from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import EventoViewSet


router = DefaultRouter()
router.register(r'eventos', EventoViewSet, basename='evento')

urlpatterns = [
    path('eventos/count-total-csv/', EventoViewSet.as_view({'get': 'count_total_events_csv'}), name='count_total_events_csv'),
    path('eventos/count-by-region/', EventoViewSet.as_view({'get': 'count_events_by_region'}), name='count_events_by_region'),
    path('eventos/count-by-region-and-day/', EventoViewSet.as_view({'get': 'count_events_by_region_and_day'}), name='count_events_by_region_and_day'),
    path('eventos/count-in-month/<int:month>/', EventoViewSet.as_view({'get': 'count_events_in_month'}), name='count_events_in_month'),
    path('eventos/user-with-most-events/', EventoViewSet.as_view({'get': 'user_with_most_created_events'}), name='user_with_most_created_events'),
    path('eventos/list-event-participants/', EventoViewSet.as_view({'get': 'list'}), name='list'),
    path('eventos/add_participant_event/<int:id>/', EventoViewSet.as_view({'get': 'add_participant_event'}), name='add_participant_event'),
    path('eventos/update/<int:id>', EventoViewSet.as_view({'put': 'update'}), name='update')

]
