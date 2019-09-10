# Copyright 2019 Google LLC All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START ndb_context_usage]
from google.cloud import ndb

# Creating a model definition does not require a client.
class Book(ndb.Model):
    title = ndb.StringProperty()

client = ndb.Client()

def list_books():
    # To interact with Datastore, get the client's runtime context.
    # All interactions with Datastore need to occur within the runtime context.
    with client.context():
        books = Book.query()
        for book in books:
            print(book.to_dict())
# [END ndb_context_usage]


if __name__ == "__main__":
    list_books()
