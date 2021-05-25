from django.shortcuts import render
from . import models as member_models


def member_list_view_handler(request):

    members = member_models.MemberModel.objects.all()

    for mem in members:
        if mem.pk % 2 == 0:
            mem.isEven = True
        else:
            mem.isEven = False

    return render(request, "screens/member_list.html", context={"members": members})
