from db_api import LogRepository
from db_provider import PostgresProvider
import datetime

# example of client code
provider = PostgresProvider()
log_repo = LogRepository(provider)
log_repo.create(data={"timestamp": datetime.datetime.now(), "type": "test_type", "message": "test_message"})
log_id = 1
'''log_repo.update(
    log_id=log_id, data={"timestamp": datetime.datetime.now(), "type": "test_type", "message": "test_message"}
)'''
print(log_repo.read(log_id))
