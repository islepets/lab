from django.db import migrations
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

def create_groups(apps, schema_editor):
    # Получаем модели
    Call = apps.get_model('calls', 'Call')
    Client = apps.get_model('calls', 'Client')
    Reason = apps.get_model('calls', 'Reason')
    Operator = apps.get_model('calls', 'Operator')
    Status = apps.get_model('calls', 'Status')

    # Создаем группы
    operator_group, created = Group.objects.get_or_create(name='Оператор')
    manager_group, created = Group.objects.get_or_create(name='Менеджер')

    # Получаем ContentType для моделей
    call_ct = ContentType.objects.get_for_model(Call)
    client_ct = ContentType.objects.get_for_model(Client)
    reason_ct = ContentType.objects.get_for_model(Reason)
    operator_ct = ContentType.objects.get_for_model(Operator)
    status_ct = ContentType.objects.get_for_model(Status)

    # Получаем все разрешения для моделей
    call_perms = Permission.objects.filter(content_type=call_ct)
    client_perms = Permission.objects.filter(content_type=client_ct)
    reason_perms = Permission.objects.filter(content_type=reason_ct)
    operator_perms = Permission.objects.filter(content_type=operator_ct)
    status_perms = Permission.objects.filter(content_type=status_ct)

    # Назначаем разрешения для Оператора
    operator_group.permissions.set([
        *call_perms.filter(codename__in=['add_call', 'view_call', 'change_call']),
        *client_perms.filter(codename__in=['view_client']),
        *reason_perms.filter(codename__in=['view_reason']),
        *operator_perms.filter(codename__in=['view_operator']),
        *status_perms.filter(codename__in=['view_status']),
    ])

    # Назначаем все разрешения для Менеджера
    manager_group.permissions.set([
        *call_perms,
        *client_perms,
        *reason_perms,
        *operator_perms,
        *status_perms,
    ])

class Migration(migrations.Migration):
    dependencies = [
        ('calls', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]