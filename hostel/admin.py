from django.contrib import admin

from hostel.views import allocate_room
from .models import Complaint, Student, Room, RoomDetails, Admin, VisitorRequest,Announcement

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('usn', 'name', 'sem', 'branch', 'ph_no', 'email', 'address', 'fathername', 'fphn_no', 'mother_name')
  
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_no', 'no_of_beds', 'is_occupied')
    

@admin.register(RoomDetails)
class RoomDetailsAdmin(admin.ModelAdmin):
    list_display = ('room_no', 'usn', 'name', 'sem')
    


@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('admin_id',)

# @admin.register(allocate_room)
# class AllocateRoom(admin.ModelAdmin):
#     list_display = ('room_no', 'usn', 'name', 'sem')
#     actions = ['allocate_rooms']

#     def allocate_rooms(self, request, queryset):
#         for room_detail in queryset:
#             room = room_detail.room_no
#             room.is_occupied = True
#             room.save()
#             room_detail.save()
#         self.message_user(request, "Rooms allocated successfully.")

#     allocate_rooms.short_description = "Allocate  rooms to students"

@admin.register(VisitorRequest)
class VisitorRequestAdmin(admin.ModelAdmin):
    list_display = ('usn', 'student_name', 'visitor_name', 'relation', 'ph_no', 'visit_date', 'visit_time', 'request_date', 'status')
    search_fields = ('usn', 'student_name', 'visitor_name', 'visit_date')
    list_filter = ('status', 'visit_date')
    
@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display =('title','content','created_at')


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('student', 'complaint_text', 'created_at')
    search_fields = ('student__usn', 'complaint_text')
    list_filter = ('created_at',)

admin.site.register(Complaint, ComplaintAdmin)
