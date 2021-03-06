Schema Migrations
=================

Over time, the ORM models in your application may change. Migrations provide a way to modify the database tables according to the changes in your models, without writing raw SQL.

The migrations that were applied to the database are recorded in the `infi_clickhouse_orm_migrations` table, so migrating the database will only apply any missing migrations.

Writing Migrations
------------------

To write migrations, create a Python package. Then create a python file for the initial migration. The migration files must begin with a four-digit number, and will be applied in sequence. For example:

    analytics
       |
       +-- analytics_migrations
              |
              +-- __init__.py
              |
              +-- 0001_initial.py
              |
              +-- 0002_add_user_agents_table.py

Each migration file is expected to contain a list of `operations`, for example:

    from infi.clickhouse_orm import migrations
    from analytics import models

    operations = [
        migrations.CreateTable(models.Visits),
        migrations.CreateTable(models.Visitors)
    ]

The following operations are supported:

**CreateTable**

A migration operation that creates a table for a given model class. If the table already exists, the operation does nothing.

In case the model class is a `BufferModel`, the operation first creates the underlying on-disk table, and then creates the buffer table.

**DropTable**

A migration operation that drops the table of a given model class. If the table does not exist, the operation does nothing.

**AlterTable**

A migration operation that compares the table of a given model class to the model’s fields, and alters the table to match the model. The operation can:

-   add new columns
-   drop obsolete columns
-   modify column types

Default values are not altered by this operation.

**AlterTableWithBuffer**

A compound migration operation for altering a buffer table and its underlying on-disk table. The buffer table is dropped, the on-disk table is altered, and then the buffer table is re-created. This is the procedure recommended in the ClickHouse documentation for handling scenarios in which the underlying table needs to be modified.

Applying this migration operation to a regular table has the same effect as an `AlterTable` operation.


Running Migrations
------------------

To migrate a database, create a `Database` instance and call its `migrate` method with the package name containing your migrations:

    Database('analytics_db').migrate('analytics.analytics_migrations')

Note that you may have more than one migrations package.


---

[<< Table Engines](table_engines.md) | [Table of Contents](toc.md) | [System Models >>](system_models.md)