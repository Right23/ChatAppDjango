
import datetime
from django.db import migrations, models

# lop Migration dung de quan ly cac phien ban cua CSDL, dai dien cho mot migration ban dau cua ung dung chat
class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        # co 2 mo hinh Message va Room duoc tao ra
        # truong id dinh danh cho cac ban ghi trong CSDL
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=1000000)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.CharField(max_length=1000000)),
                ('room', models.CharField(max_length=1000000)),
            ],
        ),
        # truong name luu tru ten phong chat
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
    ]
