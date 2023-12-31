# Generated by Django 3.0 on 2023-07-04 15:44
from django.apps import apps as global_apps
from django.db import migrations


def datamigrations(apps, schema_editor):
    try:
        OldAddress = apps.get_model('oc_lettings_site', 'Address')
        OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    except LookupError:
        print('old app not installed')
        return

    NewAdress = apps.get_model('lettings', 'Address')
    NewAdress.objects.bulk_create(
        NewAdress(number=old_object.number,
                  street=old_object.street,
                  city=old_object.city,
                  state=old_object.state,
                  zip_code=old_object.zip_code,
                  country_iso_code=old_object.country_iso_code)
        for old_object in OldAddress.objects.all()
    )

    NewLetting = apps.get_model('lettings', 'Letting')
    NewLetting.objects.bulk_create(
        NewLetting(
            title=old_object.title,
            address_id=old_object.address_id)
        for old_object in OldLetting.objects.all()
    )


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(datamigrations),
    ]

