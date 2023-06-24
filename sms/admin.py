from django.contrib import admin

from .models import Type


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = "pk", "text_short", "type", "keys", "created_at"
    list_display_links = "pk", "text_short"

    def text_short(self, obj: Type) -> str:
            return obj.text["uz_cyrl"][:48] + " ....."
    
