from django.db import migrations

def seed_tracks(apps, schema_editor):
    Track = apps.get_model("tracks", "Track")
    for name in ["Odoo", "Python", "Django"]:
        Track.objects.get_or_create(name=name)

def remove_seed_tracks(apps, schema_editor):
    Track = apps.get_model("tracks", "Track")
    Track.objects.filter(name__in=["Odoo", "Python", "Django"]).delete()

class Migration(migrations.Migration):
    dependencies = [("tracks", "0001_initial")]
    operations = [migrations.RunPython(seed_tracks, remove_seed_tracks)]
