from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("create", views.create, name="create"),
    path("insert", views.insert, name="insert"),
    path("categories/", views.categories, name="categories"),
    path("categories/<str:category>", views.filterCategories, name="category"),

    path("listing/<int:id>", views.listing, name="listing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("watch/<int:id>", views.watch, name="watch"),
    path("unwatch/<int:id>", views.unwatch, name="unwatch"),
    path("update-bid/<int:id>", views.update_bid, name="update_bid"),
    path("close-bid/<int:id>", views.close_bid, name="close_bid"),
    path("comments/<int:id>", views.add_comment, name="add_comment"),

    path("comment/status/<int:id>", views.comment_status, name="comment-status")
]
