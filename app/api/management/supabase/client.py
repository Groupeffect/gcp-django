from supabase import create_client, Client
from backend.settings import SUPABASE_URL, SUPABASE_TOKEN, SUPABASE_JWT
class SupabaseClient:
    def __init__(self):
        self.url: str = SUPABASE_URL
        self.key: str = SUPABASE_TOKEN
        self.jwt: str = SUPABASE_JWT
        self.client: Client = create_client(self.url, self.key)
        self.response = None

    def table(self, table: str):
        return self.client.table(table).select("*").execute()
    
    def insert(self, table: str, data: dict):
        return self.client.table(table).insert(data).execute()
    
    def update(self, table: str, id: str, data: dict):
        return self.client.table(table).update(data).eq("id", id).execute()
    
    def test(self):

        print(self.table("pictures"))
    