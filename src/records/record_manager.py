from ..errors.errors import IndexError

class RecordManager():
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)
    
    def view_records(self):
        #needs __str__ on record (maybe inh? or here add this func, or dependency inj and __str__ there)
        for record in self.records:
            print(record)

    def delete_record(self, record_id):
        try:
            del self.records[record_id]
        except:
            print('Wrong record id.')
            raise IndexError(f'Product with id {record_id} does not exist.')