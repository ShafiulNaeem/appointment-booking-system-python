from db.migrations.UserMigration import UserMigration

migrations = [
    UserMigration()
]

for migration in migrations:
    migration.up()