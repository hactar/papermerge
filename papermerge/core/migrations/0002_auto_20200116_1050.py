# Generated by Django 3.0.2 on 2020-01-16 10:50
import os
import logging
from django.apps import apps
from django.db import migrations

logger = logging.getLogger(__name__)


def get_sql(file_name):
    """
    Returns SQL statements from
    papermerge/core/pgsql/*.sql files
    """
    core_path = apps.get_app_config('core').path
    full_sql_file_path = os.path.join(
        core_path,
        "pgsql",
        file_name
    )
    if not os.path.exists(full_sql_file_path):
        logger.debug(f"file {full_sql_file_path} not found")
        return

    sql_content = None
    with open(full_sql_file_path, 'rt') as f:
        sql_content = f.read()
        logger.debug(sql_content)
        return sql_content

    if not sql_content:
        logger.debug(f"No SQL content available. Aborting.")
        return


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(get_sql('01_triggers.sql')),
        migrations.RunSQL(get_sql('02_basetreenode.sql')),
        migrations.RunSQL(get_sql('03_update_lang_cols.sql')),
        migrations.RunSQL(get_sql('04_views.sql')),
    ]