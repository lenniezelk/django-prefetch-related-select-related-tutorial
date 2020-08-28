# Generated by Django 3.1 on 2020-08-28 08:27

from django.db import migrations


def add_data(apps, _):
    Launch = apps.get_model("launches", "Launch")
    LaunchPad = apps.get_model("launches", "LaunchPad")
    Rocket = apps.get_model("launches", "Rocket")
    Crew = apps.get_model("launches", "Crew")
    Core = apps.get_model("launches", "Core")

    core1 = Core.objects.create(serial="Core 1")
    core2 = Core.objects.create(serial="Core 2")

    launch_pad1 = LaunchPad.objects.create(name="LaunchPad 1")
    launch_pad2 = LaunchPad.objects.create(name="LaunchPad 2")

    crew1 = Crew.objects.create(name="Crew 1")
    crew2 = Crew.objects.create(name="Crew 2")
    crew3 = Crew.objects.create(name="Crew 3")

    rocket1 = Rocket.objects.create(name="Rocket 1", core=core1)
    rocket2 = Rocket.objects.create(name="Rocket 2", core=core2)

    launch1 = Launch.objects.create(
        name="Launch 1", launch_pad=launch_pad1, rocket=rocket1
    )

    launch2 = Launch.objects.create(
        name="Launch 2", launch_pad=launch_pad2, rocket=rocket2
    )

    launch1.crew.set([crew1, crew2])
    launch2.crew.set([crew1, crew3, crew2])


class Migration(migrations.Migration):

    dependencies = [
        ("launches", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(add_data, migrations.RunPython.noop, atomic=True)
    ]