from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_management', '0005_alter_exercise_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
    ]
