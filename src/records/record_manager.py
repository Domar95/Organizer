from ..errors.errors import IndexError


#db - mysql - techwithtim

class RecordManager():
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def view_records(self):
        # needs __str__ on record (maybe inh? or here add this func, or dependency inj and __str__ there)
        for record in self.records:
            print(record)

    def delete_record(self, record_id):
        try:
            del self.records[record_id]
        except:
            print('Wrong record id.')
            raise IndexError(f'Record with id {record_id} does not exist.')

    def load_records_from_db(self, db):
        for record in db:
            self.add_record(record)
