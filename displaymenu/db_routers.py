class SecondDbRouter:
    """
    A router to control all database operations on models in the
    displaymenu application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read displaymenu models go to second_db.
        """
        if model._meta.app_label == 'displaymenu':
            return 'second_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write displaymenu models go to second_db.
        """
        if model._meta.app_label == 'displaymenu':
            return 'second_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the displaymenu app is involved.
        """
        if obj1._meta.app_label == 'displaymenu' or \
            obj2._meta.app_label == 'displaymenu':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the displaymenu app only appears in the 'second_db'
        database.
        """
        if app_label == 'displaymenu':
            return db == 'second_db'
        return None
